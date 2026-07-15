---
sourceHash: 7398aa630d6a03209a204d7b2955facf91b926d1e31bd01dc2e515cd6a2dfb95
language: fr
title: DbGate Lite
weight: 30
---

[DbGate Lite](https://lite.dbgate.io/) est un outil gratuit, exécuté dans le navigateur, pour travailler avec les données - sans installation ni connexion. Il repose sur la même grille, le même filtrage et le même moteur de requêtes que [DbGate Central](../dbgate-central/), si bien que la navigation, le filtrage et l'édition se déroulent de la même manière dans les deux produits.

## Apprendre et enseigner le SQL

DbGate Lite exécute **SQLite et DuckDB** entièrement dans votre navigateur, grâce à WebAssembly :

* Écrivez et exécutez des requêtes SQL sur une base de données d'exemple dans la grille DbGate familière.
* Visualisez les relations entre les tables à l'aide de diagrammes ER.
* Aucune installation, aucune connexion - ouvrez le site et commencez à travailler.

## Travail ponctuel avec des fichiers de données

Ouvrez un fichier dans DbGate Lite et traitez-le comme une base de données :

* **Importez** des fichiers CSV, JSON et Excel, puis interrogez-les ou modifiez-les avec SQL.
* Nettoyez et remodelez les données, puis **exportez** le résultat au format CSV, JSON ou Excel.

## Partager une base de données ou une requête via un lien

L'ouverture de DbGate Lite avec certains paramètres de hachage dans l'URL initialise automatiquement une base de données temporaire :

* `initdbtype` - type de base de données, `sqlite` ou `duckdb`
* `initdbscript` - script SQL utilisé pour créer et remplir la base de données temporaire
* `initquery` (facultatif) - requête SQL ouverte dans un nouvel onglet Query

Toute personne qui ouvre le lien obtient la même base de données d'exemple et la même requête en un clic - pratique pour les tutoriels, les rapports de bogues et l'enseignement.

## Publier une vue en lecture seule

Indépendamment du partage d'un lien modifiable, vous pouvez **publier** une vue en lecture seule d'un fichier CSV/JSON ou d'un rapport BI à l'aide du bouton Publish dans la barre d'outils. Cela ouvre une page autonome - uniquement les données et un basculement clair/sombre, sans barre latérale ni éditeur - que toute personne disposant du lien peut consulter sans compte.

## Choisir entre Lite, Central, Premium et Team Premium

DbGate Lite est idéal pour l'apprentissage et les tâches ponctuelles. Pour un travail professionnel continu, un produit dédié convient mieux :

* **DbGate Lite** - gratuit, dans le navigateur. Idéal pour apprendre le SQL et pour les fichiers de données ponctuels.
* **[DbGate Central](../dbgate-central/)** - produit hébergé pour travailler avec les API : connectez-vous à des points de terminaison GraphQL, oData et Shopify en direct, conservez les connexions et les rapports dans un espace de travail et partagez-les avec votre équipe.
* **[DbGate Premium](/fr/dbgate/getting-started/installation/)** - une édition de [DbGate](/fr/dbgate/) : l'application de bureau complète pour travailler avec les bases de données, connectez-vous à des serveurs SQL et NoSQL avec l'ensemble complet d'outils professionnels.
* **[DbGate Team Premium](/fr/dbgate/getting-started/installation/docker-tp/)** - une autre édition de [DbGate](/fr/dbgate/), pour les équipes : une interface web partagée qui s'exécute sur site, afin que toute votre équipe travaille avec les bases de données depuis le navigateur sur votre propre infrastructure.
