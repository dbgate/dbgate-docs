---
sourceHash: 80df2a73525118cee579014e200ff5f67715aa6f35468656abb3f8b70c254566
language: it
title: Archivi di dati
weight: 1
---

Gli archivi sono cartelle con dati in formato JSONL (NDJSON). DbGate consente di lavorarci in modo molto efficiente: puoi importarli in un database, esportarli in altri formati oppure modificare direttamente i dati nell'archivio. Un archivio si comporta come un database molto veloce e leggero memorizzato in file locali.

## Formato JSONL
DbGate utilizza internamente il formato JSONL ovunque. JSONL è un file di testo in cui ogni riga contiene una riga di dati convertita in stringa JSON. DbGate presuppone che la prima riga possa contenere un'intestazione (anch'essa in formato JSON) con la struttura della tabella. Quando usi JSONL con una struttura dinamica (senza la prima riga fissa), questo formato è standardizzato e può essere caricato in molti altri strumenti. 

## Cartelle di archivio
Un archivio è organizzato in cartelle contenenti file JSONL. Ha una struttura simile a quella di un database. Puoi quindi esportare un intero database in un nuovo archivio: ogni tabella viene esportata in un file JSON e, grazie alla riga di intestazione, viene mantenuta anche la struttura della tabella.

## Visualizzare e modificare i file di archivio
Puoi aprire i file JSONL in diverse modalità:
- menu contestuale "Open" - apre la griglia dati, che consente di ordinare, filtrare e modificare i tuoi dati JSONL
- menu contestuale "Open in text editor" - consente di modificare manualmente il file JSONL

## Archivi e modelli di DB
Le cartelle di archivio vengono usate anche come spazio di archiviazione per i modelli di DB. Puoi esportare il modello di DB dal menu contestuale del database, "Export DB model". Puoi quindi modificare questo modello (file YAML per la struttura delle tabelle, file SQL per viste e stored procedure), confrontarlo con il database reale e distribuirlo nel database
