---
sourceHash: f3fc7804108ada6b6dc15e241b9e3e162447625c947827b4c1d1f453d871652e
language: sk
title: Role
weight: 40
---

## Karta Roles
Nakonfigurujte role, oprávnenia rolí a mapovanie rola-pripojenie. Môžete vytvárať vlastné role a priraďovať k nim používateľov, takže oprávnenia a prepojené pripojenia sú zdieľané medzi všetkými používateľmi priradenými k tejto role.

Existuje niekoľko preddefinovaných rolí:
- superadmin - rola používaná pre administrátorskú stránku, https://your_dbgate_instance/admin.html
- logged-user - rola používaná pre všetkých prihlásených používateľov. Oprávnenia môžete prepísať pre konkrétnych používateľov
- anonymous-user - rola používaná pre používateľov prihlásených metódou overenia "Anonymous"

![Správa rolí - DbGate](https://media.dbgate.io/img/role-administration-light.png)

### Karty detailu roly
* Info
  * Konfigurácia oprávnení roly
  * Konfigurácia používateľov priradených k tejto role
* Team files - konfigurácia prístupu k [tímovým súborom](team-files)
* Connections - konfigurácia pripojení priradených k tejto role
* Databases - konfigurácia [oprávnení k databázam](permissions#database-permissions) pre túto rolu
* Tables/views/objects - konfigurácia [oprávnení k tabuľkám](permissions#table-permissions) pre túto rolu
* Disk files - konfigurácia prístupu k súborom na disku/docker volume
