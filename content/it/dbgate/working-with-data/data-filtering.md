---
sourceHash: ba49d4bd53c041c5e042d07318208cea17d32dd6c3079b21b9e4072bc94c457f
language: it
title: Filtraggio dei dati
weight: 10
---

DbGate dispone di un potente motore di filtraggio dei dati, che consente sia un filtraggio molto semplice sia condizioni complesse.

I filtri sui dati possono essere usati in molti punti di DbGate, ma il luogo più comune è il filtraggio della griglia dei dati.

![filter screenshot](https://media.dbgate.io/img/data-browser-filter-light.png)

I filtri sono evidenziati con uno sfondo:
* Sfondo verde - il filtro è corretto ed è applicato
* Sfondo rosso - c'è un errore nell'espressione del filtro, il filtro viene ignorato

Hai diverse possibilità per creare un filtro:
* {{< mdi "filter" >}} - mostra il menu con filtri predefiniti e finestre di dialogo
* {{< mdi "dots-vertical" >}} - consente di scegliere i valori da filtrare
* Puoi scrivere il filtro direttamente - usa la sintassi molto semplice descritta in [filter-expressions](#filter-expressions)
* Oppure puoi creare il filtro con metodi visuali e modificarlo manualmente

Altri comandi:
* {{< mdi "filter-off" >}} - cancella tutti i filtri

## Filter expressions
Le espressioni di filtro sono progettate per essere intuitive: nella maggior parte dei casi scrivi semplicemente e direttamente ciò che vuoi cercare. Tuttavia la sintassi è piuttosto potente, puoi combinare più condizioni e usare vari operatori.
La sintassi delle espressioni dipende dal tipo di dati della colonna.

### Esempi

| Tipo di colonna | Espressione di filtro |  Descrizione |
|----------|-------------|------|
| string | canada | il valore della colonna contiene il testo "canada" |
| string | canada, usa | il valore della colonna contiene il testo "canada" o "usa" |
| string | canada lake | il valore della colonna contiene il testo "canada" e "lake" |
| string | NOT EMPTY NOT NULL | la stringa ha un valore non vuoto |
| number | >10 | il valore della colonna è maggiore di 10 |
| number | >=5 <=10 | il valore della colonna è compreso tra 5 e 10 |
| number | 1,2,3 | il valore della colonna è 1 o 2 o 3 |
| datetime | 2020-05-26 | il valore data è del 2020-05-26 (intervallo di 24 ore)  |

### Filtri comuni (per tutti i tipi di dati)
- NULL - il valore della colonna è null
- NOT NULL - il valore della colonna non è null
- {$$ is null} - condizione SQL, scritta tra parentesi graffe {}. $$ è il segnaposto per la colonna filtrata

### Filtri di testo
Il confronto tra testi non distingue tra maiuscole e minuscole.
- text - il valore della colonna contiene _text_. Può essere racchiuso tra 'apici singoli' o "doppi apici"
- +text - il valore della colonna contiene _text_ (uguale alla riga precedente)
- ^text - il valore della colonna inizia con _text_
- $text - il valore della colonna termina con _text_
- !+text - il valore della colonna non contiene _text_ (uguale alla riga precedente)
- !^text - il valore della colonna non inizia con _text_
- !$text - il valore della colonna non termina con _text_
- EMPTY - il valore della colonna non contiene caratteri diversi dagli spazi
- NOT EMPTY - il valore della colonna contiene caratteri diversi dagli spazi

### Filtri numerici
- number - il valore della colonna è uguale al numero
- =number - il valore della colonna è uguale al numero
- !=number - il valore della colonna non è uguale al numero
- <>number - il valore della colonna non è uguale al numero
- <number - il valore della colonna è minore del numero
- \>number - il valore della colonna è maggiore del numero
- <=number - il valore della colonna è minore o uguale al numero
- \>=number - il valore della colonna è maggiore o uguale al numero

### Filtri di data e ora
- 2021 - anno del valore della colonna
- 2021-02 - anno, mese del valore della colonna
- 2021-02-15 - anno, mese, giorno del valore della colonna
- 2021-02-15 23:15 - anno, mese, giorno, ora, minuto del valore della colonna
- 2021-02-15 23:15:51 - anno, mese, giorno, ora, minuto, secondo del valore della colonna
- Filtri relativi alla data corrente
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

### Filtri logici (boolean)
- TRUE, true, 1 - il valore della colonna è true/1
- FALSE, false, 0 - il valore della colonna è false/0

### Combinazioni di filtri
I filtri possono essere combinati tra loro. Lo spazio è interpretato come operatore AND, la virgola come operatore OR. AND ha priorità più alta di OR.
