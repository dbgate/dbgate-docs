---
sourceHash: 3dab8886ac4d4e94fd5a5f1cfcbccab5e941b303d64e8ba9fc96bc2ee264040b
language: it
title: Browser ed editor dei dati
weight: 5
---

Il browser dei dati è la vista principale di DbGate per visualizzare e modificare i dati delle tabelle. Apri una qualsiasi tabella, vista o collezione per ottenere una griglia veloce, simile a Excel. Questa pagina tratta la navigazione, la modifica e l'esplorazione dei dati correlati; per le espressioni di filtro vedi [Filtraggio dei dati](data-filtering).

![Data browser](https://media.dbgate.io/img/common-data-browser-light.png)

## Navigazione dei dati

* **Navigazione da tastiera** - spostati nella griglia con i tasti freccia, come in un foglio di calcolo.
* **Ordinamento** - fai clic sull'intestazione di una colonna per ordinare in base a quella colonna.
* **Filtro** - filtra le righe usando la riga di filtro sopra la griglia; vedi [Filtraggio dei dati](data-filtering) per la sintassi completa delle espressioni.
* **Gestore colonne** - trova le colonne per nome e nascondi quelle che non ti servono.
* **Copia avanzata** - copia le celle selezionate come CSV, YAML, `INSERT` SQL o insert MongoDB.

## Modifica dei dati

La modifica dei dati avviene direttamente nella griglia:

* **Modifica in stile Excel** - modifica le celle sul posto; copia e incolla intervalli di righe, anche tra tabelle diverse.
* **Modifiche in sospeso** - le tue modifiche vengono raccolte come modifiche in sospeso. Rivedi lo script SQL di modifica generato prima che tocchi il database, poi salva o annulla.
* **Inserisci ed elimina righe** dalla griglia o dal menu contestuale.

![Save changes](https://media.dbgate.io/img/data-browser-save-changes-light.png)

### Macro dell'editor dei dati *(Premium)*

Applica macro predefinite alle celle selezionate - ad esempio cambiare il maiuscolo/minuscolo del testo, rimuovere i segni diacritici o generare un UUID.

## Lavorare con i dati correlati

DbGate rende semplice seguire le relazioni tra le tabelle:

* **Suggerimenti di relazione** - visualizza un valore testuale della tabella referenziata accanto a una chiave esterna numerica.
* **Espansione delle colonne con chiave esterna** - espandi una colonna con chiave esterna per visualizzare i dati referenziati in linea.
* **Apri dettaglio** - passa alla riga referenziata da una chiave esterna.
* **Viste master/dettaglio** *(Premium)* - esplora le righe correlate in un layout master/dettaglio collegato.

![Master/detail](https://media.dbgate.io/img/data-browser-master-detail-light.png)

## Vista modulo

La vista modulo mostra una singola riga come un elenco verticale, "trasposto" - ideale per tabelle con molte colonne. Funziona come una vista ad albero, quindi le colonne con chiave esterna possono essere espanse per esplorare i dati correlati.

![Form view](https://media.dbgate.io/img/data-browser-form-view-light.png)

## Raggruppamento *(Premium)*

Applica il raggruppamento (`GROUP BY`) nella vista a griglia per aggregare le righe direttamente durante la navigazione.

## Pagine correlate

* [Filtraggio dei dati](data-filtering) - sintassi delle espressioni di filtro
* [Esportazione e importazione](export-import) - sposta i dati dentro e fuori dalle tabelle
* [Prospettive](perspectives) - viste annidate e di sola lettura su dati correlati complessi
* [Editor SQL](/it/dbgate/sql-and-queries/sql-editor/) - modifica i risultati delle query allo stesso modo *(Premium)*
