---
sourceHash: 0f10d627c0492363d84834c24da993d0686916c833728726a2d34648885161b1
language: it
title: Editor di tabelle e schemi
weight: 5
---

DbGate può creare e modificare la struttura del database tramite un'interfaccia grafica, senza scrivere DDL a mano. Apri l'editor della struttura di una tabella dal suo menu contestuale ("Edit table") oppure crea una nuova tabella dal menu contestuale del database.

![Table structure editor](https://media.dbgate.io/img/table-structure-editor-light.png)

## Modifica delle tabelle

* **Colonne e tipi di dati** - definisci colonne, tipi di dati, nullabilità e valori predefiniti per tabelle nuove o esistenti.
* **Chiavi e indici** - gestisci chiavi primarie, chiavi esterne e indici.
* **Proprietà specifiche del motore** - imposta opzioni specifiche del database, come il motore delle tabelle di MySQL.

## Anteprima SQL e modifiche sicure

* **Anteprima SQL** - prima che qualsiasi cosa venga salvata, DbGate mostra l'SQL generato in modo che tu possa esaminarlo.
* **Avviso di ricreazione della tabella** - quando una modifica richiede la ricreazione della tabella (una limitazione di alcuni database), DbGate ti avvisa e ti permette di ispezionare prima lo script generato.

## Altri oggetti del database

Puoi anche creare, eliminare e modificare altri oggetti - viste, stored procedure e funzioni - e sfogliare tabelle, viste, procedure, funzioni e collezioni MongoDB dall'albero degli oggetti.

## Pagine correlate

* [Confronta e distribuisci modelli](model-compare-deploy) - confronta la struttura tra database e distribuisci le modifiche *(Premium)*
* [Distribuzione del database](dbdeploy) - file di modello YAML/SQL e distribuzione da riga di comando
