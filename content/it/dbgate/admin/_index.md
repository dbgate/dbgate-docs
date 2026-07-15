---
sourceHash: ede2384faaa854f0e026527b8904456ab9b2e5bb8e75f17843afd05cbe47ca54
language: it
title: Amministrazione
weight: 60
---

L'interfaccia di amministrazione consente a un team di utilizzare DbGate come applicazione web condivisa e multiutente: puoi gestire le connessioni in modo centralizzato, definire chi può accedere e con quali modalità, e concedere accessi granulari a database e oggetti tramite utenti, ruoli e permessi. Ospita inoltre i file condivisi del team. Tutto ciò che viene configurato qui è memorizzato nel database di archiviazione anziché in file locali.

Lo strumento di amministrazione è disponibile solo nell'edizione Team Premium. Nell'edizione Community, configura DbGate utilizzando le [variabili d'ambiente](/it/dbgate/customization/env-variables).

Tutta la configurazione dell'amministrazione viene salvata nel database di archiviazione: utilizza le [variabili d'ambiente STORAGE_xxx](/it/dbgate/customization/env-variables/#team-premium-edition-configuration) per configurarlo.

In questa sezione:

* [Autenticazione](auth) - configura i metodi di accesso e i provider di identità
* [Connessioni](connection) - gestisci le connessioni disponibili per il tuo team
* [File del team](team-files) - condividi script SQL, diagrammi ER e grafici
* [Utenti](users) - gestisci gli account utente
* [Ruoli](roles) - raggruppa i permessi in ruoli
* [Permessi](permissions) - concedi l'accesso a connessioni, database e tabelle

## Accesso amministratore

La pagina di amministrazione è disponibile all'URL https://your_dbgate_instance/admin.html . 

L'amministratore root deve avere una password definita. Puoi impostare la variabile d'ambiente ADMIN_PASSWORD. Se questa variabile non è definita, DbGate richiede innanzitutto la password di amministratore.

Puoi quindi aggiungere il permesso di amministrazione a un altro utente con un metodo di autenticazione diverso, ma prima devi aprire questa pagina di amministrazione.

