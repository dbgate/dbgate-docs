---
title: Roles
weight: 40
---

## Roles tab
Configure roles, role permissions and role-connection mapping. You could create custom roles and assign users to them, so that permissions and linked connections are shared between all users assigned to this role.

There are some predefined roles:
- superadmin - role used for admin page, https://your_dbgate_instance/admin.html
- logged-user - role used for all logged users. You could ovveride permission for specific users
- anonymous-user - role used for users logged with "Anonymous" authentication method

![Role administration - DbGate](https://media.dbgate.io/img/role-administration-light.png)

### Role detail tabs
* Info
  * Configure role permissions
  * Configure user assigned to this role
* Connections - configure connections assigned to this role
* Databases - configure [database permissions](permissions#database-permissions) for this role
* Tables/views/objects - configure [table permissions](permissions#table-permissions) for this role
