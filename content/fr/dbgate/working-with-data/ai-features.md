---
sourceHash: 22f2bb33edfa72684bb05dbcccca0a7b4f618485c77b184b851a079c9a3b7aff
language: fr
title: Fonctionnalités IA
weight: 55
---

DbGate inclut plusieurs fonctionnalités basées sur l'IA *(Premium et Team Premium)*. Elles sont disponibles pour tous les utilisateurs Premium, sans clé API ni configuration - DbGate utilise sa propre passerelle IA, qui transmet les requêtes au fournisseur de LLM.

![Database chat](https://media.dbgate.io/img/database-chat-light.png)

## Chat de base de données

Le chat de base de données est un chatbot IA qui comprend à la fois le schéma de votre base de données et ses données.

* **Conversation naturelle** - posez des questions dans n'importe quelle langue naturelle et obtenez des réponses ou du SQL prêt à être exécuté.
* **Conscient du contexte** - le modèle connaît votre schéma et (avec votre autorisation) les données réelles, il suggère donc les jointures, filtres et agrégations corrects.
* **Itératif** - affinez avec des commandes comme « ajoute un filtre de date » ou « groupe par client » et la requête se met à jour instantanément.
* **Graphiques** - demandez un graphique à barres, circulaire ou linéaire construit à partir des résultats.
* **Mode consultant** - il peut analyser les procédures stockées et les vues, vous pouvez donc demander par exemple « Explique la procédure X » ou « Quelles tables sont affectées par la procédure Y ». DbGate indique quels objets ont été analysés.

### Exécution du SQL - la sécurité avant tout

Le chat de base de données peut exécuter du SQL pour répondre aux questions. Vous choisissez comment :

* **Demander avant d'exécuter le SQL (par défaut)** - DbGate demande confirmation avant d'exécuter chaque requête.
* **Exécuter le SQL automatiquement** - les requêtes autres que `SELECT` nécessitent quand même une confirmation.
* **Ne jamais exécuter, seulement suggérer le SQL** - le chat affiche uniquement les requêtes ; aucune donnée de votre base de données n'est envoyée au LLM.

Si une requête suggérée échoue, DbGate renvoie l'erreur au modèle, qui corrige généralement la requête automatiquement.

## Assistant SQL IA

Utilisez le chat comme assistant SQL - « Écris une requête SQL pour les 10 meilleurs clients par chiffre d'affaires » - et ouvrez le résultat dans un onglet [éditeur SQL](/fr/dbgate/sql-and-queries/sql-editor/).

## Expliquer une erreur SQL

Cliquez sur **Expliquer** à côté d'un message d'erreur pour obtenir une explication IA de ce qui s'est mal passé et de la façon de le corriger.

![Explain query error](https://media.dbgate.io/img/explain-query-error-light.png)

## Assistant IA de thèmes

L'IA peut également générer des thèmes de couleurs personnalisés - voir [Thèmes personnalisés](/fr/dbgate/customization/custom-themes/).

## Désactiver les fonctionnalités IA

Les fonctionnalités IA peuvent être entièrement désactivées (par exemple dans des environnements restreints) via les paramètres de DbGate.
