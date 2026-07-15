---
sourceHash: 9faead63589d3a58402650e29cd85afd2223ffa5317dbd506eb962c893c3c04e
language: fr
title: Comparer et déployer des modèles
weight: 15
---

DbGate peut comparer la structure d'une base de données et déployer les modifications *(Premium)*. C'est utile pour maintenir les environnements synchronisés et pour gérer le versionnage de votre schéma.

![Compare database](https://media.dbgate.io/img/compare-database-settings-light.png)

## Comparer des bases de données

* **Comparer deux bases de données** - trouver les différences dans les colonnes, les définitions de vues et les autres objets SQL.
* **Synchroniser la structure** - générer et exécuter les actions nécessaires pour qu'une base de données corresponde à une autre.
* **Comparer avec un modèle YAML** - comparer une base de données réelle avec un modèle stocké en YAML et déployer les différences.
* **Paramètres** - contrôler la comparaison, par exemple ignorer les clés étrangères, exclure des objets spécifiques ou choisir les actions de synchronisation à effectuer.

## Exporter un modèle de base de données

* **Générer dans un dossier** - enregistrer le modèle d'une base de données existante dans un dossier, ou dans un unique fichier JSON.
* **Fichiers YAML de tables** - les tables sont stockées sous forme de simples fichiers YAML que vous pouvez conserver dans un dépôt Git.
* **Fichiers de définition SQL** - les vues, les procédures stockées et les fonctions sont stockées sous forme de fichiers SQL.

## Déployer

Déployez le modèle visuellement avec l'outil de comparaison, ou depuis la ligne de commande dans le cadre d'un pipeline CI/CD. Pour le format des fichiers de modèle et le flux de travail en ligne de commande, voir [Déploiement de base de données](dbdeploy).

## Pages associées

* [Éditeur de tables et de schémas](schema-editor) - modifier la structure des tables via l'interface graphique
* [Déploiement de base de données](dbdeploy) - format des fichiers de modèle et déploiement en ligne de commande
