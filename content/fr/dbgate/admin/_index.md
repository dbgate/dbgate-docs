---
sourceHash: ede2384faaa854f0e026527b8904456ab9b2e5bb8e75f17843afd05cbe47ca54
language: fr
title: Administration
weight: 60
---

L'interface d'administration permet à une équipe d'exécuter DbGate comme une application web partagée et multi-utilisateur : vous gérez les connexions de manière centralisée, définissez qui peut se connecter et comment, et accordez un accès précis aux bases de données et aux objets via les utilisateurs, les rôles et les permissions. Elle héberge également les fichiers partagés de l'équipe. Tout ce qui est configuré ici est stocké dans la base de données de stockage plutôt que dans des fichiers locaux.

L'outil d'administration n'est disponible que dans l'édition Team Premium. Dans l'édition Community, veuillez configurer DbGate à l'aide des [variables d'environnement](/fr/dbgate/customization/env-variables).

Toute la configuration issue de l'administration est enregistrée dans la base de données de stockage - utilisez les [variables d'environnement STORAGE_xxx](/fr/dbgate/customization/env-variables/#team-premium-edition-configuration) pour la configurer.

Dans cette section :

* [Authentification](auth) - configurer les méthodes de connexion et les fournisseurs d'identité
* [Connexions](connection) - gérer les connexions disponibles pour votre équipe
* [Fichiers d'équipe](team-files) - partager des scripts SQL, des diagrammes ER et des graphiques
* [Utilisateurs](users) - gérer les comptes utilisateurs
* [Rôles](roles) - regrouper les permissions en rôles
* [Permissions](permissions) - accorder l'accès aux connexions, bases de données et tables

## Accès administrateur

La page d'administration est disponible à l'URL https://your_dbgate_instance/admin.html . 

L'administrateur root doit avoir un mot de passe défini. Vous pouvez définir la variable d'environnement ADMIN_PASSWORD. Si cette variable n'est pas définie, DbGate demande d'abord le mot de passe administrateur.

Vous pouvez ensuite ajouter la permission d'administration à un autre utilisateur avec une méthode d'authentification différente, mais vous devez d'abord ouvrir cette page d'administration.

