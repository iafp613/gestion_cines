# ------------------------------------------------------- IMPORTACIÓN ---------------------------------------------------------------
import streamlit as st
from streamlit_player import st_player
import os
import datetime
import sys
import json
import seaborn as sns
from PIL import Image

# ---------------------------------------------------------- VARIABLES --------------------------------------------------------------------
SEP = os.sep

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + SEP + 'resources')
ruta_imagenes = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + SEP + 'resources' + SEP + 'img' + SEP
ruta_admin = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + SEP + 'resources' + SEP + 'data' + SEP + 'users' + SEP
ruta_sala = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + SEP + 'resources' + SEP + 'data' + SEP + 'users' + SEP
import utils.app as app


# Carga de imágenes
logo = Image.open(ruta_imagenes + 'cines_ciber.jpg')
spiderman = Image.open(ruta_imagenes + 'Spiderman_NWH.jpg')
abuela = Image.open(ruta_imagenes + 'La_abuela.jpg')
nilo = Image.open(ruta_imagenes + 'muerte_nilo.jpg')
moonfall = Image.open(ruta_imagenes + 'Moonfall.jpg')
uncharted = Image.open(ruta_imagenes + 'uncharted.jpg')
reserva = Image.open(ruta_imagenes + 'reserva.jpeg')
adios = Image.open(ruta_imagenes + 'despedida.jpg')
icono = Image.open(ruta_imagenes + 'icono.jpg')
registrate = Image.open(ruta_imagenes + 'registro.jpg')

# Configuración de la página
st.set_page_config(
    page_title="Cines Ciber",
    page_icon=icono,
    layout="wide"
)

# Menu desplegable
menu = st.sidebar.selectbox('Menu:',
            options=["Home", "Cartelera", "Comprar entradas", "Regístrate", "Area Administrador", "Salir"]) # Opciones del menu



# -------------------------------------------------------------- HOME ----------------------------------------------------------------------
if menu == 'Home':
    st.image(logo, width=400) # Cargamos la imagen
    st.sidebar.markdown('### Hola, Bienvenido/a a *Cines Ciber*') # Sidebar
    st.sidebar.markdown('Actividad grupal 1. **The Bridge**. Realizado el *25 de Febrero del 2022*') # Sidebar
    st.sidebar.markdown('Ciberseguridad') # Sidebar
    for i in range(15): st.sidebar.write("") # Espacios en blanco
    st.sidebar.markdown('#### Hecho por: ') # Sidebar
    st.sidebar.markdown('##### Alberto Cano, Fernando Zurita y Nacho Fontal') # Sidebar
    st.markdown("# Cines Ciber") # Título
    st.markdown("### Salas de ocio 3.0") # Subtítulo
    st.markdown('Cines Ciber nació hace casi 42 años para proporcionar una forma de ocio diferente a la de la época.\
        La idea surgió de la cabeza de tres jóvenes entusiastas de la tecnología, estudiantes de la presitigiosa escuela \
        internacional The Bridge. Ellos querían llevar los avances tecnológicos más punteros a las salas de cine. Así, un \
        4 de Marzo de 1980, nació **Cines Ciber**. Con una pequeña sala en la periferia de la ciudad de Madrid, y con solo una \
        película en proyección (Star Wars V: El Imperio contraataca), ésta ofrecía una verdadera experiencia inmersiva. \
        Con sus butacas móviles, cañones de frío y calor, control de la humedad y del aire, la IA programada proporcionaba al \
        cliente unas sensaciones acordes con la película muy realistas.')
    st.write('Hoy, a punto de cumplir nuestro XLII aniversario, contamos con más de 50 cines en toda Europa, más de 300 salas con \
        un catálogo actualizado y la tecnología más puntera, como las **proyecciones holográficas** y las experiencias en **Realidad \
        Aumentada** donde tú puedes ser el protagonista de la película. *¡Bienvenido/a al cine 3.0! ¡Bienvenido/a a Cines Ciber!*')



# --------------------------------------------------------- CARTELERA ----------------------------------------------------------------------
if menu == 'Cartelera':
    st.sidebar.markdown('### Hola, Bienvenido/a a *Cines Ciber*') # Sidebar
    st.sidebar.markdown('Actividad grupal 1. **The Bridge**. Realizado el *25 de Febrero del 2022*') # Sidebar
    st.sidebar.markdown('Ciberseguridad') # Sidebar
    for i in range(15): st.sidebar.write("") # Espacios en blanco
    st.sidebar.markdown('#### Hecho por:') # Sidebar
    st.sidebar.markdown('##### Alberto Cano, Fernando Zurita y Nacho Fontal') # Sidebar
    st.markdown('# Cartelera') # Título
    st.markdown('## Cines Ciber Callao') # Subtítulo
    col1, col2 = st.columns(2) # Dividimos la pantalla en dos columnas
    with col1: # Contenido de la columna 1
        st.markdown('**Sala 1**: Uncharted') # Nombre sala / película
        st.image(uncharted, width=200) # Imagen de la película y tamaño
        app.aforo_actual(0) # Llamamos a la función aforo_actual()
        st.write('') # Espacio en blanco
        st.markdown('**Sala 2**: Muerte en el Nilo') # Nombre sala / película
        st.image(nilo, width=240) # Imagen de la película y tamaño
        app.aforo_actual(1) # Llamamos a la función aforo_actual()
        st.write('') # Espacio en blanco
        st.markdown('**Sala 3**: Moonfall') # Nombre sala / película
        st.image(moonfall, width=210) # Imagen de la película y tamaño
        app.aforo_actual(2) # Llamamos a la función aforo_actual()
        st.write('') # Espacio en blanco
        st.markdown('**Sala 4**: Spider-Man: No Way Home') # Nombre sala / película
        st.image(spiderman, width=200) # Imagen de la película y tamaño
        app.aforo_actual(3) # Llamamos a la función aforo_actual()
        st.write('') # Espacio en blanco
        st.markdown('**Sala 5**: La Abuela') # Nombre sala / película
        st.image(abuela, width=200) # Imagen de la película y tamaño
        app.aforo_actual(4) # Llamamos a la función aforo_actual()

    with col2: # Contenido de la columna 2
        st.write('') # Espacio en blanco
        st_player('https://www.youtube.com/watch?v=v6uwWIK3p4g') # Cargamos el video del tráiler
        st.write('')
        st.write('')
        st_player("https://www.youtube.com/watch?v=2HQPNRtMbJ0")
        st.write('')
        st.write('')
        st_player('https://www.youtube.com/watch?v=5ZvH_pIq1Oc')
        st.write('')
        st.write('')
        st_player('https://www.youtube.com/watch?v=ldMn-1iQzKE')
        st.write('')
        st.write('')
        st_player('https://www.youtube.com/watch?v=JhCWvpZbw9k')



# ------------------------------------------------------------ REGISTRO --------------------------------------------------------------------
if menu == 'Regístrate':
    st.sidebar.markdown('### Hola, Bienvenido/a a *Cines Ciber*')
    st.sidebar.markdown('Actividad grupal 1. **The Bridge**. Realizado el *25 de Febrero del 2022*')
    st.sidebar.markdown('Ciberseguridad')
    for i in range(15): st.sidebar.write("")
    st.sidebar.markdown('#### Hecho por:')
    st.sidebar.markdown('##### Alberto Cano, Fernando Zurita y Nacho Fontal')
    st.markdown('# ¡Regístrate con nosotros!')
    st.image(registrate, width=500)
    st.markdown('### Aprovecha nuestras ofertas exclusivas para socios.')
    st.latex(r'''\textcolor{#228B22}{\text{Registro}}''')
    with st.form(key='Registro', clear_on_submit=True):
        usuario = st.text_input('Nombre de usuario')
        nombre = st.text_input('Nombre: ')
        apellidos = st.text_input('Apellidos: ')
        edad = st.text_input('Edad: ')
        dni = st.text_input('DNI: ')
        contraseña = st.text_input('Contraseña: ', type='password')
        registro = st.form_submit_button('¡Regístrate!')
        if registro == True:
            app.nuevo_usuario(usuario, nombre, apellidos, edad, dni, contraseña)



# ----------------------------------------------------------- ADMINISTRADOR -----------------------------------------------------------------
if menu == 'Area Administrador':
    with open(ruta_admin + 'admin.json') as file:
        administrador = json.load(file)
    st.sidebar.markdown('### Hola, Bienvenido/a a *Cines Ciber*')
    st.sidebar.markdown('Actividad grupal 1. **The Bridge**. Realizado el *25 de Febrero del 2022*')
    st.sidebar.markdown('Ciberseguridad')
    st.markdown('# Gestión de salas')
    st.markdown('### Gestiona las Salas como Administrador')
    st.subheader('Area administrador')
    for i in range(1): st.sidebar.write("")

    superuser = st.sidebar.text_input('Usuario: ')
    password = st.sidebar.text_input('Contraseña: ', type='password')

    if st.sidebar.checkbox('Login'):
        if (superuser != administrador["superuser"]) and (password != administrador['password']):
            st.sidebar.error('Usuario y/o contraseña incorrectos. Inténtelo de nuevo')
        else:
            st.success('Bienvenido de nuevo, {}'.format(superuser))
            opciones = st.selectbox('¿Qué deseas hacer?',[' ', 'Administrar Salas', 'Ver clientes', 'Histórico', 'Estadísticas'])

            if opciones == 'Administrar Salas':
                st.latex(r'''\textcolor{#228B22}{\text{Administrar Salas}}''')
                opciones1 = st.selectbox('Elige una opción', options=[' ', 'Ver Salas', 'Añadir Sala', 'Eliminar Sala'])

                if opciones1 == 'Ver Salas':
                    st.latex(r'''\textcolor{#228B22}{\text{Ver Sala}}''')
                    st.table(app.ver('Salas'))
                    st.latex(r'''\textcolor{#228B22}{\text{Ver Espectadores}}''')
                    st.table(app.listar_espectadores())

                elif opciones1 == 'Añadir Sala':
                    st.latex(r'''\textcolor{#228B22}{\text{Añadir Sala}}''')
                    with st.form(key='Registro', clear_on_submit=True):
                        nombre_sala = st.text_input('Nombre de la sala: ')
                        aforo_total = st.text_input('Aforo total de la sala: ')
                        aforo_restante = st.text_input('Aforo disponible: ')
                        pelicula = st.text_input('Nombre de la película: ')
                        trailer = st.text_input('URL Tráiler: ')
                        registro = st.form_submit_button('Añadir')
                        if registro == True:
                            app.nueva_sala(nombre_sala, aforo_total, aforo_restante, pelicula, trailer)

                elif opciones1 == 'Eliminar Sala':
                    st.latex(r'''\textcolor{#228B22}{\text{Eliminar Sala}}''')
                    with st.form('Eliminar sala', clear_on_submit=True):
                        sala_eliminar = st.text_input('¿Qué sala quieres eliminar?')
                        aplicar = st.form_submit_button('Borrar')
                        if (sala_eliminar == 'Sala 1') and (aplicar == True):
                            app.eliminar_sala(0)
                        elif (sala_eliminar == 'Sala 2') and (aplicar == True):
                            app.eliminar_sala(1)
                        elif (sala_eliminar == 'Sala 3') and (aplicar == True):
                            app.eliminar_sala(2)
                        elif (sala_eliminar == 'Sala 4') and (aplicar == True):
                            app.eliminar_sala(3)
                        elif (sala_eliminar == 'Sala 5') and (aplicar == True):
                            app.eliminar_sala(4)
                        elif (sala_eliminar == 'Sala 6') and (aplicar == True):
                            app.eliminar_sala(5)
                        elif (sala_eliminar == 'Sala 7') and (aplicar == True):
                            app.eliminar_sala(6)

            elif opciones == 'Ver clientes':
                st.latex(r'''\textcolor{#228B22}{\text{Ver clientes}}''')
                st.table(app.ver('Clientes'))
                st.latex(r'''\textcolor{#228B22}{\text{Ver espectadores}}''')
                st.table(app.listar_espectadores())

            elif opciones == 'Histórico':
                st.latex(r'''\textcolor{#228B22}{\text{Histórico}}''')
                opciones2 = st.selectbox('Elige una opción', options=[' ', 'Ver histórico de compras', 'Ver histórico de registros'])
                if opciones2 == 'Ver histórico de compras':
                    st.table(app.ver_historial('historial_compras.csv'))
                elif opciones2 == 'Ver histórico de registros':
                    registros = app.ver_historial('historial_registros.csv')
                    st.table(registros)
                    # Crear una gráfica de caja para las edades.
                    st.set_option('deprecation.showPyplotGlobalUse', False)
                    sns.set_theme(style='darkgrid')
                    g = sns.catplot(y="Edad", kind='box', data=registros, color='red')
                    g.fig.subplots_adjust(top=0.9)
                    g.fig.suptitle('Edades de los clientes')
                    st.pyplot()



            elif opciones == 'Estadísticas':
                st.latex(r'''\textcolor{#228B22}{\text{Estadísticas}}''')
                app.ver_porcentajes()



# ---------------------------------------------------------- VENTA ENTRADAS ----------------------------------------------------------------
if menu == 'Comprar entradas':
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperatura", "12 °C", "1.2 °C")
    col2.metric("Viento", "9 Km/h", "-8%")
    col3.metric("Humedad", "66%", "4%")
    st.sidebar.markdown('### Hola, Bienvenido/a a *Cines Ciber*')
    st.sidebar.markdown('Actividad grupal 1. **The Bridge**. Realizado el *25 de Febrero del 2022*')
    st.sidebar.markdown('Ciberseguridad')
    for i in range(15): st.sidebar.write("")
    st.sidebar.markdown('#### Hecho por:')
    st.sidebar.markdown('##### Alberto Cano, Fernando Zurita y Nacho Fontal')
    st.markdown('## ¡Compra tus entradas!')
    st.image(reserva, width=500)
    st.latex(r'''\textcolor{#228B22}{\text{Inicia sesión}}''')
    usuario = st.text_input('Usuario: ', help='Nombre de usuario')
    password = st.text_input('Contraseña: ', type='password', help='Contraseña')
    if st.checkbox('Login'):
        if True in app.login_user(usuario, password):
            st.success('Hola de nuevo, {}'.format(usuario))
            st.latex(r'''\textcolor{#228B22}{\text{Comprar entradas}}''')
            with st.form('Comprar entradas', clear_on_submit=False):
                usuario = usuario
                nombre = st.text_input('Nombre: ')
                apellidos = st.text_input('Apellidos: ')
                edad = st.text_input('Edad: ')
                sala = st.selectbox('Elige una opción', options=[' ', 'Sala 1', 'Sala 2', 'Sala 3', 'Sala 4', 'Sala 5'])
                pelicula = app.comprobar_pelicula(sala)
                fecha = st.date_input('Selecciona una fecha: ')
                hora = st.time_input('Selecciona una hora: ', datetime.time(21, 0))
                aplicar = st.form_submit_button('Comprar')
                if aplicar == True:
                    app.actualizar_datos(usuario, nombre, apellidos, edad, sala, pelicula, fecha, hora)
        else:
            st.error('El usuario y/o la contraseña son incorrectos. Inténtalo de nuevo o **Regístrate**.')



# -------------------------------------------------------------- SALIR ---------------------------------------------------------------------
if menu == 'Salir':
    st.sidebar.markdown('### Hola, Bienvenido/a a *Cines Ciber*')
    st.sidebar.markdown('Actividad grupal 1. **The Bridge**. Realizado el *25 de Febrero del 2022*')
    st.sidebar.markdown('Ciberseguridad')
    for i in range(15): st.sidebar.write("")
    st.sidebar.markdown('#### Hecho por:')
    st.sidebar.markdown('##### Alberto Cano, Fernando Zurita y Nacho Fontal')
    st.markdown('## ¡Hasta pronto!')
    st.image(adios)