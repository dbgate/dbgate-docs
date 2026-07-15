---
sourceHash: 155fd38e071212ba93bef9b8221af07ceb2480ab18ebdeafd80e086b3dcb0477
language: fr
title: Se connecter à des points de terminaison d'API
weight: 10
---

DbGate Central se connecte à trois familles de points de terminaison d'API, en utilisant la même boîte de dialogue Nouvelle connexion pour toutes.

## Types de points de terminaison pris en charge

* **GraphQL** - inspectez le schéma, parcourez les types et exécutez des requêtes sur n'importe quelle API GraphQL.
* **oData** - travaillez avec les services oData V4 comme s'il s'agissait de tables ordinaires.
* **Shopify** - connectez-vous à votre boutique via l'API Shopify Admin et explorez les produits, les commandes, les clients, les métachamps et bien plus encore.

## Créer une connexion

Ouvrez la boîte de dialogue **Nouvelle connexion**, choisissez le type de connexion, saisissez l'URL du service et choisissez la méthode d'authentification :

* **Aucune** - pour les points de terminaison ouverts et publics.
* **Basic** - nom d'utilisateur et mot de passe.
* **Jeton Bearer** - collez un jeton d'accès.
* **Clé d'API** - envoyez une clé dans un en-tête ou un paramètre de requête.

Les connexions sont enregistrées dans votre espace de travail, elles sont donc disponibles à votre prochaine connexion, sur n'importe quel appareil, sans rien à configurer localement.

![DbGate Central - connect to an API endpoint](https://lite.dbgate.io/screenshots/central-connect-api-dark.png)
