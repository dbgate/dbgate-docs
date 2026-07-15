---
sourceHash: f2791f82e04437cfea34f20ce37c68c887e87a2c0da52d28b9f823e0e184aab9
language: it
title: Temi personalizzati
weight: 10
---

DbGate offre un supporto flessibile per i temi. Puoi creare il tuo tema personalizzato, modificando i colori dei vari elementi dell'interfaccia utente.

I temi vengono creati come file JSON. Il modo più semplice per creare un tema personalizzato è utilizzare l'assistente AI per i temi.

## Assistente AI per i temi
Per richiamare l'assistente AI per i temi, apri Impostazioni/Temi, quindi fai clic sul pulsante "Customize with AI assistant".

![Theme settings](https://media.dbgate.io/img/app-settings-themes-light.png)

L'assistente AI per i temi personalizzerà il tuo tema in base alle tue istruzioni. Puoi specificare quali colori vuoi modificare e in che modo. Ad esempio, puoi dire "Rendi il colore primario verde e il colore di sfondo grigio scuro".

![screenshot](/screenshots/dbgate-green.png)

La generazione del tema con l'assistente AI richiederà alcuni minuti, poiché vengono generate circa 280 variabili. Dopo che il tema è stato generato, puoi fare clic sul pulsante "Apply Theme" per utilizzare il nuovo tema. Puoi anche usare il pulsante "Save theme" per salvare il tema come file JSON. Tutti i temi salvati sono quindi disponibili nel selettore dei temi. Puoi anche gestire (rinominare, modificare, eliminare) i temi nel widget dei file {{< mdi "file" >}}.

## Condividere i temi in DbGate Cloud
Puoi condividere i tuoi temi con altri utenti di DbGate utilizzando DbGate Cloud. Per condividere un tema, crea una pull request nel [repository della knowledge base di DbGate](https://github.com/dbgate/dbgate-knowledge-base). I temi sono memorizzati nella directory folder-Themes. Consulta i temi esistenti come esempi. È sufficiente copiare il file JSON del tuo tema in quella directory e creare una pull request. Dopo l'unione della tua pull request, il tuo tema sarà disponibile per tutti gli utenti di DbGate nel selettore dei temi.
