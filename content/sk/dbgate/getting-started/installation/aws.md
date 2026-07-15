---
sourceHash: fd6032a57cb859a0d8cb5046fde87de9bf1a85de56c66586391e84ecbbdc24c1
language: sk
title: Nasadenie na AWS
subtitle: Nasadenie jedným kliknutím na klaster Amazon EC2
icon: aws.svg
weight: 10
demo_url: https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy
demo_title: View on AWS
edition: 'premium'
---

DbGate AWS edition je kolaboratívna viacpoužívateľská webová platforma navrhnutá špeciálne pre správu databáz v prostredí Amazon Web Services (AWS). Využitím infraštruktúry AWS zjednodušuje tímovú spoluprácu v organizáciách, ktoré pracujú v cloudových prostrediach. Jej zdieľané rozhranie založené na prehliadači uľahčuje spoluprácu, prístup k dátam a dohľad nad databázami a zároveň sa bezproblémovo integruje s AWS.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate na AWS{{< /button >}}

## Kľúčové vlastnosti DbGate AWS
DbGate AWS podporuje rovnaké funkcie ako DbGate Team Premium, ale je optimalizovaný pre AWS

* Podpora pre AWS IAM
* Správa používateľov, pripojení a rolí
* Prehliadanie, filtrovanie a úprava dát
* Import a export dát
* Vizuálny návrhár dotazov

## Proces inštalácie
Inštalácia na AWS je veľmi jednoduchá, ide takmer o proces na jedno kliknutie.

Pre najlepší používateľský zážitok odporúčame typ inštancie t2.medium, ale pre malý počet používateľov postačí aj t2.micro dostupný v rámci free tier.

Po inštalácii musíte nastaviť heslo správcu, potom môžete spravovať pripojenia, používateľov, role a prideľovať oprávnenia.

## Predplatné a licencovanie
DbGate AWS si môžete predplatiť prostredníctvom AWS Marketplace, pričom cena závisí od veľkosti zvolenej inštancie. Väčšie inštancie podporujú viac súbežných používateľov.

30-dňová bezplatná skúšobná verzia vám sprístupní všetky funkcie DbGate. Po skončení skúšobnej doby prebieha fakturácia podľa cenového plánu AWS v závislosti od zvolenej veľkosti inštancie. Nie je potrebné žiadne ďalšie licencovanie, pretože všetky platby sa realizujú cez predplatné na [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy).

## Aktualizácie DbGate AWS
DbGate AWS má svoj špeciálny build a beží priamo na virtuálnom serveri v EC2 (nie je tu žiadna ďalšia virtualizačná vrstva ako docker). K dispozícii je funkcia automatickej aktualizácie – po štarte kontajner overí, či existuje najnovší build, a ak ho nájde, nahradí ním starú verziu. Nemusíte aktualizovať manuálne.

Ak manuálne vytvoríte nový EC2 kontajner s novou verziou, bude mať svoju novú databázu (interná MySQL databáza je súčasťou kontajnera), takže neexistuje jednoduchý spôsob, ako preniesť pripojenia a používateľov do nového EC2 kontajnera.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate na AWS{{< /button >}}
