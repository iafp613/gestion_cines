<h1 align="center"> Gestión de Cines - Proyecto individual con Streamlit.</h1>
<p align="center"><img src="https://www.rioja2.com/images/noticias/56575/recortes/12x5-sala-de-cine.jpg"/></p>

_Este repositorio muestra, de una forma sencilla, un ejemplo de una aplicación de gestión de cines._

_Aunque no se podría poner en producción, ya que falta darle algunos retoques, añadirle funcionalidades y seguridad; se ha realizado con el objetivo de mostrar todo lo que Streamlit es capaz de hacer con pocas líneas de código y solamente usando Python._

_Este proyecto ha sido realizado en unas 32 horas_

_Las funcionalidades de esta aplicación son:_

- *Mostrar las salas, películas, tráiler y aforo disponible.*
- *Registrarte en la aplicación como cliente.*
- *Comprar entradas para el propio usuario o para otras personas.*
- *Iniciar sesión como superusuario.*
- *El superusuario podrá ver un historial de registros y compras, así como los aforos y los asistentes a una sala.*
- *Añadir o eliminar salas.*

_¡Espero que te guste!_ 😊

![GitHub watchers](https://img.shields.io/github/watchers/iafp613/gestion_cines?style=social)


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo, pruebas o visualización._

Dentro de la carpeta `src` están contenidos todos los archivos ejecutables. El archivo principal es `main`, que se encuentra en `src > app > main.py`. Al ejecutar este archivo se iniciará Streamlit.

Dentro de `utils`, tenemos el archivo `app.py` el cual contiene la lógica para ejecutar la aplicación `main.py`.

En la carpeta `resources` encontramos dos carpetas: `data` y `img`.

En la carpeta `data`, a su vez, tenemos la carpeta `historial` que almacena dos archivos .csv (`historial_compras.csv` e `historial_registros.csv`). En el primero tenemos un histórico de todas las compras que se han realizado en la app y en el segundo, un historial de altas en la aplicación con fecha y hora. Además, tenemos la carpeta `users` donde se almacenan los datos de los clientes, (incluídas sus contraseñas), los aforos y las salas habilitadas. Este archivo, `gestion.json`, y `admin.json` (clave del superusuario), deberían de estar ocultos o alojados en la nube (aquí se muestran a modo didáctico y porque TODOS los datos son ficticios).

En la carpeta `img` tenemos todas las imágenes que se muestran en la aplicación.


### Pre-requisitos 📋

_Para poder ejecutar el código entero, necesitarás tener instaladas una serie de librerías (así como Python v.3.7.4). Todas las librerías que se han usado son:_

```
os
sys
pandas
pyplot
csv
json
streamlit
time
cryptography
Markdown
Pillow
streamlit-player

```
Puedes encontrar el listado en `requirements.txt`.


### Instalación 🔧

**Recuerda:**

*En la terminal del sistema operativo:*

```
pip3 install pandas
```

```
pip3 install streamlit
```
*Etc.*

Pero si necesitas hacerlo de forma global, abre la terminal de Windows (en caso de tener Windows OS), dirígete a la carpeta donde esté este proyecto descargado y ejecuta el siguiente comando:

```
pip install -r requirements.txt
```


## Construido con 🛠️

* [VSC](https://code.visualstudio.com/download) - Editor de código
* [Streamlit](https://streamlit.io/) - Librería de Aplicaciones y dashboards


![Your Repository's Stats](https://github-readme-stats.vercel.app/api/top-langs/?username=iafp613&theme=blue-green)


## Contribuyendo 🖇️

*Por favor, déjame una estrella en mi perfil y/o hazme un follow, ayudas a seguir subiendo más contenido.* 😊

![GitHub followers](https://img.shields.io/github/followers/iafp613?style=social)
![GitHub User's stars](https://img.shields.io/github/stars/iafp613?style=social)
![GitHub forks](https://img.shields.io/github/forks/iafp613/gestion_cines?style=social)



## Autor ✒️

* **Nacho Fontal** - *Proyecto* - [![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/iafp/)


## Licencia 📄

Este proyecto está bajo la Licencia MIT (mira el archivo [LICENSE.md](LICENSE.md) para detalles).


## Expresiones de Gratitud 🎁

Muchísimas gracias a YouTube, por ser una fuente inagotable de conocimientos.

Y muchísimas gracias a Streamlit, por ser de código abierto, tener una documentación tan sencilla y poder hacer estas maravillas. 😊
---