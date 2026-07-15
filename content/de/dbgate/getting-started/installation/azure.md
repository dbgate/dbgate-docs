---
sourceHash: 4f9596eb7ab62bc22f186ebb87b019eb2986c18eb704368b8634ffc2cd471482
language: de
title: Bereitstellung auf Azure
weight: 20
---

Die DbGate Azure Edition ist eine kollaborative, mehrbenutzerfähige Webplattform, die speziell für die Datenbankverwaltung innerhalb von Azure entwickelt wurde. Durch die Nutzung der Azure-Infrastruktur vereinfacht sie die Zusammenarbeit für Organisationen, die in Cloud-Umgebungen arbeiten. Ihre gemeinsam genutzte, browserbasierte Oberfläche erleichtert Zusammenarbeit, Datenzugriff und Datenbanküberwachung und lässt sich dabei nahtlos in Azure integrieren.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate auf Azure{{< /button >}}


## Wichtigste Funktionen von DbGate Azure
DbGate Azure unterstützt dieselben Funktionen wie DbGate Team Premium, ist jedoch für Azure optimiert

* Unterstützt Azure Managed Identity
* Verwaltung von Benutzern, Verbindungen und Rollen
* Durchsuchen, Filtern und Bearbeiten von Daten
* Import und Export von Daten
* Visueller Query-Builder

## Installationsprozess
Die Installation auf Azure ist sehr unkompliziert und erfolgt nahezu mit einem einzigen Klick.

Wir empfehlen virtuelle Maschinen mit 2 GB RAM.

Nach der Installation müssen Sie ein Admin-Passwort festlegen, anschließend können Sie Verbindungen, Benutzer und Rollen verwalten sowie Berechtigungen vergeben.

## Abonnement und Lizenzierung
DbGate Azure kann über den Azure Marketplace abonniert werden, wobei sich der Preis nach der Anzahl der Prozessoren der gewählten virtuellen Maschine richtet.

Eine 30-tägige kostenlose Testversion gibt Ihnen Zugriff auf alle DbGate-Funktionen. Nach Ablauf der Testphase erfolgt die Abrechnung gemäß dem Azure-Preisplan entsprechend der gewählten Instanzgröße. Es ist keine zusätzliche Lizenzierung erforderlich, da alle Zahlungen über das Abonnement im [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview) abgewickelt werden.

## Updates von DbGate Azure
DbGate Azure verfügt über einen speziellen Build und läuft direkt auf dem virtuellen Server (es gibt keine zusätzliche Virtualisierungsschicht wie Docker). Es steht eine Auto-Upgrade-Funktion zur Verfügung – nach dem Start fragt der Container den neuesten Build ab und ersetzt die alte Version, sofern einer gefunden wird. Sie müssen kein manuelles Upgrade durchführen.

Wenn Sie manuell eine neue virtuelle Maschine mit einer neuen Version erstellen, erhält diese ihre eigene neue Datenbank (die interne MySQL-Datenbank ist Teil der virtuellen Maschine), sodass es keine einfache Möglichkeit gibt, Verbindungen und Benutzer auf die neue virtuelle Maschine zu übertragen.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate auf Azure{{< /button >}}
