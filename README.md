# Fleet Management Software API

## Índice

* [1. Introducción](#1-introducción)
* [2. Tecnologías](#2-tecnologías)
* [3. Uso](#3-uso)
* [4. Autorización](#4-autorización)
* [5. Manejo de errores](#5-manejo-de-errores)

***

## 1. Introducción

Esta API REST permite gestionar los datos de una flota de taxis, proporcionando funcionalidades como la carga masiva de datos históricos de GPS, consulta de ubicaciones en tiempo real y administración de usuarios. También ofrece autenticación segura mediante JWT para proteger todos los endpoints.

## 2. Tecnologías

- **Python**: Lenguaje de programación utilizado.
- **Flask**: Framework para el desarrollo de la API.
- **SQLAlchemy**: ORM para gestionar la base de datos.
- **Flask-JWT-Extended**: Manejo de autenticación y autorización con tokens JWT.
- **PostgreSQL**: Base de datos utilizada para almacenar los datos de los taxis y usuarios.

## 3. Uso

A continuación se describen los principales endpoints disponibles:

- **GET /taxis**: Obtiene el listado de taxis. Soporta los parámetros `plate`, `page` y `limit`. Ejemplo: `/taxis?limit=3&page=2`
- **GET /trajectories**: Obtiene el listado de trayectorias, teniendo en cuenta el parámetro `taxiId` y `date`. Ejemplo: `/trajectories?taxiId=6418&date=02-02-2008`
- **GET /trajectories/latest**: Obtiene la última trayectoria de cada taxi. Ejemplo: `trajectories/latest`
- **POST /users**: Crea nuevos usuarios
`{
  "name": "user2",
  "email": "admin2@test.com",
  "password": "test2"
} `
- **GET /users**: Obtiene el listado de usuarios. Soporta los parámetros `page` y `limit`
- **PATCH /users/<id>**: Actualiza la información de un usuario basado en el ID
`{
  "name": "Grace Hopper update"
}`
- **DELETE /users/<id>**: Elimina un usuario

## 4. Autorización

Para acceder a los endpoints protegidos, se requiere un token JWT. El token debe incluirse en el encabezado de las solicitudes con el formato `Authorization: Bearer <token>`

## 5. Manejo de errores

- **401 Unauthorized**: El token JWT es inválido o no está presente en el encabezado de la solicitud.
- **404 Not Found**: El recurso solicitado no se encuentra. Se debe verificar que el endpoint y los parámetros sean correctos.
- **400 Bad Request**:  La solicitud tiene errores. Es necesario verificar que todos los parámetros y datos sean correctos.
- **500 Internal Server Error**: Error en el servidor.

Gracias por visitar este proyecto. Se espera que la API sea útil y que quienes trabajen con ella disfruten del proceso
