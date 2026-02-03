---
title: Team Premium on Docker
weight: 30
---

Typical Team Premium installation consists of two components: 
- DbGate server docker container
- Database server (MS SQL, MySQL, PostgreSQL, Oracle) - internal storage database for connections, users and roles. You could use existing database server or install new one.

## DbGate Server Docker Container
User [DbGate Team Premium image](https://hub.docker.com/r/dbgate/dbgate-premium) from Docker Hub:
```
docker pull dbgate/dbgate-premium
```

DbGate Team Premium container requires some environment variables to be set:
- `STORAGE_SERVER`, `STORAGE_DATABASE`, `STORAGE_USER`, `STORAGE_PASSWORD`, `STORAGE_ENGINE` - defines connection to internal storage database

See [environment variables documentation](/env-variables/#team-premium-edition-configuration) for more details about available environment variables.

## Resource Requirements

In fact, DbGate Team Premium has very low resource consumption, but for best performance we recommend following configuration (for 10 concurrent users):
- 2 CPU cores
- 4 GB RAM
- 10 GB free disk space (for temporary files, query results, etc. Actual disk space consumption depends on usage patterns)

For single-user installations, you could use much lower resource limits (1 GB RAM, 1 CPU core).

## Configuring docker

If you want to use disk files for storage of user files (like query results export), you should map `/root/.dbgate` path in container.

Below is example `docker-compose.yml` file, definiting DbGate Team Premium container with PostgreSQL as internal storage database.
- You could define `DBGATE_LICENSE` environment variable to set license key. If not set, DbGate will ask for license key on first start.
-  You could define 'ADMIN_PASSWORD' environment variable to set admin user password. If not set, DbGate will ask for admin password on first start.

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

## Stateless/Statefullness
DbGate container is statefull. 

The following data is stored inside container:
* Logged user sessions
* Query execution states
* Temporary files (like results)
* Opened database transactions
* Opened database connections

It is not possible to run correctly multiple DbGate containers behind load balancer, because the data above is not shared between containers.

## DbGate Server from NPM
If your infrastructure does not support Docker, you could use [DbGate Team Premium NPM package](https://www.npmjs.com/package/dbgate-serve-premium):
```
npm install -g dbgate-serve-premium
```
 
## Process isolation
DbGate Team Premium uses process isolation on database connection level, so multiple users could use same database server without interference. Process forked from DbGate grows with number of active users and connections, so make sure your server has enough resources.
Following entities are isolated into new process:
* Server connections
* Database connections
* Query sessions
* Export/import job execution
* SSH tunneling