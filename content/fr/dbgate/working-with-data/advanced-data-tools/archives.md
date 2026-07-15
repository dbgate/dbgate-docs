---
sourceHash: 80df2a73525118cee579014e200ff5f67715aa6f35468656abb3f8b70c254566
language: fr
title: Archives de données
weight: 1
---

Les archives sont des dossiers contenant des données au format JSONL (NDJSON). DbGate permet de travailler avec elles très efficacement : vous pouvez les importer dans une base de données, les exporter vers d'autres formats ou modifier directement les données dans l'archive. Une archive se comporte comme une base de données très rapide et légère stockée dans des fichiers locaux.

## Format JSONL
DbGate utilise le format JSONL en interne partout. JSONL est un fichier texte dont chaque ligne contient une ligne de données sérialisée en JSON. DbGate suppose que la première ligne peut contenir un en-tête (également au format JSON) avec la structure de la table. Lorsque vous utilisez JSONL avec une structure dynamique (sans première ligne fixe), ce format est standardisé et peut être chargé dans de nombreux autres outils.

## Dossiers d'archives
Une archive est organisée en dossiers contenant des fichiers JSONL. Elle a une structure similaire à celle d'une base de données. Vous pouvez ainsi exporter une base de données entière vers une nouvelle archive : chaque table est exportée dans un fichier JSON et, grâce à la ligne d'en-tête, la structure de la table est également conservée.

## Afficher et modifier les fichiers d'archive
Vous pouvez ouvrir les fichiers JSONL selon différents modes :
- menu contextuel « Ouvrir » - ouvre une grille de données qui permet de trier, filtrer et modifier vos données JSONL
- menu contextuel « Ouvrir dans l'éditeur de texte » - permet de modifier manuellement le fichier JSONL

## Archives et modèles de base de données
Les dossiers d'archives sont également utilisés comme stockage pour les modèles de base de données. Vous pouvez exporter un modèle de base de données depuis le menu contextuel de la base de données, « Exporter le modèle de base de données ». Vous pouvez ensuite modifier ce modèle (fichiers YAML pour la structure des tables, fichiers SQL pour les vues et les procédures stockées), le comparer avec la base de données réelle et le déployer dans la base de données
