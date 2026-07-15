---
sourceHash: 522467e3ddd1d9c344e28c1852c3352bf7f649ebf74344ba5372fcc2a245b598
language: fr
title: Connexions API
weight: 10
---

DbGate prend en charge les connexions aux API REST, aux services GraphQL et aux points de terminaison OData. Ces connexions API utilisent les mêmes modèles d'interface que les connexions aux bases de données, ce qui vous permet de travailler avec des API et des bases de données dans un environnement unifié.

La prise en charge des connexions API est disponible dans DbGate Premium.

> Vous cherchez à explorer des API sans l'application de bureau ? [DbGate Central](/fr/dbgate-central/connecting-to-api-endpoints/) est une implémentation distincte et hébergée des connexions GraphQL/oData/Shopify, réimplémentée de zéro pour le navigateur.

## GraphQL

Les connexions GraphQL vous permettent d'interagir avec des API GraphQL. DbGate offre des fonctionnalités d'introspection de schéma et d'exécution de requêtes.

### Créer une connexion GraphQL

Pour créer une connexion GraphQL, utilisez la boîte de dialogue New Connection et sélectionnez GraphQL comme type de connexion. Saisissez l'URL du point de terminaison GraphQL et configurez l'authentification si nécessaire.

### Introspection de schéma

DbGate découvre automatiquement le schéma GraphQL, y compris les types disponibles, les requêtes, les mutations et leurs arguments. L'explorateur de schéma affiche le système de types et vous permet d'explorer la structure de l'API.

### Éditeur de requêtes

L'éditeur de requêtes GraphQL vous permet d'écrire des requêtes et des mutations. Vous pouvez utiliser l'explorateur GraphQL pour construire des requêtes en sélectionnant des champs et des arguments dans le schéma.

![screenshot](https://media.dbgate.io/img/rest-graphql-query-light.png)

### Variables

Les requêtes GraphQL prennent en charge les variables. Définissez les variables dans le panneau des variables et référencez-les dans vos requêtes en utilisant la syntaxe standard des variables GraphQL. Les variables peuvent être modifiées dans un formulaire ou sous forme de JSON brut.

### Visionneuse de réponses

Les résultats des requêtes sont affichés dans une visionneuse JSON formatée avec une arborescence extensible. Si des tableaux sont détectés dans la réponse, la vue tabulaire s'affiche automatiquement. Vous pouvez revenir à la vue JSON brute si nécessaire.

## OpenAPI (Swagger)

Les connexions OpenAPI prennent en charge les API REST qui fournissent des spécifications OpenAPI (versions 2.0 et 3.0).

### Créer une connexion OpenAPI

Créez une nouvelle connexion et sélectionnez OpenAPI comme type de connexion. Indiquez l'URL du fichier de spécification OpenAPI (généralement swagger.json ou openapi.json). DbGate analysera la spécification et rendra disponibles tous les points de terminaison documentés.

### Explorateur de documentation d'API

L'explorateur OpenAPI affiche tous les points de terminaison disponibles, organisés par tags et par chemins. Pour chaque point de terminaison, vous pouvez consulter :
- La méthode HTTP (GET, POST, PUT, DELETE, PATCH)
- Les paramètres (chemin, requête, en-tête, corps)
- Les schémas du corps de la requête
- Les descriptions de la documentation

### Exécution de requêtes

Sélectionnez un point de terminaison pour ouvrir le générateur de requêtes. Renseignez les paramètres requis, les en-têtes et le corps de la requête. Exécutez la requête pour l'envoyer au serveur d'API.

![screenshot](https://media.dbgate.io/img/rest-openapi-query-light.png)

### Inspection des réponses

Consultez le code de statut, les en-têtes et le corps de la réponse. Les réponses JSON sont formatées et peuvent être affichées à la fois en vue arborescente et en vue tabulaire. Les réponses non JSON sont affichées sous forme de texte.

## OData

Les connexions OData permettent d'interroger des services OData en utilisant la syntaxe de requête OData standard.

### Créer une connexion OData

Créez une nouvelle connexion avec OData comme type de connexion. Saisissez l'URL racine du service OData. DbGate récupérera le document de métadonnées du service.

### Exploration des métadonnées

L'explorateur de métadonnées affiche les ensembles d'entités, les types d'entités, les propriétés et les relations définis dans les métadonnées du service.

### Exécution de requêtes

Les requêtes OData prennent en charge les options de requête OData standard :
- `$filter` - filtrer les entités selon les valeurs des propriétés
- `$select` - spécifier les propriétés à retourner
- `$expand` - inclure les entités liées
- `$orderby` - trier les résultats
- `$top` et `$skip` - pagination
- `$count` - inclure le nombre de résultats

![screenshot](https://media.dbgate.io/img/rest-odata-query-light.png)

Les résultats sont affichés au format tabulaire, comme les résultats des requêtes de base de données.

## Authentification

Tous les types de connexions API prennent en charge plusieurs méthodes d'authentification :

- **Clé API** - indiquez le nom et la valeur de la clé, envoyée en en-tête ou en paramètre de requête
- **Bearer Token** - jetons OAuth ou JWT envoyés dans l'en-tête Authorization
- **Authentification Basic** - nom d'utilisateur et mot de passe via HTTP Basic Auth
- **Aucune authentification** - pour les API publiques

Configurez l'authentification dans les propriétés de la connexion.

## Export de données

Les données des réponses d'API peuvent être exportées vers différents formats en utilisant la fonctionnalité d'export standard de DbGate :
- JSON
- CSV
- Excel
- Instructions SQL INSERT
- XML

Utilisez l'option « Export » du menu contextuel standard dans l'explorateur de données tabulaires.

## Travailler avec plusieurs API

Vous pouvez créer des connexions vers plusieurs API et bases de données. Ouvrez plusieurs onglets de requête pour travailler simultanément avec différents points de terminaison.

L'état des onglets est conservé après la fermeture et la réouverture de l'application, et vous pouvez rouvrir une requête depuis l'historique des onglets fermés.
