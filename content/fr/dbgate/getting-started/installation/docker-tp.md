---
sourceHash: 1565401b5cbe564d5dea5c98e8e060786cb30e1952808c41e0a5542a29f3ef42
language: fr
title: Team Premium sur Docker
weight: 30
---

Une installation typique de Team Premium se compose de deux composants :
- Le conteneur Docker du serveur DbGate
- Un serveur de base de données (MS SQL, MySQL, PostgreSQL, Oracle) - base de données de stockage interne pour les connexions, les utilisateurs et les rôles. Vous pouvez utiliser un serveur de base de données existant ou en installer un nouveau.

## Conteneur Docker du serveur DbGate
Utilisez l'[image DbGate Team Premium](https://hub.docker.com/r/dbgate/dbgate-premium) depuis Docker Hub :
```
docker pull dbgate/dbgate-premium
```

Le conteneur DbGate Team Premium nécessite la définition de certaines variables d'environnement :
- `STORAGE_SERVER`, `STORAGE_DATABASE`, `STORAGE_USER`, `STORAGE_PASSWORD`, `STORAGE_ENGINE` - définissent la connexion à la base de données de stockage interne

Consultez la [documentation des variables d'environnement](/fr/dbgate/customization/env-variables/#team-premium-edition-configuration) pour plus de détails sur les variables d'environnement disponibles.

## Ressources requises

En réalité, DbGate Team Premium consomme très peu de ressources, mais pour des performances optimales nous recommandons la configuration suivante (pour 10 utilisateurs simultanés) :
- 2 cœurs CPU
- 4 Go de RAM (inclut la consommation de RAM de la base de données de stockage interne MySQL ou PostgreSQL)
- 10 Go d'espace disque libre (pour l'installation Docker, la base de données de stockage, les fichiers temporaires, les résultats de requêtes, etc. La consommation réelle d'espace disque dépend des usages)

Pour un nombre d'utilisateurs plus faible, vous pouvez utiliser des limites de ressources inférieures (1 Go de RAM, 1 cœur CPU).  
Lorsque vous devez minimiser la consommation de ressources pour de petites installations, nous recommandons d'utiliser MySQL/MariaDB comme stockage interne.  

## Configuration de Docker

Si vous souhaitez utiliser des fichiers sur disque pour le stockage des fichiers utilisateur (comme l'export des résultats de requêtes), vous devez mapper le chemin `/root/.dbgate` dans le conteneur.

Vous trouverez ci-dessous un exemple de fichier `docker-compose.yml`, définissant un conteneur DbGate Team Premium avec PostgreSQL comme base de données de stockage interne.
- Vous pouvez définir la variable d'environnement `DBGATE_LICENSE` pour définir la clé de licence. Si elle n'est pas définie, DbGate demandera la clé de licence au premier démarrage.
-  Vous pouvez définir la variable d'environnement 'ADMIN_PASSWORD' pour définir le mot de passe de l'utilisateur admin. Si elle n'est pas définie, DbGate demandera le mot de passe admin au premier démarrage.

```yaml
version: '3'
services:
  dbgate:
    image: dbgate/dbgate-premium
    restart: always
    ports:
      - 80:3000
    environment:
      STORAGE_SERVER: postgres_service
      STORAGE_USER: postgres
      STORAGE_PASSWORD: XXXStoragePwd
      STORAGE_PORT: 5432
      STORAGE_DATABASE: dbgate
      STORAGE_ENGINE: postgres@dbgate-plugin-postgres
      STORAGE_SCHEMA: public
    volumes:
      - dbgate_data:/root/.dbgate

  postgres_service:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: XXXStoragePwd
      POSTGRES_DB: dbgate
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
    postgres_data:
      driver: local
    dbgate_data:
      driver: local
```

## Sans état / Avec état
Le conteneur DbGate est avec état (statefull).

Les données suivantes sont stockées à l'intérieur du conteneur :
* Sessions des utilisateurs connectés
* États d'exécution des requêtes
* Fichiers temporaires (comme les résultats)
* Transactions de base de données ouvertes
* Connexions de base de données ouvertes

Il n'est pas possible d'exécuter correctement plusieurs conteneurs DbGate derrière un répartiteur de charge, car les données ci-dessus ne sont pas partagées entre les conteneurs.

## Serveur DbGate depuis NPM
Si votre infrastructure ne prend pas en charge Docker, vous pouvez utiliser le [paquet NPM DbGate Team Premium](https://www.npmjs.com/package/dbgate-serve-premium) :
```
npm install -g dbgate-serve-premium
```
 
## Isolation des processus
DbGate Team Premium utilise l'isolation des processus au niveau de la connexion à la base de données, afin que plusieurs utilisateurs puissent utiliser le même serveur de base de données sans interférence. Le processus dérivé de DbGate croît avec le nombre d'utilisateurs et de connexions actifs, veillez donc à ce que votre serveur dispose de ressources suffisantes.
Les entités suivantes sont isolées dans un nouveau processus :
* Connexions au serveur
* Connexions aux bases de données
* Sessions de requêtes
* Exécution des tâches d'export/import
* Tunnels SSH
