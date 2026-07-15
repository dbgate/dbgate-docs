---
sourceHash: 0086e005ede5ab2d89ada748f23fbb27b453941fb9b7bec1159e8683ce1ee803
language: es
title: Permisos
weight: 50
---

Los permisos de DbGate utilizan **dos dimensiones**:

1. **Origen de los permisos (quién los establece)**
   Los permisos se propagan de lo general a lo específico. Los ajustes más específicos prevalecen sobre los más generales:
   * Conjuntos de permisos predefinidos
   * Roles predefinidos (*superadmin*, *usuario autenticado*, *anónimo*)
   * Roles personalizados
   * Usuario individual

2. **Ámbito de los objetos**
   Los permisos pueden aplicarse a **bases de datos** y **tablas/objetos** concretos. Consulte **[Permisos de bases de datos](#database-permissions)** y **[Permisos de tablas](#table-permissions)**.

---

## Permisos básicos

Configure los permisos globales/básicos en el **árbol de permisos** en el **Detalle de usuario** o el **Detalle de rol**.

* Una casilla **atenuada** significa que el permiso es **heredado** (por ejemplo, de un rol o de un conjunto de permisos predefinido), no establecido directamente en ese usuario/rol.

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

---

## Permisos de bases de datos

Establezca los permisos a nivel de base de datos en la pestaña **Bases de datos** (tanto en el Detalle de rol como en el Detalle de usuario).

> **Importante:** las reglas de bases de datos se aplican **solo si** el permiso **“Todas las bases de datos”** está desmarcado en los permisos básicos.

* Cada fila de la tabla de reglas concede o deniega el acceso a las bases de datos que **coinciden** con los filtros de la fila.
* **El orden de las reglas importa**: las reglas situadas **más abajo** en la lista **prevalecen** sobre las anteriores.

![Database permissions - DbGate](https://media.dbgate.io/img/database-permissions-light.png)

**Columnas**

* **Connection** – a qué conexión se aplica la regla.
* **Database names** – bases de datos que deben coincidir (lista de nombres o una expresión regular).
* **Role (nivel de acceso)**
  * **View** – puede ver la base de datos, pero no sus tablas/vistas/etc.
  * **Read content** – acceso de solo lectura al contenido de la base de datos.
  * **Write data** – puede modificar los datos de las tablas.
  * **Run script** – puede ejecutar cualquier script SQL; puede crear/eliminar/modificar objetos.
  * **Deny** – bloquea el acceso a la base de datos.

---

## Permisos de tablas

Establezca los permisos a nivel de tabla/objeto en la pestaña **Tablas / Vistas / Objetos** (en el Detalle de rol y el Detalle de usuario).

> **Importante:** las reglas de tablas/objetos se aplican **solo si** el permiso **“Todas las tablas/vistas/objetos”** está desmarcado en los permisos básicos.

* Cada fila define el acceso a las tablas/objetos que **coinciden** con los filtros.
* **El orden de las reglas importa**: las reglas situadas **más abajo** en la lista **prevalecen** sobre las anteriores.
* De forma predeterminada, los permisos de tabla se **heredan del permiso de la base de datos**.

**Columnas**

* **Connection** – a qué conexión se aplica la regla.
* **Database names** – bases de datos que deben coincidir (lista o expresión regular).
* **Schema names** – esquemas que deben coincidir (lista o expresión regular).
* **Table names** – nombres de objetos que deben coincidir (tabla/vista/procedimiento/disparador) como lista o expresión regular.
* **Scope** – qué tipos de objetos abarca la regla (tablas, vistas, procedimientos, disparadores, …).
* **Role (nivel de acceso)**
  * **Read** – puede leer los datos de la tabla.
  * **Update only** – puede actualizar filas; **insertar** y **eliminar** no están permitidos.
  * **Create, update, delete** - puede editar filas sin restricciones
  * **Run script** – puede ejecutar un script que afecte a este objeto.
    > Nota: si **no** dispone de **“Run script”** a nivel de **base de datos**, no podrá utilizarlo a nivel de tabla.
  * **Deny** – bloquea el acceso al objeto.
