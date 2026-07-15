---
sourceHash: 8396e36170a2f74ec485cc366db64869390b971ebf497d3127e7005ee1837c1d
language: it
title: File del team
weight: 25
---

I file del team sono file SQL, diagrammi o altri file archiviati nello storage interno di DbGate. La versione desktop di DbGate salva i file nella cartella dell'utente, l'edizione Team consente di archiviare i file allo stesso modo (in un volume docker), ma è più appropriato archiviare i file nel database di storage, che non viene ricreato quando il container DbGate viene ricreato.

- File su disco 
    - file archiviati su disco o su un volume docker
    - a meno che non venga definito esplicitamente un volume docker (ad es. in docker-compose.yaml), i file vengono ricreati quando il container viene ricreato.
- File del team 
    - file archiviati nel database di storage
    - non vengono persi quando il container viene ricreato, senza bisogno di definire un volume docker
    - consentono di definire permessi di accesso granulari per utenti e ruoli

## Salvare un file SQL come file del team
Quando salvi un file SQL, è sufficiente selezionare la casella "Save to team folder". Il file verrà salvato come file del team.
