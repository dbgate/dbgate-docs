---
title: Users
weight: 30
---

## Users tab
Configure users, passwords, user permissions and user-connection mapping.
Passwords are used only for "Local" authentication methods. But all methods with external identity providers use user lookup, so you could configure permissions and connections available for user, even for externaly authenticated user. 

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

### User detail tabs
* Info
  * Configure user permissions
  * Configure roles assigned to this user
* Team files - configure access to [team files](team-files)
* Connections - configure connections assigned to this user
* Databases - configure [database permissions](permissions#database-permissions) for this user
* Tables/views/objects - configure [table permissions](permissions#table-permissions) for this user
* Disk files - configure access to files on disk/docker volume
