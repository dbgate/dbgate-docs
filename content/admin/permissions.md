---
title: Permissions
weight: 50
---

## Permissions system
DbGate uses permission system with two dimensional hiearchy.

One hiearchy dimension is inheritance of permissions from roles.
- Predefined permission set
- Predefined role (superadmin/logged-user/anonymous user)
- Custom roles
- User

The second hiearchy dimension is inheritance from parent roles.

## Database permissions
You could configure permissions related to database on "Databases" tab (in Role detail and in User detail)

Database permissions are not used, unless **"All databases"** is permission is active

Each line of databases permission rules table defines permission to matched database. The order of rules is important, permissions at the bottom override permissions at the top.

![Database permissions - DbGate](https://media.dbgate.io/img/dbpermissions-light.png)

**Columns:**
* Connection - define, on which connection this rule is applied
* Database names - define database name (by list of names or by regular expression)
* Role:
  * View - view database, without access to tables, views, etc.
  * Read content - access to database content, readonly
  * Write data - change data of tables
  * Run script - run any SQL script, create/drop/alter tables
  * Deny - don't allow access to this database  

## Table Permissions
You could configure permissions related to database on "Tables/Views/Objects" tab (in Role detail and in User detail)

Tables permissions are not used, unless **"All tables/views/objects"** is permission is active

Each line of databases permission rules table defines permission to matched table. The order of rules is important, permissions at the bottom override permissions at the top.

**Columns:**
* Connection - define, on which connection this rule is applied
* Database names - define database name (by list of names or by regular expression)
* Schema names - define schema name (by list of names or by regular expression)
* Table names - define table/view/procedure/trigger name (by list of names or by regular expression)
* Scope - defines types of matched object
* Role:
  * Read - read table data
  * Update only - update table rows, don't allow to insert and delete operations
  * Run script - allow to run script with this table. In fact, if you don't have "Run script" permission on database level, this cannot be used
  * Deny - don't allow access to this table

