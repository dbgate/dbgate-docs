---
sourceHash: 0f10d627c0492363d84834c24da993d0686916c833728726a2d34648885161b1
language: fr
title: Éditeur de tables et de schémas
weight: 5
---

DbGate peut créer et modifier la structure d'une base de données via une interface graphique, sans écrire de DDL à la main. Ouvrez l'éditeur de structure d'une table depuis son menu contextuel (« Modifier la table »), ou créez une nouvelle table depuis le menu contextuel de la base de données.

![Table structure editor](https://media.dbgate.io/img/table-structure-editor-light.png)

## Modification des tables

* **Colonnes et types de données** - définissez les colonnes, les types de données, la nullabilité et les valeurs par défaut pour les tables nouvelles ou existantes.
* **Clés et index** - gérez les clés primaires, les clés étrangères et les index.
* **Propriétés spécifiques au moteur** - définissez des options propres à la base de données, comme le moteur de table MySQL.

## Aperçu SQL et modifications sûres

* **Aperçu SQL** - avant tout enregistrement, DbGate affiche le SQL généré afin que vous puissiez le vérifier.
* **Avertissement de recréation de table** - lorsqu'une modification nécessite de recréer la table (une limitation de certaines bases de données), DbGate vous avertit et vous permet d'inspecter d'abord le script généré.

## Autres objets de base de données

Vous pouvez également créer, supprimer et modifier d'autres objets - vues, procédures stockées et fonctions - et parcourir les tables, vues, procédures, fonctions et collections MongoDB depuis l'arborescence des objets.

## Pages associées

* [Comparer et déployer des modèles](model-compare-deploy) - comparez la structure entre bases de données et déployez les modifications *(Premium)*
* [Déploiement de base de données](dbdeploy) - fichiers de modèle YAML/SQL et déploiement en ligne de commande
