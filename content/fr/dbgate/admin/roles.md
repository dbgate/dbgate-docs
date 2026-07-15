---
sourceHash: f3fc7804108ada6b6dc15e241b9e3e162447625c947827b4c1d1f453d871652e
language: fr
title: Rôles
weight: 40
---

## Onglet Roles
Configurez les rôles, les permissions des rôles et l'association rôle-connexion. Vous pouvez créer des rôles personnalisés et y affecter des utilisateurs, afin que les permissions et les connexions liées soient partagées entre tous les utilisateurs affectés à ce rôle.

Il existe quelques rôles prédéfinis :
- superadmin - rôle utilisé pour la page d'administration, https://your_dbgate_instance/admin.html
- logged-user - rôle utilisé pour tous les utilisateurs connectés. Vous pouvez remplacer les permissions pour des utilisateurs spécifiques
- anonymous-user - rôle utilisé pour les utilisateurs connectés avec la méthode d'authentification « Anonymous »

![Administration des rôles - DbGate](https://media.dbgate.io/img/role-administration-light.png)

### Onglets de détail d'un rôle
* Info
  * Configurer les permissions du rôle
  * Configurer les utilisateurs affectés à ce rôle
* Team files - configurer l'accès aux [fichiers d'équipe](team-files)
* Connections - configurer les connexions affectées à ce rôle
* Databases - configurer les [permissions de base de données](permissions#database-permissions) pour ce rôle
* Tables/views/objects - configurer les [permissions de table](permissions#table-permissions) pour ce rôle
* Disk files - configurer l'accès aux fichiers sur le disque/volume docker
