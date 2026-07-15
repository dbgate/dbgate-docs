---
sourceHash: f3fc7804108ada6b6dc15e241b9e3e162447625c947827b4c1d1f453d871652e
language: es
title: Roles
weight: 40
---

## Pestaña Roles
Configure los roles, los permisos de los roles y la asignación entre roles y conexiones. Puede crear roles personalizados y asignarles usuarios, de modo que los permisos y las conexiones vinculadas se compartan entre todos los usuarios asignados a ese rol.

Existen algunos roles predefinidos:
- superadmin - rol utilizado para la página de administración, https://your_dbgate_instance/admin.html
- logged-user - rol utilizado para todos los usuarios que han iniciado sesión. Puede sobrescribir los permisos para usuarios concretos
- anonymous-user - rol utilizado para los usuarios que inician sesión con el método de autenticación "Anonymous"

![Role administration - DbGate](https://media.dbgate.io/img/role-administration-light.png)

### Pestañas de detalle del rol
* Info
  * Configurar los permisos del rol
  * Configurar los usuarios asignados a este rol
* Team files - configurar el acceso a los [archivos de equipo](team-files)
* Connections - configurar las conexiones asignadas a este rol
* Databases - configurar los [permisos de base de datos](permissions#database-permissions) para este rol
* Tables/views/objects - configurar los [permisos de tabla](permissions#table-permissions) para este rol
* Disk files - configurar el acceso a los archivos en disco o en el volumen de Docker
