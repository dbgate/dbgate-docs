---
sourceHash: a1e2c8e626b7d397e242c5a182c920ca58971109a164a8c90e909a521a92e5db
language: fr
title: Cartes
weight: 40
---

DbGate permet d'afficher des données géographiques sur des cartes.

## Sources de cartes prises en charge
- MySQL : toutes les colonnes spatiales
- MSSQL : colonnes GEOGRAPHY
- PostGIS : colonnes GEOGRAPHY
- Toutes les sources de données : coordonnées stockées dans des colonnes de latitude/longitude

## Ouvrir la vue carte
La vue carte s'ouvre depuis la grille de données. Sélectionnez d'abord les cellules contenant les données géographiques souhaitées. Le plus simple est de sélectionner une cellule GEOGRAPHY ou GEOMETRY. Vous pouvez également sélectionner plusieurs lignes. Cliquez ensuite sur le widget Données de la cellule. La carte devrait apparaître dans le widget Données de la cellule.

![screenshot](/img/map1.png)

Lorsque vous disposez de colonnes de latitude et de longitude, sélectionnez toutes les données que vous souhaitez afficher sur la carte. Les colonnes autres que la latitude ou la longitude seront affichées dans les fenêtres contextuelles des marqueurs.

![screenshot](/img/map2.png)

Vous pouvez également utiliser le menu contextuel « Open selection in map » de la grille de données sur les cellules sélectionnées ; un nouvel onglet contenant la carte s'ouvrira alors.

Le menu contextuel de la carte offre également la possibilité d'exporter la carte dans un fichier HTML autonome, qui peut être affiché partout, même là où DbGate n'est pas installé.
