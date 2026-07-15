---
sourceHash: 360217298d149b763ae90c89f93377a23ff2648b5b8801d08c83aeb3f3ae35ce
language: fr
title: Connexion
weight: 20
---

Se connecter à votre base de données depuis DbGate est simple. Vous pouvez vous connecter à une base de données de plusieurs façons :

* Menu Fichier/Ajouter une connexion ou icône {{< mdi "plus-thick" >}} dans le widget CONNEXIONS
* Menu Fichier/Nouvelle base de données SQLite - crée une nouvelle base de données SQLite
* Menu Fichier/Ouvrir - vous pouvez ouvrir une base de données SQLite existante

## Écran de connexion
![Écran de connexion](https://media.dbgate.io/img/new-connection-light.png)

Les champs de l'écran de connexion dépendent fortement du type de connexion.

Quelques champs communs :

* Serveur - nom d'hôte du serveur de base de données
* Port - port ; dans le cas du port par défaut de la base de données, vous pouvez le laisser vide
* Utilisateur, Mot de passe - authentification
* Mode de mot de passe
    * Enregistrer et chiffrer - le mot de passe est enregistré de façon chiffrée, vous ne pourrez pas le voir la prochaine fois
    * Enregistrer en clair - le mot de passe est enregistré tel quel (sans chiffrement), vous pourrez le consulter plus tard
    * Ne pas enregistrer, demander le mot de passe - le mot de passe n'est pas enregistré, vous devez le saisir lors de la connexion
    * Ne pas enregistrer, demander l'identifiant et le mot de passe - ni le mot de passe ni l'identifiant ne sont enregistrés, vous devez saisir les deux lors de la connexion
* Lecture seule - la connexion sera en lecture seule (pour les moteurs sans prise en charge des sessions en lecture seule, vous ne pourrez pas exécuter de requêtes SQL dans ce cas)
* Base de données par défaut - quelle base de données sera active après la connexion
* Utiliser uniquement la base de données *&lt;base de données par défaut&gt;* - si cette option est cochée, seule la base de données par défaut apparaît dans l'arborescence de connexion (les autres bases de données du serveur sont masquées)
* Nom affiché - nom sous lequel la connexion apparaîtra dans l'application

## Tunnel SSH
Vous pouvez configurer ici une connexion via un tunnel SSH.

Champs communs :
* Utiliser un tunnel SSH - cochez pour utiliser un tunnel SSH
* Hôte - nom d'hôte du serveur SSH

![DbGate - configuration du tunnel SSH](https://media.dbgate.io/img/connection-sshtunnel-window-light.png)

## SSL
Configurez la connexion SSL.

Champs communs :
* Utiliser SSL - cochez pour utiliser SSL. Dans la plupart des cas, c'est la seule chose que vous ayez à configurer pour utiliser SSL

![DbGate - configuration de la connexion SSL](https://media.dbgate.io/img/connection-ssl-window-light.png)
