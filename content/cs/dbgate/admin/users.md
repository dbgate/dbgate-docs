---
sourceHash: e88bb0618f23a7bdce895dcef0093c2c2dbd7ad2ee16c003e961c2e51a419cab
language: cs
title: Uživatelé
weight: 30
---

## Záložka Users
Nastavte uživatele, hesla, uživatelská oprávnění a mapování uživatelů na připojení.
Hesla se používají pouze pro metody ověřování typu "Local". Ale všechny metody s externími poskytovateli identity používají vyhledání uživatele, takže můžete nastavit oprávnění a připojení dostupná pro uživatele, a to i pro externě ověřeného uživatele. 

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

### Záložky detailu uživatele
* Info
  * Nastavení uživatelských oprávnění
  * Nastavení rolí přiřazených tomuto uživateli
* Team files - nastavení přístupu k [týmovým souborům](team-files)
* Connections - nastavení připojení přiřazených tomuto uživateli
* Databases - nastavení [oprávnění k databázím](permissions#database-permissions) pro tohoto uživatele
* Tables/views/objects - nastavení [oprávnění k tabulkám](permissions#table-permissions) pro tohoto uživatele
* Disk files - nastavení přístupu k souborům na disku/docker volume
