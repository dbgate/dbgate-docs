---
sourceHash: d544deb1088946415d8fae3a2b5da3de8bee338a8dfe25d4d99541b1252b56c5
language: fr
title: Authentification
weight: 10
---

## Onglet Authentification
Il existe plusieurs méthodes d'authentification. L'utilisateur choisira la méthode d'authentification sur la page de connexion. Si vous n'avez activé qu'une seule méthode d'authentification et que celle-ci ne nécessite pas de page de connexion, la page de connexion est ignorée.

![Administration de l'authentification - DbGate](https://media.dbgate.io/img/authentication-administration-light.png)

- Méthode d'authentification locale - l'utilisateur est sélectionné dans la liste des utilisateurs de la base de données de stockage (configurée dans l'onglet « Users »)
- Anonyme - aucune information d'identification n'est requise, l'utilisateur dispose des permissions du rôle « anonymous-user »
- Utiliser la connexion à la base de données - les informations d'identification sont redirigées vers le serveur de base de données. L'utilisateur choisira la connexion dans l'onglet « Connections »
- OAuth 2.0 - fournisseur OAuth générique. Avec un peu d'effort et les connaissances appropriées, il peut être configuré avec la plupart des fournisseurs d'identité récents, comme Google, Facebook ou Keycloak
- Active Directory - accès à AD via le protocole LDAP
- Microsoft Entra - anciennement Azure Active Directory - accès par authentification unique aux bases de données Azure

### Option « Allow only defined logins »
Pour les fournisseurs d'identité externes, l'utilisateur n'a pas besoin d'exister dans la base de données de stockage de DbGate. Si cette case est cochée, un utilisateur qui n'est pas trouvé dans la base de données de stockage n'est pas autorisé à se connecter

### Keycloak

Keycloak peut être intégré à DbGate à l'aide du fournisseur OAuth 2.0 générique. Pour configurer l'authentification Keycloak, vous devez :

1. Créer un nouveau client dans votre realm Keycloak
2. Configurer les paramètres du client
3. Configurer le fournisseur OAuth 2.0 dans DbGate avec les paramètres suivants :

**Configuration requise :**
- **OAuth auth endpoint** : `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/auth`
- **OAuth token endpoint** : `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/token`
- **OAuth logout endpoint** : `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/logout`
- **OAuth client** : l'ID de votre client Keycloak
- **OAuth login field** : le claim Keycloak qui contient l'identifiant de connexion de l'utilisateur (généralement `preferred_username` ; selon votre configuration Keycloak, vous pouvez également utiliser `given_name`, `email` ou un autre claim approprié)

**Configuration du client Keycloak :**
- Valid Redirect URIs : `https://dbgate.company.com/`

Assurez-vous que les attributs de vos utilisateurs Keycloak sont correctement mappés afin de fournir les claims nécessaires (email, nom, nom d'utilisateur) que DbGate attend du fournisseur OAuth.


