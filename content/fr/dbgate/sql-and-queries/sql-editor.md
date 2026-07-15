---
sourceHash: 12c8ac4efdd1d8c03e7c029deb726b52281b6dba121709c45f621f4c4eca3710
language: fr
title: Éditeur SQL
weight: 10
---

L'éditeur SQL est l'endroit où vous écrivez et exécutez des scripts SQL sur votre connexion. Ouvrez-le depuis le bouton {{< mdi "flash" >}} « Nouvelle requête » de la barre d'outils, ou depuis le menu contextuel d'une connexion ou d'une base de données.

![SQL editor](https://media.dbgate.io/img/common-data-browser-light.png)

## Exécution de SQL

* **Exécuter le script** - exécute l'ensemble du script à l'aide du bouton {{< mdi "play" >}} Exécuter (ou F5).
* **Exécuter l'instruction courante** - exécute uniquement l'instruction située sous le curseur.
* **Exécuter la sélection** - si vous sélectionnez une partie du script, seul le texte sélectionné est exécuté.
* Les résultats apparaissent dans la grille de résultats sous l'éditeur. Les jeux de résultats multiples sont affichés dans des onglets distincts.
* Les messages, le nombre de lignes et les erreurs sont affichés dans l'onglet **Messages**.

## Aides à l'édition

* **Formateur de code SQL** - reformate le script courant pour une indentation et une casse cohérentes.
* **Complétion de code** - suggestions de tables, de colonnes et de mots-clés basées sur le schéma de la base de données connectée.
* **Assistant de jointure** - l'utilitaire « Add SQL join » génère une clause `LEFT`/`INNER`/`RIGHT JOIN` à partir des clés étrangères, ce qui vous évite de saisir les conditions de jointure à la main.

## Utilisation des résultats

La grille de résultats utilise le même moteur que le [navigateur de données](/fr/dbgate/working-with-data/data-browser/), vous pouvez donc [filtrer et trier](/fr/dbgate/working-with-data/data-filtering/), copier des cellules dans différents formats et [exporter](/fr/dbgate/working-with-data/export-import/) le résultat.

### Modification des résultats de requête et des vues *(Premium)*

Les résultats de requête sont modifiables lorsque DbGate peut faire correspondre le résultat à une seule table ou à une vue actualisable. Modifiez les cellules directement dans la grille de résultats, examinez le script de modification généré et enregistrez-le dans la base de données - le même flux de travail de modifications en attente que dans le [navigateur de données](/fr/dbgate/working-with-data/data-browser/). La modification des vues est également prise en charge.

> Les résultats de requête modifiables et les vues modifiables ont été introduits dans DbGate 7.2.

## Contrôle des transactions

Vous pouvez contrôler les transactions depuis l'éditeur - exécuter à l'intérieur d'une transaction explicite et valider ou annuler les modifications, ce qui est utile lors du test de scripts modifiant des données.

## Autres éditeurs

* **Éditeur JavaScript Mongo** - pour les connexions MongoDB, écrivez et exécutez des scripts Mongo en utilisant la syntaxe NodeJS.
* **Redis** - parcourez l'arborescence des clés Redis, générez un script à partir des clés sélectionnées et exécutez des scripts Redis.
