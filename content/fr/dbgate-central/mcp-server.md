---
sourceHash: a08152934c181f22217bbf815d79cc43332db1a6b54e7c67a8218d55a3ebc39c
language: fr
title: Serveur MCP pour les agents IA
weight: 50
---

DbGate Central peut exposer votre espace de travail à des assistants IA tels que [Claude](https://claude.ai) sous forme de connecteur **MCP (Model Context Protocol)** distant - un agent peut ainsi explorer et interroger vos API de la même manière que vous, avec un accès dont vous gardez le contrôle.

## Configuration

1. Ouvrez l'onglet **Settings** et créez un **profil MCP**. Copiez son **Server URL** (`https://central.dbgate.cloud/mcp/{profileId}`), son **Client ID** et son **Client Secret**.
2. Dans claude.ai (ou un autre client compatible MCP), ajoutez un connecteur personnalisé en utilisant cette URL et les identifiants OAuth.
3. Dans l'éditeur de chaque connexion, définissez son niveau d'**accès MCP** - **No access**, **Read-only** ou **Writable**. La valeur par défaut est aucun accès, donc rien n'est partagé tant que vous ne l'autorisez pas.
4. L'assistant exécute la négociation OAuth et vous donnez votre consentement, ce qui lie le connecteur à ce profil et à cet espace de travail.

Chaque espace de travail peut disposer de plusieurs profils MCP, chacun avec sa propre URL, ses identifiants et ses autorisations par connexion. L'authentification utilise OAuth 2.1 avec PKCE obligatoire, et les secrets client sont chiffrés au repos.

## Ce que l'agent peut faire

Disponible pour les connexions **oData**, **GraphQL** et **Shopify** (SQLite/DuckDB fonctionnent uniquement dans le navigateur et sont hors du périmètre MCP) :

* **Lister les connexions** que le profil est autorisé à utiliser.
* **Lister les entités** - tables, vues ou entités de catalogue.
* **Inspecter le schéma** - noms et types de colonnes.
* **Interroger les lignes** - filtrer, paginer et sélectionner des données.
* **Mettre à jour les lignes** - Shopify uniquement, et seulement si vous accordez l'accès Writable.

Comme les lectures et les écritures réutilisent le même moteur que la grille et le planificateur, un agent voit exactement les mêmes données et capacités que vous - jamais plus que l'accès que vous accordez.

![DbGate Central - MCP server for AI agents](https://lite.dbgate.io/screenshots/central-mcp-dark.png)
