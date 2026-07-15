---
sourceHash: 5e47867df26e6f347a8126762b620b430051ec272991c8832bb180423abcd8cc
language: fr
title: Graphiques
weight: 30
---

Avec DbGate, vous pouvez utiliser un graphique pour visualiser vos requêtes SQL. Exécutez simplement la requête, si un graphique est détecté automatiquement, l'onglet « Chart 1 » apparaîtra. Si vous avez plusieurs résultats de requête, il peut y avoir plusieurs graphiques.

Si aucun graphique n'est détecté automatiquement, mais que vous souhaitez créer un graphique à partir des résultats de votre requête, faites un clic droit sur les données du résultat de la requête et choisissez « Open chart ».

![Capture d'écran du graphique](https://media.dbgate.io/img/query-result-chart-light.png)

## Paramètres du graphique
Utilisez le bouton {{< mdi "pencil" >}} Customize pour ouvrir les paramètres du graphique. Vous pouvez configurer la source de données et le style du graphique :
* Type de graphique
  * Bar (barres)
  * Line (courbe)
  * Timeline (chronologie) - c'est un cas particulier du graphique en courbe, avec le temps sur l'axe X
  * Pie (secteurs)
  * Polar area (aire polaire)
* Champ de l'axe X - données sur l'axe X. Pour les valeurs de type date/heure, des fonctions de regroupement et de chronologie sont disponibles
* Champ de regroupement - définit plusieurs graphiques déterminés par la valeur de ce champ
* Transformation de l'axe X - permet de définir un regroupement pour la chronologie de l'axe X (par ex. par année ou par mois)
* Champ N de l'axe Y - vous pouvez avoir plusieurs champs sur l'axe Y
  * Un champ spécial est disponible pour chaque jeu de données, « Count », qui compte les lignes
* Fonction d'agrégation - Sum, Minimum, Maximum, Average, First Value, Last Value

Lorsque vous modifiez une option dans les paramètres du graphique, elle est enregistrée au début du script SQL sous forme de front-matter.

## Modification manuelle de la définition du graphique
Certaines options ne sont pas disponibles dans l'éditeur, mais elles peuvent être modifiées dans le code SQL. Veuillez lire [SQL front matter](/fr/dbgate/developer/sql-front-matter) pour plus d'informations
