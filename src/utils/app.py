import json
import csv
import os
import time
from datetime import datetime
import streamlit as st
import pandas as pd
from pandas import json_normalize
# from cryptography.fernet import Fernet
SEP = os.sep

########### ENCRIPTADO ############
'''
key = b'2M1J9aDVarGbGaI0iU23bdbsfX9OGBgFODaU-Jxhm-w='
objeto_cifrado = Fernet(key)

def encriptar(texto):
    texto_encriptado = objeto_cifrado.encrypt(str.encode(texto))
    return texto_encriptado

def desencriptar(encriptado):
    texto_bytes = objeto_cifrado.decrypt(encriptado)
    resultado = texto_bytes.decode()
    return resultado
'''

########### ESTADÍSTICAS ############


ruta_historial = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + SEP + 'resources' + SEP + 'data' + SEP + 'historial' + SEP
ruta_gestion = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + SEP + 'resources' + SEP + 'data' + SEP + 'users' + SEP
columnas_compras = [
    'User',
    'Nombre',
    'Apellidos',
    'Edad',
    'Sala',
    'Pelicula',
    'Fecha',
    'Hora'
]
columnas_registros = [
    'User',
    'Nombre',
    'Apellidos',
    'Edad',
    'Registro',
    'Fecha',
    'Hora'
]


def ver_historial(tipo):
    """Leer y visualizar los datos de un fichero .csv
    Parameters
    ----------
    tipo : str
        nombre del archivo
    Returns
    -------
    Pandas DataFrame
        Devuelve un DataFrame con los datos
    """
    df_historial= pd.read_csv(ruta_historial + tipo)
    return df_historial

def ver_porcentajes():
    """Abre y lee un archivo JSON y selecciona los datos requeridos para mostrarlos por pantalla.
    """
    with open(ruta_gestion + 'gestion.json') as file:
        salas = json.load(file)
    for sala in range(0, 5):
        aforo_total = salas['Salas'][sala]['Aforo total']
        aforo_act = salas['Salas'][sala]['Aforo actual']
        st.write(salas['Salas'][sala]['Numero Sala'])
        st.write(f'Hay **{aforo_act}** butacas reservadas de un total de **{aforo_total}**')
        porcentaje = round((aforo_act * 100) / aforo_total, 2)
        st.write(f'El aforo disponible es del **{porcentaje} %**')
        st.write('------------------------------------------------------------')


########### GESTIÓN DE USUARIOS ############


ruta_gestion = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + SEP + 'resources' + SEP + 'data' + SEP + 'users' + SEP


def nuevo_usuario(usuario, nombre, apellidos, edad, dni, contraseña):
    """Abre y lee un JSON, comprueba si existe o no el dato y si no existe, lo añade y sobreescribe al JSON.
    Además guarda el registro en un archivo CSV.
    Parameters
    ----------
    usuario : str
        Nickname del usuario.
    nombre : str
        Nombre del usuario
    apellidos : str
        Apellidos del usuario
    edad : int
        Edad del usuario
    dni : str
        DNI del usuario
    contraseña : str
        Contraseña del usuario
    """
    with open(ruta_gestion + 'gestion.json') as file:
        users = json.load(file)
    lista_dni = []
    lista_nickname = []
    for cliente in users['Clientes']:
        if dni in cliente.values():
            lista_dni.append(True)
        else:
            lista_dni.append(False)
        if usuario in cliente.values():
            lista_nickname.append(True)
        else:
            lista_nickname.append(False)
    if (True in lista_dni):
        st.error('El usuario ya está registrado. Inicia sesión.')
    elif (True in lista_nickname):
        st.error('El nombre de usuario ya está en uso. Por favor, elige otro.')
    else:
        with open(ruta_historial + 'historial_registros.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columnas_registros)
            writer.writerow({
            'User': usuario,
            'Nombre': nombre,
            'Apellidos': apellidos,
            'Edad': int(edad),
            'Registro': 'Alta',
            'Fecha': datetime.today().strftime('%d-%m-%Y'),
            'Hora': datetime.now().strftime('%H:%M')
            })
            csvfile.close()
        users['Clientes'].append({
            'Usuario': usuario,
            'Nombre': nombre,
            'Apellidos': apellidos,
            'Edad': int(edad),
            'DNI': dni,
            'Password': contraseña
        })
        with open(ruta_gestion + 'gestion.json', 'w') as file:
            json.dump(users, file, indent=4)
        st.success('¡GRACIAS POR REGISTRARTE!')
        st.balloons()


def login_user(usuario, password):
    """Lee un archivo JSON. Comprueba que el usuario existe y la contraseña coincide con los datos.
    Parameters
    ----------
    usuario : str
        Descripción del parametro
    password : str
        Descripción del parametro
    Returns
    -------
    list
        Devuelve una lista de False o una lista con True si el usuario y su contraseña coinciden
    """
    lista_pass = []
    with open(ruta_gestion + 'gestion.json') as file:
        usuarios = json.load(file)
    for i in usuarios['Clientes']:
        if (i['Password'] == password) and (i['Usuario'] == usuario):
            lista_pass.append(True)
        else:
            lista_pass.append(False)
    return lista_pass



def ver(tipo):
    """Abre y lee un archivo JSON y muestra los datos en forma de tabla.
    Parameters
    ----------
    tipo : str
        Nombre del diccionario dentro del JSON.
    Returns
    -------
    str
        Datos solicitados en forma de tabla.
    """
    with open(ruta_gestion + 'gestion.json') as file:
        users = json.load(file)
    df_ver = json_normalize(users[tipo])
    return df_ver



########### GESTIÓN DE SALAS ############


def aforo_actual(sala):
    """Lee un archivo JSON y muestra el aforo de la sala indicada.
    Parameters
    ----------
    sala : str
        Sala de la que queremos saber el aforo.
    """
    with open(ruta_gestion + 'gestion.json') as file:
        salas = json.load(file)
    aforo_total = salas['Salas'][sala]['Aforo total']
    aforo_act = salas['Salas'][sala]['Aforo actual']
    st.write(f'El aforo disponible es {aforo_act}/{aforo_total}')

def nueva_sala(nombre_sala, aforo_total, aforo_restante, pelicula, trailer):
    """Lee un archivo JSON, comprueba que la sala no existe y la añade al JSON, lo sobreescribe.
    Parameters
    ----------
    nombre_sala : str
        Nombre y número de la sala.
    aforo_total : str
        Aforo total de la sala.
    aforo_restante : str
        Aforo que queda libre.
    pelicula : str
        Película que se va a proyectar.
    trailer : str
        URL del trailer de la película.
    """
    with open(ruta_gestion + 'gestion.json') as file:
        salas1 = json.load(file)
    lista_sala = []
    lista_pelicula = []
    for sala in salas1['Salas']:
        if nombre_sala in sala.values():
            lista_sala.append(True)
        else:
            lista_sala.append(False)
        if pelicula in sala.values():
            lista_pelicula.append(True)
        else:
            lista_pelicula.append(False)
    if (True in lista_sala):
        st.error('La sala ya existe, pruebe otra.')
    elif (True in lista_pelicula):
        st.error('La película ya está asignada a otra sala')
    else:
        try:
            salas1['Salas'].append({
                "Numero Sala": nombre_sala,
                "Aforo total": int(aforo_total),
                "Aforo actual": int(aforo_restante),
                "Pelicula": pelicula,
                "Trailer": trailer,
            })
            with open(ruta_gestion + 'gestion.json', 'w') as file:
                json.dump(salas1, file, indent=4)
            st.success('Sala añadida correctamente')
        except:
            st.error('Debes de introducir un número entero para los aforos.')


def eliminar_sala(posicion):
    """Abre y lee un archivo JSON y elimina la sala que se le pasa por parámetro.
    Parameters
    ----------
    posicion : int
        Posición del diccionario de Salas.
    """
    salas_json = json.loads(open(ruta_gestion + 'gestion.json').read())
    try:
        salas_json['Salas'].pop(posicion)
        json.dump(salas_json, open(ruta_gestion + 'gestion.json', 'w'), indent=4)
        st.success('La sala ha sido eliminada del sistema')
    except:
        st.error('La sala no está creada.')


def listar_espectadores():
    """Abre y lee un archivo JSON y muestra los datos en forma de tabla.
    Returns
    -------
    str
        Datos solicitados en forma de tabla.
    """
    with open(ruta_gestion + 'gestion.json') as file:
        espectadores = json.load(file)
        df = json_normalize(espectadores['Espectadores'])
        return df




########### COMPRA DE ENTRADAS ############


def actualizar_datos(usuario, nombre, apellidos, edad, sala, pelicula, fecha, hora):
    """Abre y lee un archivo CSV, y añade los datos de la compra. Además comprueba si queda aforo disponible y añade al
    espectador en el archivo JSON correspondiente.
    Parameters
    ----------
    usuario : str
        Nombre de usuario del comprador.
    nombre : str
        Nombre del espectador.
    apellidos : str
        Apellidos del espectador.
    edad : int
        Edad del espectador.
    sala : str
        Sala de proyección.
    pelicula : str
        Película que quiere ver.
    fecha : str
        Fecha de proyección.
    hora : str
        Hora de proyeccion.
    """
    with open(ruta_historial + 'historial_compras.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columnas_compras)
            writer.writerow({
            'User': usuario,
            'Nombre': nombre,
            'Apellidos': apellidos,
            'Edad': int(edad),
            'Sala': sala,
            'Pelicula': pelicula,
            'Fecha': fecha,
            'Hora': hora
            })
            csvfile.close()
    salas_json = json.loads(open(ruta_gestion + 'gestion.json').read())
    try:
        for i in salas_json['Salas']:
            if i['Numero Sala'] == sala:
                if i['Aforo actual'] > 0:
                    i['Aforo actual'] = i['Aforo actual'] - 1
                    break
                else:
                    st.warning(f'Lo sentimos, la {sala} está completa.')
            else:
                continue
        for i in salas_json['Espectadores']:
            if i['Numero Sala'] == sala:
                i['Espectadores'].append(nombre + ' ' + apellidos)
                json.dump(salas_json, open(ruta_gestion + 'gestion.json', 'w'), indent=4)
                time.sleep(1)
                st.warning('Accediendo a la pasarela de pago')
                time.sleep(1)
                st.warning('Realizando el pago')
                time.sleep(2)
                st.success('Pago realizado satisfactoriamente')
                time.sleep(0.5)
                st.write(f'{usuario}: has reservado una entrada para **{nombre} {apellidos}** en la **{sala}**, el **{fecha}** a las **{hora}**. ¡Esperemos que te guste **{pelicula}**!')
    except:
        st.error('Ha ocurrido un error, inténtelo de nuevo. Gracias.')

def comprobar_pelicula(sala):
    """Lee un archivo JSON y comprueba el nombre de la película para una sala determinada.
    Parameters
    ----------
    sala : str
        Sala que queremos comprobar
    Returns
    -------
    str
        Película de la sala comprobada.
    """
    salas_json = json.loads(open(ruta_gestion + 'gestion.json').read())
    for i in salas_json['Salas']:
        if sala == i['Numero Sala']:
            pelicula = i['Pelicula']
            return pelicula
        else:
            continue