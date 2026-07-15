---
sourceHash: fd6032a57cb859a0d8cb5046fde87de9bf1a85de56c66586391e84ecbbdc24c1
language: cs
title: Nasazení na AWS
subtitle: Nasazení na Amazon EC2 cluster jedním kliknutím
icon: aws.svg
weight: 10
demo_url: https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy
demo_title: Zobrazit na AWS
edition: 'premium'
---

DbGate AWS edition je kolaborativní víceuživatelská webová platforma navržená speciálně pro správu databází v rámci Amazon Web Services (AWS). Díky využití infrastruktury AWS zjednodušuje týmovou spolupráci pro organizace působící v cloudových prostředích. Její sdílené rozhraní běžící v prohlížeči usnadňuje spolupráci, přístup k datům a dohled nad databázemi a zároveň se hladce integruje s AWS.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate na AWS{{< /button >}}

## Klíčové vlastnosti DbGate AWS
DbGate AWS podporuje stejné funkce jako DbGate Team Premium, ale je optimalizován pro AWS

* Podpora pro AWS IAM
* Administrace uživatelů, připojení a rolí
* Procházení, filtrování a editace dat
* Import a export dat
* Vizuální návrhář dotazů

## Průběh instalace
Instalace na AWS je velmi přímočará, jde téměř o proces na jedno kliknutí.

Pro nejlepší uživatelský komfort doporučujeme typ instance t2.medium, ale pro malý počet uživatelů postačí i t2.micro dostupná ve free tier.

Po instalaci musíte nastavit heslo administrátora, poté můžete spravovat připojení, uživatele, role a udělovat oprávnění.

## Předplatné a licencování
DbGate AWS lze předplatit prostřednictvím AWS Marketplace, přičemž cena se odvíjí od velikosti zvolené instance. Větší instance podporují více souběžných uživatelů.

30denní bezplatná zkušební verze vám poskytne přístup ke všem funkcím DbGate. Po skončení zkušební doby probíhá účtování podle cenového plánu AWS odpovídajícího zvolené velikosti instance. Žádné další licencování není potřeba, protože všechny platby jsou vyřizovány prostřednictvím předplatného na [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy).

## Aktualizace DbGate AWS
DbGate AWS má svůj speciální build a běží přímo na virtuálním serveru v EC2 (není zde žádná další virtualizační vrstva jako docker). K dispozici je funkce automatické aktualizace – po startu si kontejner vyžádá nejnovější build, a pokud jej najde, nahradí starou verzi. Nemusíte tedy aktualizovat ručně.

Pokud ručně vytvoříte nový EC2 kontejner s novou verzí, bude mít vlastní novou databázi (interní MySQL databáze je součástí kontejneru), takže neexistuje jednoduchý způsob, jak přenést připojení a uživatele do nového EC2 kontejneru.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate na AWS{{< /button >}}
