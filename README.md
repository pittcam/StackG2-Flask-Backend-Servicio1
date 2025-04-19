# 🎬 MovieNest - Vue + Flask + PostgreSQL + GraphQL

¡Bienvenido a **MovieNest**!  
Este proyecto es una aplicación web para la gestión de películas favoritas con listas.

## 🚀 Requisitos Previos

- Docker y Docker Compose
- Configuración ambiente de PostgreSQL Local
- Conexión a internet activa
---

## ⚙️ Configuración Inicial

Antes de levantar el proyecto, es necesario realizar algunos ajustes en la configuración del entorno y base de datos:

### 📄 1. Variables de Entorno

Editá el archivo `.env` y el docker-compose del contenedor del servicio 2 con los siguientes datos:

env
- POSTGRES_DB=MovieNest
- POSTGRES_USER=tu usuario #cambiar el usuario o mantener
- POSTGRES_PASSWORD=tu contraseña #cambiar la contraseña
- POSTGRES_HOST=host.docker.internal
- POSTGRES_PORT=5433

### 📄 2. Para ejecutar el contenedor general

Correr el siguiente comando en la raíz de la carpeta MovieNest-App:
docker-compose up --build

Si quiere detenerse se usa el comando: docker-compose down
