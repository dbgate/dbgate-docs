---
title: Administration
weight: 60
---

The administration interface lets a team run DbGate as a shared, multi-user web application: you manage connections centrally, define who can sign in and how, and grant fine-grained access to databases and objects through users, roles and permissions. It also hosts shared team files. Everything configured here is stored in the storage database rather than in local files.

The administration tool is available only on the Team Premium edition. In the Community edition, please configure DbGate using [environment variables](/dbgate-classic/customization/env-variables) instead.

All configuration from administration is saved into the storage database - use the [STORAGE_xxx environment variables](/dbgate-classic/customization/env-variables/#team-premium-edition-configuration) to configure it.

In this section:

* [Authentication](auth) - configure sign-in methods and identity providers
* [Connections](connection) - manage the connections available to your team
* [Team Files](team-files) - share SQL scripts, ER diagrams and charts
* [Users](users) - manage user accounts
* [Roles](roles) - group permissions into roles
* [Permissions](permissions) - grant access to connections, databases and tables

## Administrator access

Administration page is available on URL https://your_dbgate_instance/admin.html . 

Root administrator should have password defined. You could set environment variable ADMIN_PASSWORD. If this variable is not defined, DbGate asks for admin password at first.

You could then add administration permission to different user with different authentication method, but at first, you have to open this admin page.

