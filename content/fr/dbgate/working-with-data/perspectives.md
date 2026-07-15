---
sourceHash: c4524af52346052c42b28b4771f78e2c49809f07b0e8cb293f1b38112577855b
language: fr
title: Perspectives
weight: 50
---

Une perspective est une vue en lecture seule de données imbriquées complexes. Elle ressemble à un rapport, mais les perspectives se créent simplement en ajoutant des données à la vue. Vous pouvez utiliser le concepteur de perspectives, qui permet de joindre des données en suivant d'autres relations que les clés étrangères.

Les perspectives permettent de joindre facilement des données entre elles et d'afficher des groupes.

<!-- ![screenshot](/screenshots/perspective1.png) -->

## Créer une perspective
Les perspectives peuvent être créées à partir de tables et de vues SQL (les collections MongoDB ne sont pas encore prises en charge, mais cette prise en charge est prévue).
Utilisez le menu contextuel de la table ou de la vue, « Open perspective ».

![screenshot](/img/perspective-create.png)

DbGate ouvre une perspective simple, avec une seule colonne affichée. Cette colonne est choisie par un algorithme heuristique, afin d'être la meilleure représentation possible de la ligne entière.
## Personnaliser la perspective
Vous pouvez définir quelles colonnes sont disponibles dans la vue. Vous pouvez également ajouter des données référencées à la vue. Utilisez le bouton d'expansion pour parcourir l'arborescence des références.

## Filtrer les données
Utilisez le menu contextuel dans la table ou dans la liste des colonnes sur le côté gauche, « Add to filter ». Vous pouvez utiliser les mêmes expressions de filtre que dans les autres parties de DbGate. Vous pouvez aussi utiliser la commande du menu contextuel « Filter this value » sur une cellule de la table.

## Filtrer les lignes parentes
Prenons la perspective suivante. Nous avons une relation maître/détail, Genre, avec les pistes associées. Nous voulons filtrer par Track (j'ai essayé de rechercher le texte « mix »).

![screenshot](/img/parentrows1.png)

Comme vous pouvez le constater, il y a beaucoup de lignes Genre sans aucune piste correspondant aux critères de recherche. Si vous souhaitez filtrer également les lignes Genre, utilisez la commande « Filter parent rows » dans le menu contextuel de l'en-tête de table. Vous pouvez aussi utiliser le bouton bascule dans la ligne de filtre.

![screenshot](/img/parentrows2.png)

## Définir des jointures personnalisées
Les perspectives fonctionnent très bien avec les clés étrangères. Mais même lorsque vous avez une base de données sans clés étrangères, vous pouvez utiliser cette fonctionnalité. Il est possible de définir une jointure personnalisée avec n'importe quelle condition. Vous pouvez même définir une jointure personnalisée vers une autre base de données (qui peut se trouver sur un serveur de base de données différent, voire avec un moteur de base de données sous-jacent différent).

![screenshot](/img/customjoin.png)

Vous pouvez également glisser-déposer des colonnes pour créer une relation de jointure.

![screenshot](/img/customjoin2.png)
