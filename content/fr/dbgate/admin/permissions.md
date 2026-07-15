---
sourceHash: 0086e005ede5ab2d89ada748f23fbb27b453941fb9b7bec1159e8683ce1ee803
language: fr
title: Permissions
weight: 50
---

Les permissions de DbGate reposent sur **deux dimensions** :

1. **Source des permissions (qui les définit)**
   Les permissions se propagent du général au spécifique. Les réglages plus spécifiques prévalent sur les plus généraux :
   * Ensembles de permissions prédéfinis
   * Rôles prédéfinis (*superadmin*, *utilisateur connecté*, *anonyme*)
   * Rôles personnalisés
   * Utilisateur individuel

2. **Portée des objets**
   Les permissions peuvent cibler des **bases de données** et des **tables/objets** spécifiques. Voir **[Permissions de base de données](#database-permissions)** et **[Permissions de table](#table-permissions)**.

---

## Permissions de base

Configurez les permissions globales/de base dans l’**arborescence des permissions** dans le **détail de l’utilisateur** ou le **détail du rôle**.

* Une case à cocher **grisée** signifie que la permission est **héritée** (par exemple d’un rôle ou d’un ensemble de permissions prédéfini), et non définie directement sur cet utilisateur/rôle.

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

---

## Permissions de base de données

Définissez les permissions au niveau de la base de données dans l’onglet **Databases** (à la fois dans le détail du rôle et le détail de l’utilisateur).

> **Important :** les règles de base de données ne s’appliquent **que si** la permission **« All databases »** est décochée dans les permissions de base.

* Chaque ligne du tableau de règles autorise ou refuse l’accès aux bases de données qui **correspondent** aux filtres de la ligne.
* **L’ordre des règles est important** : les règles situées **plus bas** dans la liste **prévalent** sur celles situées au-dessus.

![Database permissions - DbGate](https://media.dbgate.io/img/database-permissions-light.png)

**Colonnes**

* **Connection** – la connexion à laquelle la règle s’applique.
* **Database names** – les bases de données à faire correspondre (liste de noms ou expression régulière).
* **Role (niveau d’accès)**
  * **View** – peut voir la base de données, mais pas ses tables/vues/etc.
  * **Read content** – accès en lecture seule au contenu de la base de données.
  * **Write data** – peut modifier les données des tables.
  * **Run script** – peut exécuter n’importe quel script SQL ; peut créer/supprimer/modifier des objets.
  * **Deny** – bloque l’accès à la base de données.

---

## Permissions de table

Définissez les permissions au niveau des tables/objets dans l’onglet **Tables / Views / Objects** (dans le détail du rôle et le détail de l’utilisateur).

> **Important :** les règles de table/objet ne s’appliquent **que si** la permission **« All tables/views/objects »** est décochée dans les permissions de base.

* Chaque ligne définit l’accès aux tables/objets qui **correspondent** aux filtres.
* **L’ordre des règles est important** : les règles situées **plus bas** dans la liste **prévalent** sur celles situées au-dessus.
* Par défaut, les permissions de table sont **héritées de la permission de base de données**.

**Colonnes**

* **Connection** – la connexion à laquelle la règle s’applique.
* **Database names** – les bases de données à faire correspondre (liste ou expression régulière).
* **Schema names** – les schémas à faire correspondre (liste ou expression régulière).
* **Table names** – les noms d’objets à faire correspondre (table/vue/procédure/déclencheur) sous forme de liste ou d’expression régulière.
* **Scope** – les types d’objets couverts par la règle (tables, vues, procédures, déclencheurs, …).
* **Role (niveau d’accès)**
  * **Read** – peut lire les données de la table.
  * **Update only** – peut mettre à jour les lignes ; l’**insertion** et la **suppression** ne sont pas autorisées.
  * **Create, update, delete** - peut modifier les lignes sans restrictions
  * **Run script** – peut exécuter un script qui touche cet objet.
    > Remarque : si vous **n’avez pas** la permission **« Run script »** au niveau de la **base de données**, vous ne pouvez pas l’utiliser au niveau de la table.
  * **Deny** – bloque l’accès à l’objet.

