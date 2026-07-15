---
sourceHash: f2791f82e04437cfea34f20ce37c68c887e87a2c0da52d28b9f823e0e184aab9
language: cs
title: Vlastní motivy
weight: 10
---

DbGate má flexibilní podporu motivů. Můžete si vytvořit vlastní motiv a změnit barvy různých prvků uživatelského rozhraní.

Motivy se vytvářejí jako soubory JSON. Nejjednodušší způsob, jak vytvořit vlastní motiv, je použít AI asistenta pro motivy.

## AI asistent pro motivy
Pro vyvolání AI asistenta pro motivy otevřete Settings/Themes a poté klikněte na tlačítko "Customize with AI assistant".

![Theme settings](https://media.dbgate.io/img/app-settings-themes-light.png)

AI asistent pro motivy přizpůsobí váš motiv podle vašich pokynů. Můžete určit, které barvy chcete změnit a jak. Například můžete říct "Make primary color green, and background color dark gray".

![screenshot](/screenshots/dbgate-green.png)

Generování motivu pomocí AI asistenta zabere několik minut, generuje se přibližně 280 proměnných. Po vygenerování motivu můžete kliknutím na tlačítko "Apply Theme" nový motiv použít. Můžete také použít tlačítko "Save theme" a uložit motiv jako soubor JSON. Všechny uložené motivy jsou pak dostupné ve výběru motivů. Motivy můžete také spravovat (přejmenovat, upravit, smazat) ve widgetu souborů {{< mdi "file" >}}.

## Sdílení motivů v DbGate Cloud
Své motivy můžete sdílet s ostatními uživateli DbGate pomocí DbGate cloud. Chcete-li motiv sdílet, vytvořte pull request v [repozitáři DbGate knowledge base](https://github.com/dbgate/dbgate-knowledge-base). Motivy jsou uloženy v adresáři folder-Themes. Příklady najdete u existujících motivů. Stačí zkopírovat soubor JSON s vaším motivem do tohoto adresáře a vytvořit pull request. Po sloučení vašeho pull requestu bude váš motiv dostupný pro všechny uživatele DbGate ve výběru motivů.