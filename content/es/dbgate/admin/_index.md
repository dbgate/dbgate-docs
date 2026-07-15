---
sourceHash: ede2384faaa854f0e026527b8904456ab9b2e5bb8e75f17843afd05cbe47ca54
language: es
title: Administración
weight: 60
---

La interfaz de administración permite a un equipo ejecutar DbGate como una aplicación web compartida y multiusuario: gestionas las conexiones de forma centralizada, defines quién puede iniciar sesión y cómo, y concedes acceso detallado a bases de datos y objetos mediante usuarios, roles y permisos. También aloja los archivos compartidos del equipo. Todo lo que se configura aquí se almacena en la base de datos de almacenamiento en lugar de en archivos locales.

La herramienta de administración solo está disponible en la edición Team Premium. En la edición Community, configura DbGate mediante [variables de entorno](/es/dbgate/customization/env-variables) en su lugar.

Toda la configuración de la administración se guarda en la base de datos de almacenamiento; usa las [variables de entorno STORAGE_xxx](/es/dbgate/customization/env-variables/#team-premium-edition-configuration) para configurarla.

En esta sección:

* [Autenticación](auth) - configura los métodos de inicio de sesión y los proveedores de identidad
* [Conexiones](connection) - gestiona las conexiones disponibles para tu equipo
* [Archivos de equipo](team-files) - comparte scripts SQL, diagramas ER y gráficos
* [Usuarios](users) - gestiona las cuentas de usuario
* [Roles](roles) - agrupa permisos en roles
* [Permisos](permissions) - concede acceso a conexiones, bases de datos y tablas

## Acceso de administrador

La página de administración está disponible en la URL https://your_dbgate_instance/admin.html . 

El administrador root debe tener una contraseña definida. Puedes establecer la variable de entorno ADMIN_PASSWORD. Si esta variable no está definida, DbGate solicita la contraseña de administrador la primera vez.

Después puedes añadir el permiso de administración a otro usuario con un método de autenticación distinto, pero primero tienes que abrir esta página de administración.

