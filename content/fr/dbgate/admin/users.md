---
sourceHash: e88bb0618f23a7bdce895dcef0093c2c2dbd7ad2ee16c003e961c2e51a419cab
language: fr
title: Utilisateurs
weight: 30
---

## Onglet Utilisateurs
Configurez les utilisateurs, les mots de passe, les permissions des utilisateurs et l'association utilisateur-connexion.
Les mots de passe ne sont utilisés que pour les méthodes d'authentification « Local ». Mais toutes les méthodes avec des fournisseurs d'identité externes utilisent la recherche d'utilisateur, vous pouvez donc configurer les permissions et les connexions disponibles pour un utilisateur, même pour un utilisateur authentifié en externe. 

![Administration des rôles - DbGate](https://media.dbgate.io/img/user-administration-light.png)

### Onglets de détail de l'utilisateur
* Info
  * Configurer les permissions de l'utilisateur
  * Configurer les rôles attribués à cet utilisateur
* Team files - configurer l'accès aux [fichiers d'équipe](team-files)
* Connections - configurer les connexions attribuées à cet utilisateur
* Databases - configurer les [permissions de base de données](permissions#database-permissions) pour cet utilisateur
* Tables/views/objects - configurer les [permissions de table](permissions#table-permissions) pour cet utilisateur
* Disk files - configurer l'accès aux fichiers sur le disque/volume docker
