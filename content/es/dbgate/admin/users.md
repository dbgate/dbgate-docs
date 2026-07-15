---
sourceHash: e88bb0618f23a7bdce895dcef0093c2c2dbd7ad2ee16c003e961c2e51a419cab
language: es
title: Usuarios
weight: 30
---

## Pestaña Users
Configure los usuarios, las contraseñas, los permisos de usuario y la asignación usuario-conexión.
Las contraseñas se usan únicamente con los métodos de autenticación "Local". Sin embargo, todos los métodos con proveedores de identidad externos utilizan la búsqueda de usuarios, por lo que puede configurar los permisos y las conexiones disponibles para un usuario, incluso para un usuario autenticado externamente. 

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

### Pestañas de detalle del usuario
* Info
  * Configure los permisos del usuario
  * Configure los roles asignados a este usuario
* Team files - configure el acceso a los [archivos de equipo](team-files)
* Connections - configure las conexiones asignadas a este usuario
* Databases - configure los [permisos de base de datos](permissions#database-permissions) para este usuario
* Tables/views/objects - configure los [permisos de tabla](permissions#table-permissions) para este usuario
* Disk files - configure el acceso a los archivos en disco/volumen de Docker
