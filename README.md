# Desarrollo del website de una biblioteca comunitaria

Vamos a realizar el sitio web de la biblioteca comunitaria de la fundación CUYECA, Para ello, nos apoyaremos en el tutorial disponible en la documentación de Mozilla, que nos ayudará a vencer el temor a leer documentación y resolver el problema que se nos presenta.

## Instalación

Asegúrate de tener Python y Django instalados en tu máquina.

1. Clona este repositorio: `git clone https://github.com/fabert111/djjango-startproject-locallibrary.git`
2. Ve al directorio del proyecto: `cd tu_proyecto`
3. Crea y activa un entorno virtual (opcional): `python -m venv env` y `source env/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Ejecuta las migraciones de la base de datos: `python manage.py migrate`

## Configuración

1. Crea un archivo `.env` en el directorio raíz del proyecto y define las variables de entorno necesarias. Puedes utilizar el archivo `.env.example` como referencia.
2. Configura la base de datos en el archivo `settings.py`.
3. Personaliza cualquier otra configuración específica en el archivo `settings.py` según sea necesario.

## Uso

Ejecuta el servidor de desarrollo de Django: Cómo desarrollo web de una aplicación de libros, escoger la base de datos y realizar el backend de la aplicación.

Este backend nos servira para en próximas entregas realizar el frontend de la web y así tener un desarrollo robusto para nuestro portafolio.

```bash

# Reduerda tener el entorno activado a momemnto de correr el sevidor
python manage.py runserver


