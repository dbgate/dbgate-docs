---
sourceHash: e260ab1affedec4216935e4608a9e283db7bec0178fb62eaad167e28d4857df1
language: fr
title: Concepteur de requêtes
weight: 20
---

Le concepteur de requêtes *(Premium)* vous permet de construire des requêtes SQL visuellement, sans écrire de SQL à la main. Ajoutez des tables sur le canevas, choisissez les colonnes et définissez les conditions - DbGate génère le SQL pour vous.

![Query designer](https://media.dbgate.io/img/query-designer-light.png)

## Construire une requête

* **Ajouter des tables** - déposez les tables sur le canevas de conception ; DbGate dessine automatiquement les relations à partir des clés étrangères.
* **Choisir les colonnes** - choisissez les colonnes qui apparaissent dans le résultat, définissez le tri et le regroupement.
* **Types de JOIN** - outre les jointures SQL standard (`INNER`, `LEFT`, `RIGHT`), vous pouvez utiliser des pseudo-jointures - la plus utile étant `WHERE NOT EXISTS`.
* **Filtres puissants** - filtrez à l'aide du même moteur que l'[explorateur de données](/fr/dbgate/working-with-data/data-browser/), y compris les conditions composées et le filtrage par un ensemble de valeurs.

## Résultat

Le concepteur produit une requête SQL normale, elle s'exécute donc avec les mêmes performances qu'un SQL écrit à la main. Vous pouvez basculer à tout moment vers le SQL généré et continuer à l'éditer dans l'[éditeur SQL](sql-editor).

## Perspectives - le concepteur universel

Pour les vues imbriquées et hiérarchiques - et pour joindre des données entre des tables SQL et des collections MongoDB côté client - utilisez les [Perspectives](/fr/dbgate/working-with-data/perspectives/), qui ne sont pas limitées par ce que la base de données source peut joindre.
