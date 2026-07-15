---
sourceHash: 4f9596eb7ab62bc22f186ebb87b019eb2986c18eb704368b8634ffc2cd471482
language: cs
title: Nasazení na Azure
weight: 20
---

DbGate Azure edition je kolaborativní, víceuživatelská webová platforma navržená specificky pro správu databází v rámci Azure. Díky využití infrastruktury Azure zjednodušuje týmovou spolupráci v organizacích, které pracují v cloudovém prostředí. Její sdílené rozhraní běžící v prohlížeči usnadňuje spolupráci, přístup k datům a dohled nad databázemi a zároveň se bezproblémově integruje s Azure.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate na Azure{{< /button >}}


## Klíčové funkce DbGate Azure
DbGate Azure podporuje stejné funkce jako DbGate Team Premium, ale je optimalizován pro Azure

* Podpora Azure managed identity
* Administrace uživatelů, připojení a rolí
* Procházení, filtrování a editace dat
* Import a export dat
* Vizuální návrhář dotazů

## Průběh instalace
Instalace na Azure je velmi přímočará, jde téměř o proces na jedno kliknutí. 

Doporučujeme virtuální stroje s 2 GB RAM.

Po instalaci musíte nastavit heslo správce, poté můžete spravovat připojení, uživatele, role a přidělovat oprávnění.

## Předplatné a licencování
DbGate Azure lze předplatit prostřednictvím Azure Marketplace, přičemž cena se odvíjí od počtu procesorů zvoleného virtuálního stroje. 

30denní bezplatná zkušební verze vám zpřístupní všechny funkce DbGate. Po skončení zkušební doby probíhá fakturace podle cenového plánu Azure odpovídajícího zvolené velikosti instance. Není potřeba žádná další licence, protože všechny platby jsou řešeny prostřednictvím předplatného [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview).

## Aktualizace DbGate Azure
DbGate Azure má svůj speciální build a běží přímo na virtuálním serveru (není zde žádná další virtualizační vrstva jako docker). K dispozici je funkce automatické aktualizace – po startu si kontejner vyžádá nejnovější build, a pokud jej najde, nahradí starou verzi. Nemusíte tedy aktualizovat ručně. 

Pokud ručně vytvoříte nový virtuální stroj s novou verzí, bude mít vlastní novou databázi (interní MySQL databáze je součástí virtuálního stroje), takže neexistuje jednoduchý způsob, jak přenést připojení a uživatele na nový virtuální stroj.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate na Azure{{< /button >}}
