---
sourceHash: d544deb1088946415d8fae3a2b5da3de8bee338a8dfe25d4d99541b1252b56c5
language: de
title: Authentifizierung
weight: 10
---

## Registerkarte "Authentifizierung"
Es gibt mehrere Authentifizierungsmethoden. Der Benutzer wählt die Authentifizierungsmethode auf der Anmeldeseite aus. Wenn nur eine Authentifizierungsmethode aktiviert ist und diese keine Anmeldeseite erfordert, wird die Anmeldeseite übersprungen.

![Authentifizierungsverwaltung - DbGate](https://media.dbgate.io/img/authentication-administration-light.png)

- Lokale Authentifizierungsmethode - der Benutzer wird aus der Benutzerliste in der Speicherdatenbank ausgewählt (konfiguriert in der Registerkarte "Users")
- Anonym - es sind keine Anmeldedaten erforderlich, der Benutzer erhält die Berechtigungen der Rolle "anonymous-user"
- Datenbank-Anmeldung verwenden - die Anmeldedaten werden an den Datenbankserver weitergeleitet. Der Benutzer wählt die Verbindung in der Registerkarte "Connections" aus
- OAuth 2.0 - generischer OAuth-Anbieter. Mit etwas Aufwand und entsprechenden Kenntnissen lässt sich damit die Mehrzahl der aktuellen Identitätsanbieter konfigurieren, z. B. Google, Facebook, Keycloak
- Active Directory - AD-Zugriff über das LDAP-Protokoll
- Microsoft Entra - ehemals Azure Active Directory - Single-Sign-on-Zugriff auf Azure-Datenbanken

### Option "Allow only defined logins"
Bei externen Identitätsanbietern muss der Benutzer nicht in der DbGate-Speicherdatenbank vorhanden sein. Wenn dieses Kontrollkästchen aktiviert ist, darf sich ein Benutzer, der nicht in der Speicherdatenbank gefunden wird, nicht anmelden

### Keycloak

Keycloak kann über den generischen OAuth 2.0-Anbieter in DbGate integriert werden. Um die Keycloak-Authentifizierung zu konfigurieren, müssen Sie:

1. Einen neuen Client in Ihrem Keycloak-Realm anlegen
2. Die Client-Einstellungen konfigurieren
3. Den OAuth 2.0-Anbieter in DbGate mit den folgenden Parametern einrichten:

**Erforderliche Konfiguration:**
- **OAuth auth endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/auth`
- **OAuth token endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/token`
- **OAuth logout endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/logout`
- **OAuth client**: Ihre Keycloak-Client-ID
- **OAuth login field**: der Keycloak-Claim, der die Anmeldekennung des Benutzers enthält (üblicherweise `preferred_username`; je nach Ihrer Keycloak-Konfiguration können Sie auch `given_name`, `email` oder einen anderen geeigneten Claim verwenden)

**Keycloak-Client-Konfiguration:**
- Valid Redirect URIs: `https://dbgate.company.com/`

Stellen Sie sicher, dass Ihre Keycloak-Benutzerattribute korrekt zugeordnet sind, sodass die notwendigen Claims (E-Mail, Name, Benutzername) bereitgestellt werden, die DbGate vom OAuth-Anbieter erwartet.


