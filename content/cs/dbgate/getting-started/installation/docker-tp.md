---
sourceHash: 1565401b5cbe564d5dea5c98e8e060786cb30e1952808c41e0a5542a29f3ef42
language: cs
title: Team Premium na Dockeru
weight: 30
---

Typická instalace Team Premium se skládá ze dvou komponent:
- Docker kontejner s DbGate serverem
- Databázový server (MS SQL, MySQL, PostgreSQL, Oracle) - interní úložná databáze pro připojení, uživatele a role. Můžete použít existující databázový server nebo nainstalovat nový.

## Docker kontejner s DbGate serverem
Použijte [image DbGate Team Premium](https://hub.docker.com/r/dbgate/dbgate-premium) z Docker Hubu:
```
docker pull dbgate/dbgate-premium
```

Kontejner DbGate Team Premium vyžaduje nastavení několika proměnných prostředí:
- `STORAGE_SERVER`, `STORAGE_DATABASE`, `STORAGE_USER`, `STORAGE_PASSWORD`, `STORAGE_ENGINE` - definují připojení k interní úložné databázi

Více informací o dostupných proměnných prostředí najdete v [dokumentaci proměnných prostředí](/cs/dbgate/customization/env-variables/#team-premium-edition-configuration).

## Požadavky na zdroje

DbGate Team Premium má ve skutečnosti velmi nízkou spotřebu zdrojů, ale pro nejlepší výkon doporučujeme následující konfiguraci (pro 10 souběžných uživatelů):
- 2 CPU jádra
- 4 GB RAM (zahrnuje spotřebu RAM interní úložné databáze MySQL nebo PostgreSQL)
- 10 GB volného místa na disku (pro instalaci dockeru, úložnou databázi, dočasné soubory, výsledky dotazů atd. Skutečná spotřeba místa na disku závisí na způsobu používání)

Pro menší počet uživatelů můžete použít nižší limity zdrojů (1 GB RAM, 1 CPU jádro).  
Pokud potřebujete minimalizovat spotřebu zdrojů u malých instalací, doporučujeme použít jako interní úložiště MySQL/MariaDB.  

## Konfigurace dockeru

Pokud chcete pro ukládání uživatelských souborů (například exportů výsledků dotazů) používat souborový disk, měli byste v kontejneru namapovat cestu `/root/.dbgate`.

Níže je příklad souboru `docker-compose.yml`, který definuje kontejner DbGate Team Premium s PostgreSQL jako interní úložnou databází.
- Můžete definovat proměnnou prostředí `DBGATE_LICENSE` pro nastavení licenčního klíče. Pokud není nastavena, DbGate si při prvním spuštění o licenční klíč řekne.
-  Můžete definovat proměnnou prostředí 'ADMIN_PASSWORD' pro nastavení hesla uživatele admin. Pokud není nastavena, DbGate si při prvním spuštění o heslo administrátora řekne.

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

## Bezstavovost/Stavovost
Kontejner DbGate je stavový.

Uvnitř kontejneru jsou uložena následující data:
* Relace přihlášených uživatelů
* Stavy provádění dotazů
* Dočasné soubory (například výsledky)
* Otevřené databázové transakce
* Otevřená databázová připojení

Není možné správně provozovat více kontejnerů DbGate za load balancerem, protože výše uvedená data nejsou mezi kontejnery sdílena.

## DbGate server z NPM
Pokud vaše infrastruktura nepodporuje Docker, můžete použít [NPM balíček DbGate Team Premium](https://www.npmjs.com/package/dbgate-serve-premium):
```
npm install -g dbgate-serve-premium
```
 
## Izolace procesů
DbGate Team Premium používá izolaci procesů na úrovni databázového připojení, takže více uživatelů může používat stejný databázový server bez vzájemného ovlivňování. Proces odvětvený z DbGate roste s počtem aktivních uživatelů a připojení, proto se ujistěte, že váš server má dostatek zdrojů.
Do nového procesu jsou izolovány následující entity:
* Připojení k serverům
* Databázová připojení
* Relace dotazů
* Provádění exportních/importních úloh
* SSH tunelování
