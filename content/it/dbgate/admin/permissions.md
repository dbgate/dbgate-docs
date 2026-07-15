---
sourceHash: 0086e005ede5ab2d89ada748f23fbb27b453941fb9b7bec1159e8683ce1ee803
language: it
title: Autorizzazioni
weight: 50
---

Le autorizzazioni di DbGate utilizzano **due dimensioni**:

1. **Origine delle autorizzazioni (chi le imposta)**
   Le autorizzazioni si propagano dal livello generale a quello specifico. Le impostazioni più specifiche prevalgono su quelle più generali:
   * Set di autorizzazioni predefiniti
   * Ruoli predefiniti (*superadmin*, *logged user*, *anonymous*)
   * Ruoli personalizzati
   * Singolo utente

2. **Ambito degli oggetti**
   Le autorizzazioni possono riguardare **database** e **tabelle/oggetti** specifici. Vedi **[Autorizzazioni sui database](#database-permissions)** e **[Autorizzazioni sulle tabelle](#table-permissions)**.

---

## Autorizzazioni di base

Configura le autorizzazioni globali/di base nell'**albero delle autorizzazioni** nel **dettaglio utente** o nel **dettaglio ruolo**.

* Una casella di controllo **grigia** indica che l'autorizzazione è **ereditata** (ad esempio, da un ruolo o da un set di autorizzazioni predefinito) e non impostata direttamente su quell'utente/ruolo.

![Role administration - DbGate](https://media.dbgate.io/img/user-administration-light.png)

---

## Autorizzazioni sui database

Imposta le autorizzazioni a livello di database nella scheda **Databases** (sia nel dettaglio ruolo sia nel dettaglio utente).

> **Importante:** le regole sui database vengono applicate **solo se** l'autorizzazione **"All databases"** è deselezionata nelle autorizzazioni di base.

* Ogni riga della tabella delle regole concede o nega l'accesso ai database che **corrispondono** ai filtri della riga.
* **L'ordine delle regole è importante**: le regole più **in basso** nell'elenco **prevalgono** su quelle sopra di esse.

![Database permissions - DbGate](https://media.dbgate.io/img/database-permissions-light.png)

**Colonne**

* **Connection** – a quale connessione si applica la regola.
* **Database names** – i database da confrontare (elenco di nomi o espressione regolare).
* **Role (livello di accesso)**
  * **View** – può vedere il database, ma non le sue tabelle/viste/ecc.
  * **Read content** – accesso in sola lettura al contenuto del database.
  * **Write data** – può modificare i dati delle tabelle.
  * **Run script** – può eseguire qualsiasi script SQL; può creare/eliminare/modificare oggetti.
  * **Deny** – blocca l'accesso al database.

---

## Autorizzazioni sulle tabelle

Imposta le autorizzazioni a livello di tabella/oggetto nella scheda **Tables / Views / Objects** (nel dettaglio ruolo e nel dettaglio utente).

> **Importante:** le regole su tabelle/oggetti vengono applicate **solo se** l'autorizzazione **"All tables/views/objects"** è deselezionata nelle autorizzazioni di base.

* Ogni riga definisce l'accesso alle tabelle/agli oggetti che **corrispondono** ai filtri.
* **L'ordine delle regole è importante**: le regole più **in basso** nell'elenco **prevalgono** su quelle sopra di esse.
* Per impostazione predefinita, le autorizzazioni sulle tabelle sono **ereditate dall'autorizzazione sul database**.

**Colonne**

* **Connection** – a quale connessione si applica la regola.
* **Database names** – i database da confrontare (elenco o espressione regolare).
* **Schema names** – gli schemi da confrontare (elenco o espressione regolare).
* **Table names** – i nomi degli oggetti da confrontare (tabella/vista/procedura/trigger) come elenco o espressione regolare.
* **Scope** – quali tipi di oggetto sono coperti dalla regola (tabelle, viste, procedure, trigger, …).
* **Role (livello di accesso)**
  * **Read** – può leggere i dati della tabella.
  * **Update only** – può aggiornare le righe; **insert** e **delete** non sono consentiti.
  * **Create, update, delete** - può modificare le righe senza restrizioni
  * **Run script** – può eseguire uno script che interessa questo oggetto.
    > Nota: se **non** disponi di **"Run script"** a livello di **database**, non puoi utilizzarlo a livello di tabella.
  * **Deny** – blocca l'accesso all'oggetto.

