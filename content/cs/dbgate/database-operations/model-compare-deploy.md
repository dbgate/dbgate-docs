---
sourceHash: 9faead63589d3a58402650e29cd85afd2223ffa5317dbd506eb962c893c3c04e
language: cs
title: Porovnání a nasazení modelů
weight: 15
---

DbGate umí porovnat strukturu databáze a nasadit změny *(Premium)*. To se hodí pro udržování prostředí v souladu a pro verzování schématu.

![Compare database](https://media.dbgate.io/img/compare-database-settings-light.png)

## Porovnání databází

* **Porovnání dvou databází** - najděte rozdíly ve sloupcích, definicích pohledů a dalších SQL objektech.
* **Synchronizace struktury** - vygenerujte a spusťte akce potřebné k tomu, aby jedna databáze odpovídala druhé.
* **Porovnání proti YAML modelu** - porovnejte skutečnou databázi s modelem uloženým v YAML a nasaďte rozdíly.
* **Nastavení** - řiďte porovnání, například ignorujte cizí klíče, vylučte konkrétní objekty nebo zvolte, které synchronizační akce se mají provést.

## Export modelu databáze

* **Scaffold do složky** - uložte model existující databáze do složky nebo do jediného souboru JSON.
* **YAML soubory tabulek** - tabulky jsou uloženy jako jednoduché YAML soubory, které můžete udržovat v Git repozitáři.
* **SQL soubory s definicemi** - pohledy, uložené procedury a funkce jsou uloženy jako SQL soubory.

## Nasazení

Model nasaďte vizuálně pomocí nástroje Compare, nebo z příkazové řádky jako součást CI/CD pipeline. Formát souboru modelu a postup přes CLI najdete v části [Nasazení databáze](dbdeploy).

## Související stránky

* [Editor tabulek a schémat](schema-editor) - úprava struktury tabulek přes GUI
* [Nasazení databáze](dbdeploy) - formát souboru modelu a nasazení z příkazové řádky
