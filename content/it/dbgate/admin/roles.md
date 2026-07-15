---
sourceHash: f3fc7804108ada6b6dc15e241b9e3e162447625c947827b4c1d1f453d871652e
language: it
title: Ruoli
weight: 40
---

## Scheda Roles
Configura i ruoli, le autorizzazioni dei ruoli e la mappatura tra ruoli e connessioni. Puoi creare ruoli personalizzati e assegnarvi gli utenti, in modo che le autorizzazioni e le connessioni collegate siano condivise tra tutti gli utenti assegnati a questo ruolo.

Esistono alcuni ruoli predefiniti:
- superadmin - ruolo utilizzato per la pagina di amministrazione, https://your_dbgate_instance/admin.html
- logged-user - ruolo utilizzato per tutti gli utenti autenticati. Puoi sovrascrivere le autorizzazioni per utenti specifici
- anonymous-user - ruolo utilizzato per gli utenti autenticati con il metodo di autenticazione "Anonymous"

![Role administration - DbGate](https://media.dbgate.io/img/role-administration-light.png)

### Schede di dettaglio del ruolo
* Info
  * Configura le autorizzazioni del ruolo
  * Configura gli utenti assegnati a questo ruolo
* Team files - configura l'accesso ai [file del team](team-files)
* Connections - configura le connessioni assegnate a questo ruolo
* Databases - configura le [autorizzazioni dei database](permissions#database-permissions) per questo ruolo
* Tables/views/objects - configura le [autorizzazioni delle tabelle](permissions#table-permissions) per questo ruolo
* Disk files - configura l'accesso ai file su disco/volume docker
