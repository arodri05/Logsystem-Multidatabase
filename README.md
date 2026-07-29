# Logmon: Sistema de Logs Multi Base de Datos

Logmon es una plataforma de monitoreo diseñada para registrar, almacenar y centralizar eventos (logs) de múltiples aplicaciones, con la capacidad de cambiar dinámicamente el motor de almacenamiento en tiempo real sin interrupción del servicio ni pérdida de datos.

El proyecto utiliza una arquitectura desacoplada: un backend en **FastAPI** que gestiona el enrutamiento y las conexiones, y un frontend en **React** para la administración y visualización del historial.

## Características
* **Almacenamiento Dinámico:** Cambio de motor de base de datos en caliente mediante un sistema de Adapters.
* **Compatibilidad Multi-Motor:** Soporte integrado para MariaDB, PostgreSQL, SQL Server, MongoDB y Redis.
* **Gestión de Fuentes:** API REST y Dashboard para dar de alta aplicaciones externas y probar conexiones.
* **Persistencia de Metadata:** Centralización de configuraciones e historial de cambios en SQLite.
* **Consultas Avanzadas:** Filtrado y auditoría global de logs desde una interfaz unificada.

## Arquitectura y Stack Tecnológico

* **Backend:** Python 3.12, FastAPI, Uvicorn, SQLAlchemy, Pydantic.
* **Frontend:** React, TypeScript, Vite.
* **Infraestructura:** Docker y Docker Compose para el despliegue local de los motores.

```text
logmon/
├── backend/          # API REST y lógica de persistencia
├── frontend/         # Dashboard de administración
├── docker-compose.yml # Contenedores de bases de datos
├── Makefile          # Atajos de comandos (seed, tests)
└── .env.example      # Plantilla de configuración
```

## Requisitos Previos
* Docker Desktop / Docker Compose
* Python 3.12 (opcional para desarrollo local)
* Git

## Instalación y Despliegue

1. Clonar el repositorio y acceder al directorio:
   ```bash
   git clone URL_DEL_REPOSITORIO
   cd logmon
   ```

2. Configurar el entorno:
   ```bash
   cp .env.example .env
   ```
   *(Ajustar las credenciales en el archivo `.env` si es necesario).*

3. Levantar la infraestructura en segundo plano:
   ```bash
   docker compose up -d
   ```

4. Generar registros de prueba iniciales:
   ```bash
   make seed
   ```

## Flujo de Trabajo e Integración

1. Una aplicación cliente envía un evento a la API.
2. El Router del backend intercepta la solicitud y valida la fuente de origen.
3. El Adapter activo procesa y escribe el registro en el motor seleccionado.
4. Los cambios de motor se reflejan inmediatamente en el Dashboard sin requerir reinicios.

## Endpoints Principales (API)

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `POST` | `/api/logs` | Registrar un nuevo evento de log |
| `GET` | `/api/logs` | Listado y filtrado de logs históricos |
| `GET` | `/api/logs/{id}` | Obtener el detalle específico de un log |
| `POST` | `/api/sources/{id}/switch` | Cambiar el motor de almacenamiento asignado |
| `POST` | `/api/connections/{id}/test` | Validar estado y ping de una base de datos |
| `POST` | `/api/logs/demo` | Ingesta masiva de datos dummy para pruebas |

## Pruebas de Sistema
El repositorio incluye una suite de pruebas automatizadas enfocadas en validar:
* El comportamiento individual de cada Adapter de base de datos.
* La consistencia de datos durante operaciones de conmutación de motor (*failover/switch*).
* Resistencia a escrituras concurrentes de alta carga.

## Licencia
Este proyecto se distribuye bajo la **Licencia MIT**. Consulta el archivo `LICENSE` para ver los términos completos.

Copyright (c) 2026 Federico Gis





