---
sourceHash: 3dab8886ac4d4e94fd5a5f1cfcbccab5e941b303d64e8ba9fc96bc2ee264040b
language: fr
title: Navigateur et éditeur de données
weight: 5
---

Le navigateur de données est la vue centrale de DbGate pour consulter et modifier les données des tables. Ouvrez n'importe quelle table, vue ou collection pour obtenir une grille rapide, de type Excel. Cette page couvre la navigation, l'édition et le parcours des données liées ; pour les expressions de filtrage, voir [Filtrage des données](data-filtering).

![Data browser](https://media.dbgate.io/img/common-data-browser-light.png)

## Navigation dans les données

* **Navigation au clavier** - déplacez-vous dans la grille avec les touches fléchées, comme dans un tableur.
* **Tri** - cliquez sur un en-tête de colonne pour trier selon cette colonne.
* **Filtre** - filtrez les lignes à l'aide de la ligne de filtre située au-dessus de la grille ; voir [Filtrage des données](data-filtering) pour la syntaxe complète des expressions.
* **Gestionnaire de colonnes** - retrouvez les colonnes par leur nom et masquez celles dont vous n'avez pas besoin.
* **Copie avancée** - copiez les cellules sélectionnées au format CSV, YAML, `INSERT` SQL ou insertions MongoDB.

## Édition des données

L'édition des données se fait directement dans la grille :

* **Édition de type Excel** - modifiez les cellules sur place ; copiez et collez des plages de lignes, y compris d'une table à l'autre.
* **Modifications en attente** - vos modifications sont regroupées sous forme de changements en attente. Vérifiez le script SQL de modification généré avant qu'il n'affecte la base de données, puis enregistrez-le ou annulez-le.
* **Insertion et suppression de lignes** depuis la grille ou le menu contextuel.

![Save changes](https://media.dbgate.io/img/data-browser-save-changes-light.png)

### Macros de l'éditeur de données *(Premium)*

Appliquez des macros prédéfinies aux cellules sélectionnées - par exemple changer la casse du texte, supprimer les diacritiques ou générer un UUID.

## Travailler avec les données liées

DbGate facilite le suivi des relations entre les tables :

* **Indications de relation** - affichez une valeur textuelle de la table référencée à côté d'une clé étrangère numérique.
* **Expansion des colonnes de clé étrangère** - développez une colonne de clé étrangère pour afficher les données référencées en ligne.
* **Ouvrir le détail** - accédez directement à la ligne référencée par une clé étrangère.
* **Vues maître/détail** *(Premium)* - explorez les lignes liées dans une disposition maître/détail connectée.

![Master/detail](https://media.dbgate.io/img/data-browser-master-detail-light.png)

## Vue formulaire

La vue formulaire affiche une seule ligne sous forme de liste verticale « transposée » - idéale pour les tables comportant de nombreuses colonnes. Elle fonctionne comme une vue arborescente : les colonnes de clé étrangère peuvent donc être développées pour explorer les données liées.

![Form view](https://media.dbgate.io/img/data-browser-form-view-light.png)

## Regroupement *(Premium)*

Appliquez un regroupement (`GROUP BY`) dans la vue grille pour agréger les lignes directement pendant la navigation.

## Pages associées

* [Filtrage des données](data-filtering) - syntaxe des expressions de filtrage
* [Export et import](export-import) - transférez des données vers et depuis les tables
* [Perspectives](perspectives) - vues imbriquées en lecture seule sur des données liées complexes
* [Éditeur SQL](/fr/dbgate/sql-and-queries/sql-editor/) - modifiez les résultats de requête de la même manière *(Premium)*
