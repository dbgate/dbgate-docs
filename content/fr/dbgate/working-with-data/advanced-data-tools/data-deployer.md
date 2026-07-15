---
sourceHash: 813897622368b4a3dc176bd6e81b91d11c78d140ebe8055d76beb033560861d6
language: fr
title: Déployeur de données
weight: 2
---

Avec le déployeur de données, vous pouvez comparer et synchroniser visuellement vos données situées dans des **dossiers d'archive** avec une **base de données réelle**
![DbGate data duplicator screenshot](https://media.dbgate.io/img/data-deployer-light.png)

## Lancer le déployeur de données
Vous pouvez lancer le déployeur de données depuis le menu contextuel d'une base de données ou depuis le menu contextuel d'un dossier d'archive. Lors du lancement depuis une base de données, il vous sera demandé de choisir une archive. Lors du lancement depuis une archive, le déployeur de données démarrera avec la base de données courante.

## Paramètres
- Serveur de base de données, base de données - choisissez la base de données avec laquelle travailler
- Archive de données - choisissez le dossier contenant les données qui seront utilisées pour la comparaison et la synchronisation
### Relatif à la table
- Clé (colonnes de correspondance) - choisissez les colonnes qui seront utilisées pour faire correspondre les lignes entre la base de données et l'archive
### Paramètres du réplicateur
Les paramètres ci-dessous (« table » - déploiement et paramètres globaux de déploiement de données) sont spécifiques au réplicateur et sont décrits dans la rubrique [Réplicateur de données](data-replicator)

## Copier les différences de données
Le déployeur de données affiche les différences entre les données de l'archive et celles de la base de données. Si vous sélectionnez des cellules présentant une différence, vous pouvez écrire ces différences dans l'archive ou dans la base de données. Lorsque ces cellules sont sélectionnées, des boutons permettant la synchronisation apparaissent dans le coin inférieur droit :
- Écrire x lignes, y colonnes dans l'archive - copie les cellules sélectionnées de la base de données vers l'archive.
- Écrire x lignes, y colonnes dans la base de données - copie les cellules sélectionnées de l'archive vers la base de données. Une boîte de dialogue de confirmation affichant le SQL de modification est présentée au préalable.

## Actions du réplicateur de données
- Déployer dans la BD - cette action déploie les modifications dans la base de données avec les paramètres configurés
- Générer un shell - cette action crée un fichier JavaScript qui exécutera le déploiement. Ce fichier peut être lancé depuis la ligne de commande
- Générer le SQL - crée le SQL qui déploie les modifications de l'archive vers la base de données

Plus d'informations sur ces actions dans la rubrique [Réplicateur de données](data-replicator)
