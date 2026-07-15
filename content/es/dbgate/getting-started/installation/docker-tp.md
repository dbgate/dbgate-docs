---
sourceHash: 1565401b5cbe564d5dea5c98e8e060786cb30e1952808c41e0a5542a29f3ef42
language: es
title: Team Premium en Docker
weight: 30
---

Una instalación típica de Team Premium consta de dos componentes: 
- Contenedor Docker del servidor DbGate
- Servidor de base de datos (MS SQL, MySQL, PostgreSQL, Oracle) - base de datos de almacenamiento interno para conexiones, usuarios y roles. Puede utilizar un servidor de base de datos existente o instalar uno nuevo.

## Contenedor Docker del servidor DbGate
Utilice la [imagen de DbGate Team Premium](https://hub.docker.com/r/dbgate/dbgate-premium) de Docker Hub:
```
docker pull dbgate/dbgate-premium
```

El contenedor de DbGate Team Premium requiere que se configuren algunas variables de entorno:
- `STORAGE_SERVER`, `STORAGE_DATABASE`, `STORAGE_USER`, `STORAGE_PASSWORD`, `STORAGE_ENGINE` - definen la conexión a la base de datos de almacenamiento interno

Consulte la [documentación de variables de entorno](/es/dbgate/customization/env-variables/#team-premium-edition-configuration) para obtener más detalles sobre las variables de entorno disponibles.

## Requisitos de recursos

De hecho, DbGate Team Premium tiene un consumo de recursos muy bajo, pero para obtener el mejor rendimiento recomendamos la siguiente configuración (para 10 usuarios concurrentes):
- 2 núcleos de CPU
- 4 GB de RAM (incluye el consumo de RAM de la base de datos de almacenamiento interno MySQL o PostgreSQL)
- 10 GB de espacio libre en disco (para la instalación de Docker, la base de datos de almacenamiento, los archivos temporales, los resultados de consultas, etc. El consumo real de espacio en disco depende de los patrones de uso)

Para un número menor de usuarios, puede utilizar límites de recursos más bajos (1 GB de RAM, 1 núcleo de CPU).  
Cuando necesite minimizar el consumo de recursos en instalaciones pequeñas, recomendamos utilizar MySQL/MariaDB como almacenamiento interno.  

## Configuración de Docker

Si desea utilizar archivos en disco para almacenar los archivos de usuario (como la exportación de resultados de consultas), debe mapear la ruta `/root/.dbgate` en el contenedor.

A continuación se muestra un ejemplo de archivo `docker-compose.yml`, que define el contenedor de DbGate Team Premium con PostgreSQL como base de datos de almacenamiento interno.
- Puede definir la variable de entorno `DBGATE_LICENSE` para establecer la clave de licencia. Si no se define, DbGate solicitará la clave de licencia en el primer inicio.
-  Puede definir la variable de entorno 'ADMIN_PASSWORD' para establecer la contraseña del usuario administrador. Si no se define, DbGate solicitará la contraseña de administrador en el primer inicio.

```yaml
version: '3'
services:
  dbgate:
    image: dbgate/dbgate-premium
    restart: always
    ports:
      - 80:3000
    environment:
      STORAGE_SERVER: postgres_service
      STORAGE_USER: postgres
      STORAGE_PASSWORD: XXXStoragePwd
      STORAGE_PORT: 5432
      STORAGE_DATABASE: dbgate
      STORAGE_ENGINE: postgres@dbgate-plugin-postgres
      STORAGE_SCHEMA: public
    volumes:
      - dbgate_data:/root/.dbgate

  postgres_service:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: XXXStoragePwd
      POSTGRES_DB: dbgate
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
    postgres_data:
      driver: local
    dbgate_data:
      driver: local
```

## Sin estado / Con estado
El contenedor de DbGate tiene estado. 

Los siguientes datos se almacenan dentro del contenedor:
* Sesiones de usuarios conectados
* Estados de ejecución de consultas
* Archivos temporales (como los resultados)
* Transacciones de base de datos abiertas
* Conexiones de base de datos abiertas

No es posible ejecutar correctamente varios contenedores de DbGate detrás de un balanceador de carga, porque los datos anteriores no se comparten entre contenedores.

## Servidor DbGate desde NPM
Si su infraestructura no admite Docker, puede utilizar el [paquete NPM de DbGate Team Premium](https://www.npmjs.com/package/dbgate-serve-premium):
```
npm install -g dbgate-serve-premium
```
 
## Aislamiento de procesos
DbGate Team Premium utiliza aislamiento de procesos a nivel de conexión de base de datos, de modo que varios usuarios pueden utilizar el mismo servidor de base de datos sin interferencias. El proceso bifurcado desde DbGate crece con el número de usuarios y conexiones activas, así que asegúrese de que su servidor tenga suficientes recursos.
Las siguientes entidades se aíslan en un nuevo proceso:
* Conexiones de servidor
* Conexiones de base de datos
* Sesiones de consultas
* Ejecución de trabajos de exportación/importación
* Túneles SSH
