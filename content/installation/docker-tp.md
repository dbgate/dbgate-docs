---
title: Docker Team Premium
weight: 30
---

Typical Team Premium installation consists of two components: 
- DbGate server docker container
- Database server (MS SQL, MySQL, PostgreSQL, Oracle) - internal storage database for connections, users and roles

## DbGate Server Docker Container
User [DbGate Team Premium image](https://hub.docker.com/r/dbgate/dbgate-premium) from Docker Hub:
```
docker pull dbgate/dbgate-premium
```

DbGate Team Premium container requires some environment variables to be set:
- `STORAGE_SERVER`, `STORAGE_DATABASE`, `STORAGE_USER`, `STORAGE_PASSWORD`, `STORAGE_ENGINE` - defines connection to internal storage database

See [environment variables documentation](/env-variables/#team-premium-edition-configuration) for more details about available environment variables.

In fact, DbGate Team Premium has very low resource consumption, but for best performance we recommend following configuration (for 10 concurrent users):
- Minimum 2 CPU cores
- Minimum 2 GB RAM
- Minimum 10 GB free disk space

If you want to use disk files for storage of user files (like query results export), you should map `/root/.dbgate` path in container.

```yaml
    volumes:
      - dbgate-data:/root/.dbgate
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