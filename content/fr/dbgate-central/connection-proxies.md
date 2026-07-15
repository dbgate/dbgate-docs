---
sourceHash: da9ffbf5e9249c4fa1b2604052996a7d624acf51bed34304c0aa4ca3bf9ab0d4
language: fr
title: Proxys de connexion
weight: 60
---

DbGate Central peut atteindre des API oData et GraphQL situées sur un réseau privé en acheminant leur trafic via un petit agent sortant que vous exécutez à l'intérieur de ce réseau. Les connexions Shopify et OpenAPI ne peuvent pas être proxifiées.

## Configuration d'un proxy

1. Ouvrez l'onglet **Paramètres** et créez un **proxy** sous *Proxys de connexion*. Copiez le jeton généré.
2. Cochez les connexions oData/GraphQL que le proxy peut desservir. Chaque modification régénère le jeton, redémarrez donc l'agent après avoir changé la sélection.
3. Exécutez l'agent à l'intérieur de votre réseau privé :
   ```sh
   npx dbgate-central-proxy --token <token>
   ```
   L'agent n'établit que des connexions sortantes - aucun accès entrant à votre réseau n'est requis.
4. Une fois l'agent en cours d'exécution et connecté, les requêtes vers les connexions proxifiées sont acheminées par son intermédiaire. Si le proxy n'est pas connecté, DbGate Central revient à une récupération directe.

Le même routage s'applique également au [serveur MCP](../mcp-server) : lorsqu'un outil MCP lit une connexion proxifiée, la requête passe par le même proxy.
