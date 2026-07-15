---
sourceHash: d544deb1088946415d8fae3a2b5da3de8bee338a8dfe25d4d99541b1252b56c5
language: sk
title: Autentifikácia
weight: 10
---

## Karta Authentication
Existuje niekoľko metód autentifikácie. Používateľ si zvolí metódu autentifikácie na prihlasovacej stránke. Ak máte povolenú iba jednu metódu autentifikácie a táto metóda nevyžaduje prihlasovaciu stránku, prihlasovacia stránka sa preskočí.

![Správa autentifikácie - DbGate](https://media.dbgate.io/img/authentication-administration-light.png)

- Lokálna autentifikácia - používateľ sa vyberá zo zoznamu používateľov v úložnej databáze (nakonfigurovanej na karte "Users")
- Anonymous - nevyžadujú sa žiadne prihlasovacie údaje, používateľ má oprávnenia z roly "anonymous-user"
- Use database login - prihlasovacie údaje sa presmerujú na databázový server. Používateľ si vyberie pripojenie na karte "Connections"
- OAuth 2.0 - všeobecný poskytovateľ OAuth. S trochou úsilia a správnych znalostí sa dá nakonfigurovať s väčšinou súčasných poskytovateľov identity, ako sú Google, Facebook, Keycloak
- Active Directory - prístup k AD cez protokol LDAP
- Microsoft Entra - bývalý Azure Active Directory - jednotné prihlásenie (single sign-on) k databázam v Azure

### Možnosť "Allow only defined logins"
Pri externých poskytovateľoch identity nemusí používateľ existovať v úložnej databáze DbGate. Ak je toto zaškrtávacie políčko zaškrtnuté, používateľ, ktorý sa nenachádza v úložnej databáze, sa nemôže prihlásiť

### Keycloak

Keycloak je možné integrovať s DbGate pomocou všeobecného poskytovateľa OAuth 2.0. Na nakonfigurovanie autentifikácie cez Keycloak potrebujete:

1. Vytvoriť nového klienta vo vašom Keycloak realme
2. Nakonfigurovať nastavenia klienta
3. Nastaviť poskytovateľa OAuth 2.0 v DbGate s nasledujúcimi parametrami:

**Požadovaná konfigurácia:**
- **OAuth auth endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/auth`
- **OAuth token endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/token`
- **OAuth logout endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/logout`
- **OAuth client**: ID vášho Keycloak klienta
- **OAuth login field**: claim v Keycloaku, ktorý obsahuje prihlasovací identifikátor používateľa (zvyčajne `preferred_username`; v závislosti od vašej konfigurácie Keycloaku môžete použiť aj `given_name`, `email` alebo iný vhodný claim)

**Konfigurácia klienta v Keycloaku:**
- Valid Redirect URIs: `https://dbgate.company.com/`

Uistite sa, že atribúty vašich používateľov v Keycloaku sú správne namapované tak, aby poskytovali potrebné claims (email, meno, používateľské meno), ktoré DbGate od poskytovateľa OAuth očakáva.


