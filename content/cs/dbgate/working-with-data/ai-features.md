---
sourceHash: 22f2bb33edfa72684bb05dbcccca0a7b4f618485c77b184b851a079c9a3b7aff
language: cs
title: Funkce AI
weight: 55
---

DbGate obsahuje několik funkcí využívajících AI *(Premium a Team Premium)*. Jsou dostupné všem uživatelům edice Premium bez nutnosti API klíčů nebo konfigurace - DbGate používá vlastní AI bránu, která přeposílá požadavky poskytovateli LLM.

![Database chat](https://media.dbgate.io/img/database-chat-light.png)

## Databázový chat

Databázový chat je AI chatbot, který rozumí jak schématu vaší databáze, tak jejím datům.

* **Přirozená konverzace** - ptejte se v libovolném přirozeném jazyce a získejte odpovědi nebo SQL připravené ke spuštění.
* **Znalost kontextu** - model zná vaše schéma a (s povolením) i živá data, takže navrhuje správné joiny, filtry a agregace.
* **Iterativní práce** - upřesněte dotaz příkazy jako „přidej filtr podle data“ nebo „seskup podle zákazníka“ a dotaz se okamžitě aktualizuje.
* **Grafy** - požádejte o sloupcový, koláčový nebo spojnicový graf sestavený z výsledků.
* **Režim konzultanta** - dokáže analyzovat uložené procedury a pohledy, takže se můžete ptát například „Vysvětli proceduru X“ nebo „Kterých tabulek se týká procedura Y“. DbGate zobrazí, které objekty byly analyzovány.

### Spouštění SQL - bezpečnost na prvním místě

Databázový chat může spouštět SQL, aby odpověděl na vaše otázky. Způsob si volíte vy:

* **Ask before execute SQL (výchozí)** - DbGate se před spuštěním každého dotazu zeptá.
* **Execute SQL automatically** - dotazy jiné než `SELECT` stále vyžadují potvrzení.
* **Never execute, only suggest SQL** - chat pouze zobrazuje dotazy; do LLM se neodesílají žádná data z vaší databáze.

Pokud navržený dotaz selže, DbGate odešle chybu zpět modelu, který dotaz obvykle automaticky opraví.

## SQL AI asistent

Použijte chat jako SQL asistenta - „Napiš SQL dotaz na 10 nejlepších zákazníků podle prodejů“ - a otevřete výsledek na kartě [SQL editoru](/cs/dbgate/sql-and-queries/sql-editor/).

## Vysvětlení chyby SQL

Kliknutím na **Explain** vedle chybové zprávy získáte vysvětlení od AI, co se pokazilo a jak to opravit.

![Explain query error](https://media.dbgate.io/img/explain-query-error-light.png)

## AI asistent pro motivy

AI umí také generovat vlastní barevné motivy - viz [Vlastní motivy](/cs/dbgate/customization/custom-themes/).

## Vypnutí funkcí AI

Funkce AI lze zcela vypnout (například v omezených prostředích) v nastavení DbGate.
