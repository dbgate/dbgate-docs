---
sourceHash: 7fa891cd013b615be872e6897dd3bef55b9e44378ab58adeb9642df7bd80bb79
language: fr
title: DbGate Cloud
weight: 80
---

DbGate Cloud est un stockage en ligne pour vos connexions, scripts SQL et autres objets. Il propose également une base de connaissances publique de scripts SQL utiles.

> DbGate Cloud est un complément de stockage pour l'application DbGate **desktop** (connexions, scripts SQL, dossiers partagés). Vous cherchez plutôt une application hébergée, uniquement dans le navigateur ? Voir [DbGate Central](/fr/dbgate-central/).

## Connexion
Pour utiliser DbGate Cloud, il est nécessaire de se connecter. Utilisez l'icône {{< mdi "account-remove-outline" >}} dans le panneau de gauche.

Votre stockage cloud est toujours associé à votre adresse e-mail.  
Vous pouvez choisir l'un des fournisseurs d'authentification suivants :
* GMail
* GitHub
* E-mail - un lien magique de connexion à usage unique sera envoyé à votre adresse e-mail

Les serveurs DbGate ne stockent pas votre mot de passe.

## Utiliser les connexions stockées sur le cloud
Votre contenu cloud apparaît sous le widget {{< mdi "cloud-key" >}} après la connexion. Par défaut, vous voyez votre dossier Private (avec accès en écriture).

Enregistrer une connexion sur le cloud :
* Menu contextuel de la connexion, choisissez « Copy to cloud folder »
* Cliquez sur {{<mdi "plus-thick" >}}, puis choisissez « Add connection on cloud »

## Quelle connexion est stockée sur le cloud ?
* Vos connexions cloud se trouvent toujours sous le widget {{< mdi "cloud-key" >}}
* Vos connexions stockées localement sous le widget {{< mdi "database" >}}

## Travailler avec les dossiers
Vous pouvez créer d'autres dossiers en plus de votre dossier Private (édition Premium requise).

Sous le bouton {{<mdi "plus-thick" >}}, les commandes suivantes sont disponibles :
* New shared folder - crée un nouveau dossier partagé. Par défaut, il n'est accessible qu'à vous, vous pouvez inviter d'autres utilisateurs
* Add existing shared folder - si vous disposez d'un lien d'invitation vers un dossier partagé (créé par un autre utilisateur), c'est ici qu'il faut l'utiliser

Si vous souhaitez partager votre dossier avec d'autres personnes, faites un clic droit sur le dossier et choisissez « Copy invite link »

## Permissions des dossiers partagés
* Admin - vous avez un accès complet au dossier, vous pouvez inviter d'autres personnes et écrire du contenu
* Write - vous pouvez écrire/supprimer du contenu, mais vous ne pouvez pas inviter d'autres personnes
* Read - lecture seule du contenu du dossier. Veuillez noter que cette permission ne s'applique pas aux bases de données disponibles au sein d'une connexion définie sur un serveur

## Dossiers partagés dans l'édition Community
Dans l'édition Community, vous pouvez utiliser les dossiers partagés créés par des utilisateurs Premium, mais vous ne pouvez pas créer vos propres dossiers partagés. Cela permet aux équipes disposant de l'édition Premium de partager des connexions, des fichiers SQL et des diagrammes ER avec d'autres membres de l'équipe utilisant l'édition Community.

## Base de connaissances publique
La base de connaissances publique est une collection de scripts SQL et de graphiques utiles pour des tâches telles que l'optimisation des performances SQL, l'analyse des interblocages, l'utilisation des index, etc. La base de connaissances est disponible dans toutes les éditions, mais les graphiques ne sont disponibles que dans les éditions Premium.

Vous pouvez voir tous les éléments sous l'icône {{< mdi "cloud-search" >}} dans le panneau de widgets de gauche.  
Les scripts grisés indiquent les scripts qui ne sont pas compatibles avec la base de données actuellement sélectionnée.

Si vous souhaitez enrichir la base de connaissances avec vos scripts SQL, veuillez créer une pull request dans le dépôt GIT [dbgate-knowledge-base](https://github.com/dbgate/dbgate-knowledge-base).

Les scripts de la base de connaissances sont annotés avec la syntaxe [SQL front matter](/fr/dbgate/developer/sql-front-matter)

![DbGate screenshot](https://media.dbgate.io/img/public-knowledge-base-tables-sizes-light.png)
