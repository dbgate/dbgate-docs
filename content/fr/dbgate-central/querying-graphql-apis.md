---
sourceHash: 0413647e4082277a5414b137c9b738bb5454cdf2da42397cc555e87f9b1b7823
language: fr
title: Interroger des API GraphQL
weight: 20
---

Pointez DbGate Central vers n'importe quelle API GraphQL et il découvre ce qui est disponible pour vous - inutile de fouiller dans une documentation séparée.

## Explorer le schéma

DbGate Central introspecte le schéma GraphQL dès que vous vous connectez. Parcourez les types et les champs disponibles dans l'arborescence, puis ouvrez un onglet de requête pour commencer à travailler.

## Exécuter des requêtes

* Écrivez des requêtes avec l'éditeur GraphQL et exécutez-les sur l'API en direct.
* Fournissez les variables de requête en même temps que la requête, soit dans un formulaire, soit sous forme de JSON brut.
* Les résultats sont renvoyés dans la même grille rapide, triable et filtrable utilisée partout dans DbGate, si bien qu'une réponse GraphQL ressemble à une table de base de données.
* Les objets et listes imbriqués sont renvoyés sous forme de JSON structuré que vous pouvez déplier et inspecter sur place.

Les vues interrogées sont mises en cache par connexion, si bien que leur réouverture est instantanée pendant que vous continuez à travailler.

> Les connexions GraphQL dans DbGate Central sont une implémentation distincte, basée sur le navigateur, de la [fonctionnalité GraphQL du bureau](/fr/dbgate/developer/api-connections/#graphql) - consultez cette page si vous utilisez plutôt l'application de bureau.

![DbGate Central - query a GraphQL API](https://lite.dbgate.io/screenshots/central-graphql-dark.png)
