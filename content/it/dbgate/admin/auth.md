---
sourceHash: d544deb1088946415d8fae3a2b5da3de8bee338a8dfe25d4d99541b1252b56c5
language: it
title: Autenticazione
weight: 10
---

## Scheda Autenticazione
Esistono diversi metodi di autenticazione. L'utente sceglierà il metodo di autenticazione nella pagina di login. Se è abilitato un solo metodo di autenticazione e tale metodo non richiede la pagina di login, la pagina di login viene saltata.

![Amministrazione dell'autenticazione - DbGate](https://media.dbgate.io/img/authentication-administration-light.png)

- Metodo di autenticazione locale - l'utente viene selezionato dall'elenco utenti nel database di archiviazione (configurato nella scheda "Users")
- Anonimo - non sono richieste credenziali, l'utente ha i permessi del ruolo "anonymous-user"
- Usa login del database - le credenziali vengono inoltrate al server del database. L'utente sceglierà la connessione dalla scheda "Connections"
- OAuth 2.0 - provider OAuth generico. Con un po' di impegno e le adeguate conoscenze, può essere configurato con la maggior parte dei provider di identità recenti, come Google, Facebook, Keycloak
- Active Directory - accesso ad AD tramite protocollo LDAP
- Microsoft Entra - precedentemente Azure Active Directory - accesso single sign-on ai database Azure

### Opzione "Allow only defined logins"
Per i provider di identità esterni, l'utente non deve necessariamente esistere nel database di archiviazione di DbGate. Se questa casella di controllo è selezionata, un utente che non viene trovato nel database di archiviazione non è autorizzato ad accedere

### Keycloak

Keycloak può essere integrato con DbGate utilizzando il provider OAuth 2.0 generico. Per configurare l'autenticazione Keycloak è necessario:

1. Creare un nuovo client nel proprio realm Keycloak
2. Configurare le impostazioni del client
3. Impostare il provider OAuth 2.0 in DbGate con i seguenti parametri:

**Configurazione richiesta:**
- **OAuth auth endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/auth`
- **OAuth token endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/token`
- **OAuth logout endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/logout`
- **OAuth client**: l'ID del client Keycloak
- **OAuth login field**: il claim di Keycloak che contiene l'identificatore di login dell'utente (comunemente `preferred_username`; a seconda della configurazione di Keycloak è possibile utilizzare anche `given_name`, `email` o un altro claim adeguato)

**Configurazione del client Keycloak:**
- Valid Redirect URIs: `https://dbgate.company.com/`

Assicurarsi che gli attributi utente di Keycloak siano mappati correttamente in modo da fornire i claim necessari (email, nome, username) che DbGate si aspetta dal provider OAuth.


