---
sourceHash: ba49d4bd53c041c5e042d07318208cea17d32dd6c3079b21b9e4072bc94c457f
language: fr
title: Filtrage des données
weight: 10
---

DbGate dispose d'un moteur de filtrage de données puissant, permettant aussi bien un filtrage très simple que des conditions complexes.

Les filtres de données peuvent être utilisés à de nombreux endroits dans DbGate, mais l'endroit le plus courant est le filtrage de la grille de données.

![filter screenshot](https://media.dbgate.io/img/data-browser-filter-light.png)

Les filtres sont remplis avec un arrière-plan :
* Arrière-plan vert - le filtre est correct et est appliqué
* Arrière-plan rouge - il y a une erreur dans l'expression du filtre, le filtre est ignoré

Vous avez plusieurs possibilités pour créer un filtre :
* {{< mdi "filter" >}} - affiche un menu avec des filtres prédéfinis et des boîtes de dialogue
* {{< mdi "dots-vertical" >}} - vous permet de choisir les valeurs à filtrer
* Vous pouvez écrire le filtre directement - utilisez la syntaxe très simple décrite dans [filter-expressions](#filter-expressions)
* Ou vous pouvez créer le filtre avec des méthodes visuelles et le modifier manuellement

Autres commandes :
* {{< mdi "filter-off" >}} - efface tous les filtres

## Filter expressions
Les expressions de filtre sont conçues pour être intuitives, dans la plupart des cas, vous écrivez simplement directement ce que vous voulez rechercher. Cependant, la syntaxe est assez puissante, vous pouvez combiner plusieurs conditions et utiliser divers opérateurs.
La syntaxe des expressions dépend du type de données de la colonne.

### Exemples

| Type de colonne | Expression de filtre |  Description |
|----------|-------------|------|
| string | canada | la valeur de la colonne contient le texte "canada" |
| string | canada, usa | la valeur de la colonne contient le texte "canada" ou "usa" |
| string | canada lake | la valeur de la colonne contient le texte "canada" et "lake" |
| string | NOT EMPTY NOT NULL | la chaîne a une valeur non vide |
| number | >10 | la valeur de la colonne est supérieure à 10 |
| number | >=5 <=10 | la valeur de la colonne est comprise entre 5 et 10 |
| number | 1,2,3 | la valeur de la colonne est 1 ou 2 ou 3 |
| datetime | 2020-05-26 | la valeur de date est du 2020-05-26 (intervalle de 24 heures)  |

### Filtres communs (pour tous les types de données)
- NULL - la valeur de la colonne est null
- NOT NULL - la valeur de la colonne n'est pas null
- {$$ is null} - condition SQL, écrite entre accolades {}. $$ est l'espace réservé pour la colonne filtrée

### Filtres de texte
La comparaison de texte est insensible à la casse.
- text - la valeur de la colonne contient _text_. Peut être entre 'guillemets simples' ou "guillemets doubles"
- +text - la valeur de la colonne contient _text_ (identique à la ligne ci-dessus)
- ^text - la valeur de la colonne commence par _text_
- $text - la valeur de la colonne se termine par _text_
- !+text - la valeur de la colonne ne contient pas _text_ (identique à la ligne ci-dessus)
- !^text - la valeur de la colonne ne commence pas par _text_
- !$text - la valeur de la colonne ne se termine pas par _text_
- EMPTY - la valeur de la colonne ne contient aucun caractère non blanc
- NOT EMPTY - la valeur de la colonne contient un caractère non blanc

### Filtres numériques
- number - la valeur de la colonne est égale au nombre
- =number - la valeur de la colonne est égale au nombre
- !=number - la valeur de la colonne n'est pas égale au nombre
- <>number - la valeur de la colonne n'est pas égale au nombre
- <number - la valeur de la colonne est inférieure au nombre
- \>number - la valeur de la colonne est supérieure au nombre
- <=number - la valeur de la colonne est inférieure ou égale au nombre
- \>=number - la valeur de la colonne est supérieure ou égale au nombre

### Filtres de date et heure
- 2021 - année de la valeur de la colonne
- 2021-02 - année, mois de la valeur de la colonne
- 2021-02-15 - année, mois, jour de la valeur de la colonne
- 2021-02-15 23:15 - année, mois, jour, heure, minute de la valeur de la colonne
- 2021-02-15 23:15:51 - année, mois, jour, heure, minute, seconde de la valeur de la colonne
- Filtres relatifs à la date actuelle
  - YESTERDAY
  - TODAY
  - TOMORROW
  - LAST WEEK
  - THIS WEEK
  - NEXT WEEK
  - LAST MONTH
  - THIS MONTH
  - NEXT MONTH
  - LAST YEAR
  - THIS YEAR
  - NEXT YEAR

### Filtres logiques (booléens)
- TRUE, true, 1 - la valeur de la colonne est true/1
- FALSE, false, 0 - la valeur de la colonne est false/0

### Combinaisons de filtres
Les filtres peuvent être combinés entre eux. L'espace est interprété comme l'opérateur AND, la virgule comme l'opérateur OR. AND a une priorité plus élevée que OR.
