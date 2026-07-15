---
sourceHash: 22f2bb33edfa72684bb05dbcccca0a7b4f618485c77b184b851a079c9a3b7aff
language: sk
title: AI funkcie
weight: 55
---

DbGate obsahuje niekoľko funkcií poháňaných AI *(Premium a Team Premium)*. Sú dostupné všetkým používateľom Premium bez API kľúčov či konfigurácie - DbGate používa vlastnú AI bránu, ktorá presmerúva požiadavky na poskytovateľa LLM.

![Database chat](https://media.dbgate.io/img/database-chat-light.png)

## Databázový chat

Databázový chat je AI chatbot, ktorý rozumie schéme vašej databázy aj jej dátam.

* **Prirodzená konverzácia** - pýtajte sa v ľubovoľnom prirodzenom jazyku a získajte odpovede alebo SQL pripravené na spustenie.
* **Znalosť kontextu** - model pozná vašu schému a (s povolením) aj živé dáta, takže navrhuje správne spojenia, filtre a agregácie.
* **Iteratívnosť** - upresnite zadanie príkazmi ako "pridaj filter podľa dátumu" alebo "zoskup podľa zákazníka" a dotaz sa okamžite aktualizuje.
* **Grafy** - požiadajte o stĺpcový, koláčový alebo čiarový graf zostavený z výsledkov.
* **Režim konzultanta** - dokáže analyzovať uložené procedúry a pohľady, takže sa môžete pýtať napríklad "Vysvetli procedúru X" alebo "Ktoré tabuľky sú ovplyvnené procedúrou Y". DbGate zobrazí, ktoré objekty boli analyzované.

### Spúšťanie SQL - bezpečnosť na prvom mieste

Databázový chat môže na zodpovedanie otázok spúšťať SQL. Vy si vyberiete ako:

* **Opýtať sa pred spustením SQL (predvolené)** - DbGate sa pred spustením každého dotazu opýta.
* **Spúšťať SQL automaticky** - dotazy iné než `SELECT` stále vyžadujú potvrdenie.
* **Nikdy nespúšťať, iba navrhovať SQL** - chat iba zobrazuje dotazy; do LLM sa neodosielajú žiadne dáta z vašej databázy.

Ak navrhnutý dotaz zlyhá, DbGate odošle chybu späť modelu, ktorý dotaz zvyčajne automaticky opraví.

## SQL AI asistent

Použite chat ako SQL asistenta - "Napíš SQL dotaz na 10 najlepších zákazníkov podľa predaja" - a výsledok otvorte na karte [SQL editora](/sk/dbgate/sql-and-queries/sql-editor/).

## Vysvetlenie chyby SQL

Kliknite na **Explain** vedľa chybovej správy a získajte AI vysvetlenie toho, čo sa pokazilo a ako to opraviť.

![Explain query error](https://media.dbgate.io/img/explain-query-error-light.png)

## AI asistent pre témy

AI dokáže tiež generovať vlastné farebné témy - pozrite si [Vlastné témy](/sk/dbgate/customization/custom-themes/).

## Vypnutie AI funkcií

AI funkcie sa dajú úplne vypnúť (napríklad v obmedzených prostrediach) cez nastavenia DbGate.
