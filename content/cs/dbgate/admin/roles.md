---
sourceHash: f3fc7804108ada6b6dc15e241b9e3e162447625c947827b4c1d1f453d871652e
language: cs
title: Role
weight: 40
---

## Záložka Roles
Konfigurace rolí, oprávnění rolí a mapování rolí na připojení. Můžete vytvářet vlastní role a přiřazovat k nim uživatele, takže oprávnění a propojená připojení jsou sdílena mezi všemi uživateli přiřazenými k této roli.

Existuje několik předdefinovaných rolí:
- superadmin - role používaná pro administrátorskou stránku, https://your_dbgate_instance/admin.html
- logged-user - role používaná pro všechny přihlášené uživatele. Oprávnění můžete přepsat pro konkrétní uživatele
- anonymous-user - role používaná pro uživatele přihlášené metodou ověření "Anonymous"

![Role administration - DbGate](https://media.dbgate.io/img/role-administration-light.png)

### Záložky detailu role
* Info
  * Konfigurace oprávnění role
  * Konfigurace uživatelů přiřazených k této roli
* Team files - konfigurace přístupu k [týmovým souborům](team-files)
* Connections - konfigurace připojení přiřazených k této roli
* Databases - konfigurace [oprávnění k databázím](permissions#database-permissions) pro tuto roli
* Tables/views/objects - konfigurace [oprávnění k tabulkám](permissions#table-permissions) pro tuto roli
* Disk files - konfigurace přístupu k souborům na disku/docker volume
