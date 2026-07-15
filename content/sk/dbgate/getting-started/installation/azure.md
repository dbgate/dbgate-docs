---
sourceHash: 4f9596eb7ab62bc22f186ebb87b019eb2986c18eb704368b8634ffc2cd471482
language: sk
title: Nasadenie na Azure
weight: 20
---

DbGate Azure edition je kolaboratívna, viacpoužívateľská webová platforma navrhnutá špeciálne na správu databáz v prostredí Azure. Využíva infraštruktúru Azure a zjednodušuje tímovú spoluprácu pre organizácie pôsobiace v cloudových prostrediach. Jej zdieľané rozhranie založené na prehliadači uľahčuje spoluprácu, prístup k dátam a dohľad nad databázami a zároveň sa bezproblémovo integruje s Azure.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate na Azure{{< /button >}}


## Kľúčové vlastnosti DbGate Azure
DbGate Azure podporuje rovnaké funkcie ako DbGate Team Premium, je však optimalizovaný pre Azure

* Podpora Azure managed identity
* Administrácia používateľov, pripojení a rolí
* Prehliadanie, filtrovanie a úprava dát
* Import a export dát
* Vizuálny návrhár dotazov

## Proces inštalácie
Inštalácia na Azure je veľmi jednoduchá, ide takmer o proces na jedno kliknutie.

Odporúčame virtuálne stroje s 2 GB RAM.

Po inštalácii musíte nastaviť heslo správcu, potom môžete spravovať pripojenia, používateľov, role a udeľovať oprávnenia.

## Predplatné a licencovanie
DbGate Azure si možno predplatiť cez Azure Marketplace, pričom cena vychádza z počtu procesorov zvoleného virtuálneho stroja.

30-dňová bezplatná skúšobná verzia vám sprístupní všetky funkcie DbGate. Po skončení skúšobnej doby prebieha fakturácia podľa cenového plánu Azure zodpovedajúceho zvolenej veľkosti inštancie. Nie je potrebná žiadna ďalšia licencia, pretože všetky platby sa vybavujú prostredníctvom predplatného na [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview).

## Aktualizácie DbGate Azure
DbGate Azure má svoj špeciálny build a beží priamo na virtuálnom serveri (nie je tu žiadna ďalšia virtualizačná vrstva ako docker). K dispozícii je funkcia automatickej aktualizácie – po štarte si kontajner vyžiada najnovší build a ak ho nájde, nahradí starú verziu. Nemusíte aktualizovať manuálne.

Ak manuálne vytvoríte nový virtuálny stroj s novou verziou, bude mať svoju novú databázu (interná MySQL databáza je súčasťou virtuálneho stroja), takže neexistuje jednoduchý spôsob, ako presunúť pripojenia a používateľov na nový virtuálny stroj.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate na Azure{{< /button >}}
