---
sourceHash: e10360d65315ca6bef22d826b37ec0f1623808453e37fd5d2a391f720399cc17
language: fr
title: Développement de plugins
weight: 30
---

DbGate prend en charge la création de plugins. Grâce à l'assistant de plugins, il est vraiment simple de créer un plugin de base. Les plugins DbGate sont des paquets NPM (JavaScript), ils peuvent avoir des dépendances. (mais pas de dépendances natives)

Il existe actuellement 3 types de plugins :
- Plugin de thème
- Plugin de format de fichier
- Plugin de pilote de base de données

## Installer les prérequis
Vous devez avoir [node.js](https://nodejs.org) installé.

Vous aurez également besoin de [Yeoman](https://yeoman.io/) et du [générateur de plugins DbGate](https://www.npmjs.com/package/generator-dbgate) pour yeoman :

```sh
npm install -g yo
npm install -g generator-dbgate
```

## Créer un plugin
Exécutez la commande suivante dans la console :

```sh
yo dbgate
```

Vous devez répondre à 3 questions :
- Le nom du plugin, il doit commencer par dbgate-plugin-, par ex. dbgate-plugin-myplugin
- Le type de plugin, choisissez par ex. « Database driver »
- Le gestionnaire de paquets, choisissez npm ou yarn, selon votre préférence. DbGate utilise yarn.

## Modifier et tester le plugin
Ouvrez un éditeur, l'option recommandée est [Visual Studio Code](https://code.visualstudio.com/)  .
Un plugin de thème ne contient qu'un seul fichier source, src/index.js. Vous pouvez modifier les couleurs du thème comme vous le souhaitez. L'attribut themeName est le nom affiché dans le sélecteur de thèmes de DbGate.

Lorsque vous voulez voir votre nouveau thème, exécutez ceci depuis la console (depuis le répertoire du plugin) :
```sh
yarn plugin
```
ou si vous utilisez npm, alors
```sh
npm run plugin
```
Cette commande installe votre plugin dans l'instance DbGate installée localement (ou le met à jour lorsque vous faites des modifications). Après le redémarrage de DbGate, vous devriez voir le nouveau thème.
Le redémarrage n'est pas nécessaire, il suffit de recharger l'application (menu View/Reload) pour utiliser la nouvelle version du plugin après avoir exécuté « yarn plugin »

## Supprimer un plugin
Vous pouvez désinstaller un plugin depuis le widget des plugins de DbGate. Ou en utilisant la commande suivante :
```sh
yarn plugout
```

## Publier un plugin
Un plugin est un paquet NPM normal, vous pouvez le publier dans le dépôt NPM. Après publication, il sera disponible pour tous les utilisateurs de DbGate dans le widget « Plugins ».

## Icône de plugin
Chaque plugin est représenté par une icône dans la liste des extensions. NPM ne prend pas en charge les icônes pour les paquets NPM, l'icône peut donc être placée dans le champ description du fichier package.json avec la syntaxe suivante :

```
    "description": "Any description ![icon](https://link_to_icon.svg)",
```

Si vous utilisez le générateur yeoman, il vous aidera un peu pour cela.

## Créer un plugin de pilote de base de données
La création d'un plugin de pilote est très similaire à la création, il suffit de sélectionner « Database driver plugin ». Après `yarn plugin`, vous devriez pouvoir définir une connexion en utilisant votre nouveau pilote et voir une liste de bases de données et une liste de tables factices.

Vous pouvez créer très rapidement un pilote simple avec des fonctionnalités de base, les fonctionnalités plus complexes peuvent être implémentées plus tard.

La création d'un pilote peut se composer des étapes suivantes :
* trouver un paquet nodejs (pilote) approprié. Choisissez si possible un paquet en JavaScript pur. Les paquets natifs sont une grande complication, ce paquet natif doit être ajouté à la distribution DbGate, et vous pouvez également vous attendre à des problèmes de compilation sur différentes plateformes. En revanche, les paquets en JavaScript pur fonctionnent normalement sans problème sur toutes les plateformes, sans nécessiter de modification de DbGate.
* définir les champs de connexion dans frontend/driver.js, fonction showConnectionField
* implémenter la fonction connect dans backend/driver.js
* implémenter la fonction getVersion dans backend/driver.js (optionnel, mais une fois fait, vous pouvez tester la connexion avec le bouton « Test » dans l'onglet de connexion)
* implémenter la méthode _rynAnalysis dans la classe backend/Analyser.js. Cette méthode doit retourner la structure de la base de données.
* implémenter la méthode query dans backend/driver.js. Après cela, vous devriez pouvoir voir la liste des tables et parcourir les données des tables
* implémenter les autres méthodes. Veuillez vous inspirer des autres plugins de pilotes, le plugin le plus typique est probablement le plugin PostgreSQL, https://github.com/dbgate/dbgate/tree/master/plugins/dbgate-plugin-postgres
