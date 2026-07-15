---
sourceHash: 1565401b5cbe564d5dea5c98e8e060786cb30e1952808c41e0a5542a29f3ef42
language: sk
title: Team Premium na Dockeri
weight: 30
---

Typická inštalácia Team Premium pozostáva z dvoch komponentov: 
- Docker kontajner so serverom DbGate
- Databázový server (MS SQL, MySQL, PostgreSQL, Oracle) - interná úložná databáza pre pripojenia, používateľov a role. Môžete použiť existujúci databázový server alebo nainštalovať nový.

## Docker kontajner so serverom DbGate
Použite [obraz DbGate Team Premium](https://hub.docker.com/r/dbgate/dbgate-premium) z Docker Hub:
```
docker pull dbgate/dbgate-premium
```

Kontajner DbGate Team Premium vyžaduje nastavenie niektorých premenných prostredia:
- `STORAGE_SERVER`, `STORAGE_DATABASE`, `STORAGE_USER`, `STORAGE_PASSWORD`, `STORAGE_ENGINE` - definujú pripojenie k internej úložnej databáze

Ďalšie podrobnosti o dostupných premenných prostredia nájdete v [dokumentácii premenných prostredia](/sk/dbgate/customization/env-variables/#team-premium-edition-configuration).

## Požiadavky na zdroje

DbGate Team Premium má v skutočnosti veľmi nízku spotrebu zdrojov, ale pre najlepší výkon odporúčame nasledujúcu konfiguráciu (pre 10 súbežných používateľov):
- 2 jadrá CPU
- 4 GB RAM (zahŕňa spotrebu RAM internej úložnej databázy MySQL alebo PostgreSQL)
- 10 GB voľného miesta na disku (pre inštaláciu dockeru, úložnú databázu, dočasné súbory, výsledky dotazov atď. Skutočná spotreba miesta na disku závisí od spôsobu používania)

Pri menšom počte používateľov môžete použiť nižšie limity zdrojov (1 GB RAM, 1 jadro CPU).  
Ak potrebujete minimalizovať spotrebu zdrojov pri malých inštaláciách, odporúčame použiť ako interné úložisko MySQL/MariaDB.  

## Konfigurácia dockeru

Ak chcete používať diskové súbory na ukladanie používateľských súborov (napríklad export výsledkov dotazov), mali by ste namapovať cestu `/root/.dbgate` v kontajneri.

Nižšie je príklad súboru `docker-compose.yml`, ktorý definuje kontajner DbGate Team Premium s PostgreSQL ako internou úložnou databázou.
- Môžete definovať premennú prostredia `DBGATE_LICENSE` na nastavenie licenčného kľúča. Ak nie je nastavená, DbGate si pri prvom spustení vyžiada licenčný kľúč.
-  Môžete definovať premennú prostredia 'ADMIN_PASSWORD' na nastavenie hesla používateľa admin. Ak nie je nastavená, DbGate si pri prvom spustení vyžiada heslo administrátora.

```yaml
version: '3'
services:
  dbgate:
    image: dbgate/dbgate-premium
    restart: always
    ports:
      - 80:3000
    environment:
      STORAGE_SERVER: postgres_service
      STORAGE_USER: postgres
      STORAGE_PASSWORD: XXXStoragePwd
      STORAGE_PORT: 5432
      STORAGE_DATABASE: dbgate
      STORAGE_ENGINE: postgres@dbgate-plugin-postgres
      STORAGE_SCHEMA: public
    volumes:
      - dbgate_data:/root/.dbgate

  postgres_service:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: XXXStoragePwd
      POSTGRES_DB: dbgate
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
    postgres_data:
      driver: local
    dbgate_data:
      driver: local
```

## Bezstavovosť/Stavovosť
Kontajner DbGate je stavový. 

Vnútri kontajnera sú uložené nasledujúce údaje:
* Relácie prihlásených používateľov
* Stavy vykonávania dotazov
* Dočasné súbory (napríklad výsledky)
* Otvorené databázové transakcie
* Otvorené databázové pripojenia

Nie je možné správne spustiť viacero kontajnerov DbGate za load balancerom, pretože vyššie uvedené údaje nie sú medzi kontajnermi zdieľané.

## DbGate Server z NPM
Ak vaša infraštruktúra nepodporuje Docker, môžete použiť [NPM balík DbGate Team Premium](https://www.npmjs.com/package/dbgate-serve-premium):
```
npm install -g dbgate-serve-premium
```
 
## Izolácia procesov
DbGate Team Premium používa izoláciu procesov na úrovni databázového pripojenia, takže viacerí používatelia môžu používať rovnaký databázový server bez vzájomného ovplyvňovania. Proces odvetvený z DbGate rastie s počtom aktívnych používateľov a pripojení, preto sa uistite, že váš server má dostatok zdrojov.
Nasledujúce entity sú izolované do nového procesu:
* Serverové pripojenia
* Databázové pripojenia
* Relácie dotazov
* Vykonávanie úloh exportu/importu
* SSH tunelovanie
