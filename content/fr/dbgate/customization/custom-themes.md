---
sourceHash: f2791f82e04437cfea34f20ce37c68c887e87a2c0da52d28b9f823e0e184aab9
language: fr
title: Thèmes personnalisés
weight: 10
---

DbGate offre une prise en charge flexible des thèmes. Vous pouvez créer votre propre thème en modifiant les couleurs des différents éléments de l'interface.

Les thèmes sont créés sous forme de fichiers JSON. Le moyen le plus simple de créer un thème personnalisé est d'utiliser l'assistant IA de thèmes.

## Assistant IA de thèmes
Pour appeler l'assistant IA de thèmes, ouvrez Paramètres/Thèmes, puis cliquez sur le bouton « Customize with AI assistant ».

![Theme settings](https://media.dbgate.io/img/app-settings-themes-light.png)

L'assistant IA de thèmes personnalisera votre thème selon vos instructions. Vous pouvez indiquer quelles couleurs vous souhaitez modifier, et comment. Par exemple, vous pouvez dire « Rends la couleur principale verte et la couleur d'arrière-plan gris foncé ».

![screenshot](/screenshots/dbgate-green.png)

La génération d'un thème avec l'assistant IA prend quelques minutes, car environ 280 variables doivent être générées. Une fois le thème généré, vous pouvez cliquer sur le bouton « Apply Theme » pour utiliser le nouveau thème. Vous pouvez également utiliser le bouton « Save theme » pour enregistrer le thème dans un fichier JSON. Tous les thèmes enregistrés sont ensuite disponibles dans le sélecteur de thèmes. Vous pouvez aussi gérer (renommer, modifier, supprimer) les thèmes dans le widget des fichiers {{< mdi "file" >}}.

## Partage de thèmes dans DbGate Cloud
Vous pouvez partager vos thèmes avec d'autres utilisateurs de DbGate via DbGate Cloud. Pour partager un thème, créez une pull request dans le [dépôt de la base de connaissances DbGate](https://github.com/dbgate/dbgate-knowledge-base). Les thèmes sont stockés dans le répertoire folder-Themes. Consultez les thèmes existants pour des exemples. Copiez simplement votre fichier JSON de thème dans ce répertoire et créez une pull request. Une fois votre pull request fusionnée, votre thème sera disponible pour tous les utilisateurs de DbGate dans le sélecteur de thèmes.
