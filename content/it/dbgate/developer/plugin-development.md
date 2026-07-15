---
sourceHash: e10360d65315ca6bef22d826b37ec0f1623808453e37fd5d2a391f720399cc17
language: it
title: Sviluppo di plugin
weight: 30
---

DbGate supporta la creazione di plugin. Grazie alla procedura guidata per i plugin, creare un plugin di base è davvero semplice. I plugin di DbGate sono pacchetti NPM (JavaScript) e possono avere dipendenze (ma non dipendenze native).

Attualmente esistono 3 tipi di plugin:
- Plugin tema
- Plugin per formati di file
- Plugin driver di database

## Installare i prerequisiti
È necessario avere installato [node.js](https://nodejs.org). 

Serviranno inoltre [Yeoman](https://yeoman.io/) e il [generatore di plugin DbGate](https://www.npmjs.com/package/generator-dbgate) per yeoman:

```sh
npm install -g yo
npm install -g generator-dbgate
```

## Creare un plugin
Esegui il seguente comando nella console:

```sh
yo dbgate
```

Devi rispondere a 3 domande:
- Nome del plugin, deve iniziare con dbgate-plugin-, ad es. dbgate-plugin-myplugin
- Tipo di plugin, scegli ad es. "Database driver"
- Gestore di pacchetti, scegli npm o yarn, come preferisci. DbGate usa yarn.

## Modificare e testare il plugin
Apri un editor, l'opzione consigliata è [Visual Studio Code](https://code.visualstudio.com/)  . 
Il plugin tema contiene un solo file sorgente, src/index.js. Puoi modificare i colori del tema come preferisci. L'attributo themeName è il nome che viene mostrato nel selettore dei temi di DbGate.

Quando vuoi vedere il tuo nuovo tema, esegui questo comando dalla console (dalla directory del plugin):
```sh
yarn plugin
```
oppure, se usi npm, allora
```sh
npm run plugin
```
Questo comando installa il tuo plugin nell'istanza di DbGate installata localmente (o lo aggiorna, quando apporti modifiche). Dopo il riavvio di DbGate, dovresti vedere il nuovo tema.  
Il riavvio non è necessario, per usare la nuova versione del plugin dopo aver eseguito "yarn plugin" è sufficiente ricaricare l'applicazione (menu View/Reload)

## Rimuovere un plugin
Puoi disinstallare il plugin dal widget dei plugin di DbGate. Oppure usando il seguente comando:
```sh
yarn plugout
```

## Pubblicare un plugin
Il plugin è un normale pacchetto NPM, puoi pubblicarlo nel repository NPM. Dopo la pubblicazione, sarà disponibile per tutti gli utenti di DbGate nel widget "Plugins".

## Icona del plugin
Ogni plugin è rappresentato da un'icona nell'elenco delle estensioni. NPM non supporta le icone per i pacchetti NPM, quindi l'icona può essere inserita nel campo description del file package.json con la seguente sintassi:

```
    "description": "Any description ![icon](https://link_to_icon.svg)",
```

Se usi il generatore yeoman, ti aiuterà un po' con questo.

## Creare un plugin driver di database
Creare un plugin driver è molto simile alla creazione normale, solo che devi selezionare "Database driver plugin". Dopo `yarn plugin` dovresti essere in grado di definire una connessione usando il tuo nuovo driver e di vedere un elenco fittizio di database e tabelle.

Puoi creare molto rapidamente un driver semplice con funzionalità di base, le funzionalità più complesse possono essere implementate in seguito.

La creazione di un driver può consistere nei seguenti passaggi:
* trova un pacchetto nodejs (driver) adeguato. Se possibile, scegli un pacchetto in puro JavaScript. I pacchetti nativi sono una grande complicazione, il pacchetto nativo deve essere aggiunto alla distribuzione di DbGate e inoltre puoi aspettarti problemi con la build su piattaforme diverse. D'altra parte, i pacchetti in puro JavaScript funzionano normalmente senza problemi su tutte le piattaforme, senza bisogno di modificare DbGate.
* definisci i campi per la connessione in frontend/driver.js, funzione showConnectionField
* implementa la funzione connect in backend/driver.js 
* implementa la funzione getVersion in backend/driver.js (facoltativo, ma una volta fatto puoi testare la connessione con il pulsante "Test" nella scheda della connessione)
* implementa il metodo _rynAnalysis nella classe backend/Analyser.js. Questo metodo deve restituire la struttura del database.
* implementa il metodo query in backend/driver.js. Dopodiché dovresti essere in grado di vedere l'elenco delle tabelle e di sfogliare i dati delle tabelle
* implementa gli altri metodi. Usa gli altri plugin driver come ispirazione, il plugin più tipico è probabilmente il plugin PostgreSQL, https://github.com/dbgate/dbgate/tree/master/plugins/dbgate-plugin-postgres
