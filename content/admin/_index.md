---
title: Adminstration
weight: 110
---

Administration tool is available only on Team Premium edition. In Community edition, please use configuration using [environment variables](/env-variables)

All configuration from administration is saved into database, use [STORAGE_xxx environment variables](/env-variables/#premium-edition-configuration) for configure this.

## Administrator access

Administration page is available on URL https://your_dbgate_instance/admin.html . 

Root adminstrator should have password defined. You could set environment variable ADMIN_PASSWORD. If this variable is not defined, DbGate asks for admin password at first.

You could then add administration permission to different user with different authentication method, but at first, you have to open this admin page.

