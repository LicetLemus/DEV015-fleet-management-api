# Estructura del Proyecto

## `app/__init__.py`

Este archivo contiene la configuración inicial de la aplicación Flask. Aquí se crean las instancias como `SQLAlchemy`, se crea la coneccion con la base de datos y se registran las rutas. Es el punto de entrada para la inicialización de la aplicación.

## `app/config.py`

Define la configuración de la aplicación Flask, incluyendo la clave secreta, la URI de la base de datos PostgreSQL, y la clave secreta para JWT. La configuración se carga desde variables de entorno para mayor seguridad.

## `app/models.py`

Define los modelos de datos para la base de datos utilizando SQLAlchemy. Incluye los modelos `Taxi` y `Trajectory`, que representan los taxis y sus trayectorias en la base de datos, respectivamente.

## `app/routes.py`

Contiene las rutas y controladores de la API. Define las rutas para obtener la lista de taxis, las trayectorias asociadas a un taxi específico, y las trayectorias más recientes de cada taxi.

## `app/schemas.py`

Utiliza Marshmallow para definir los esquemas de serialización y deserialización de los modelos `Taxi` y `Trajectory`. Facilita la conversión de los modelos a formatos JSON para las respuestas de la API.

## `app/utils.py`

Incluye funciones utilitarias que pueden ser usadas en diferentes partes de la aplicación.

## `app/auth.py`

Gestiona la autenticación de usuarios mediante JWT. 

## `tests/test_taxis.py`

Contiene pruebas unitarias para el modelo `Taxi`.

## `requirements.txt`

Lista todas las dependencias necesarias para el proyecto, incluyendo Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-JWT-Extended y psycopg2. Se usa para instalar las librerías necesarias mediante `pip`.

## `run.py`

Es el archivo principal para ejecutar la aplicación Flask. Importa la función `create_app` del módulo `app` y ejecuta la aplicación en modo de depuración.

## `README.md`

Proporciona una visión general del proyecto, instrucciones de instalación, y detalles sobre los endpoints de la API. Incluye pasos para configurar el entorno, inicializar la base de datos, ejecutar la aplicación, y ejecutar las pruebas.