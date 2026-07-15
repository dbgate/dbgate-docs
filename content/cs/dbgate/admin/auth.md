---
sourceHash: d544deb1088946415d8fae3a2b5da3de8bee338a8dfe25d4d99541b1252b56c5
language: cs
title: Autentizace
weight: 10
---

## Záložka Authentication
Existuje několik metod autentizace. Uživatel si zvolí metodu autentizace na přihlašovací stránce. Pokud máte povolenou pouze jednu metodu autentizace a tato metoda nevyžaduje přihlašovací stránku, je přihlašovací stránka přeskočena.

![Authentication administration - DbGate](https://media.dbgate.io/img/authentication-administration-light.png)

- Lokální metoda autentizace - uživatel je vybrán ze seznamu uživatelů v úložné databázi (konfiguruje se v záložce "Users")
- Anonymní - nejsou vyžadovány žádné přihlašovací údaje, uživatel má oprávnění z role "anonymous-user"
- Použití přihlášení do databáze - přihlašovací údaje jsou přesměrovány na databázový server. Uživatel si zvolí připojení v záložce "Connections"
- OAuth 2.0 - obecný poskytovatel OAuth. S trochou úsilí a potřebnými znalostmi lze nakonfigurovat s většinou současných poskytovatelů identit, jako je Google, Facebook nebo Keycloak
- Active Directory - přístup k AD přes protokol LDAP
- Microsoft Entra - dříve Azure Active Directory - jednotné přihlášení (single sign-on) k databázím v Azure

### Volba "Allow only defined logins"
U externích poskytovatelů identit nemusí uživatel existovat v úložné databázi DbGate. Pokud je toto zaškrtávací pole zaškrtnuto, uživatel, který není nalezen v úložné databázi, se nesmí přihlásit

### Keycloak

Keycloak lze integrovat s DbGate pomocí obecného poskytovatele OAuth 2.0. Pro konfiguraci autentizace přes Keycloak je potřeba:

1. Vytvořit nového klienta ve vašem Keycloak realmu
2. Nakonfigurovat nastavení klienta
3. Nastavit v DbGate poskytovatele OAuth 2.0 s následujícími parametry:

**Požadovaná konfigurace:**
- **OAuth auth endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/auth`
- **OAuth token endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/token`
- **OAuth logout endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/logout`
- **OAuth client**: ID vašeho Keycloak klienta
- **OAuth login field**: claim v Keycloaku, který obsahuje přihlašovací identifikátor uživatele (obvykle `preferred_username`; v závislosti na vaší konfiguraci Keycloaku můžete použít také `given_name`, `email` nebo jiný vhodný claim)

**Konfigurace klienta v Keycloaku:**
- Valid Redirect URIs: `https://dbgate.company.com/`

Ujistěte se, že atributy uživatelů v Keycloaku jsou správně namapovány tak, aby poskytovaly potřebné claims (email, name, username), které DbGate od poskytovatele OAuth očekává.


