---
sourceHash: fd6032a57cb859a0d8cb5046fde87de9bf1a85de56c66586391e84ecbbdc24c1
language: de
title: Bereitstellung auf AWS
subtitle: Ein-Klick-Bereitstellung auf einem Amazon EC2-Cluster
icon: aws.svg
weight: 10
demo_url: https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy
demo_title: View on AWS
edition: 'premium'
---

Die DbGate AWS Edition ist eine kollaborative Mehrbenutzer-Webplattform, die speziell für die Datenbankverwaltung innerhalb von Amazon Web Services (AWS) entwickelt wurde. Durch die Nutzung der AWS-Infrastruktur vereinfacht sie die Teamarbeit für Organisationen, die in Cloud-Umgebungen arbeiten. Ihre gemeinsam genutzte, browserbasierte Oberfläche erleichtert die Zusammenarbeit, den Datenzugriff und die Datenbanküberwachung und lässt sich dabei nahtlos in AWS integrieren.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate auf AWS{{< /button >}}

## Wichtigste Funktionen von DbGate AWS
DbGate AWS unterstützt dieselben Funktionen wie DbGate Team Premium, ist jedoch für AWS optimiert

* Unterstützung für AWS IAM
* Verwaltung von Benutzern, Verbindungen und Rollen
* Durchsuchen, Filtern und Bearbeiten von Daten
* Import und Export von Daten
* Visueller Abfrage-Designer

## Installationsprozess
Die Installation auf AWS ist sehr unkompliziert, es ist nahezu ein Ein-Klick-Vorgang.

Wir empfehlen den Instanztyp t2.medium für die beste Benutzererfahrung, aber t2.micro, der im Free Tier verfügbar ist, reicht für eine kleine Anzahl von Benutzern aus.

Nach der Installation müssen Sie ein Admin-Passwort festlegen, anschließend können Sie Verbindungen, Benutzer und Rollen verwalten sowie Berechtigungen vergeben.

## Abonnement und Lizenzierung
DbGate AWS kann über den AWS Marketplace abonniert werden, wobei sich der Preis nach der Größe der gewählten Instanz richtet. Größere Instanzen unterstützen mehr gleichzeitige Benutzer.

Eine 30-tägige kostenlose Testphase gibt Ihnen Zugang zu allen DbGate-Funktionen. Nach der Testphase erfolgt die Abrechnung gemäß dem Preisplan von AWS entsprechend der gewählten Instanzgröße. Es ist keine zusätzliche Lizenzierung erforderlich, da alle Zahlungen über das Abonnement im [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy) abgewickelt werden.

## DbGate AWS-Updates
DbGate AWS verfügt über einen speziellen Build und läuft direkt auf einem virtuellen Server in EC2 (es gibt keine zusätzliche Virtualisierungsschicht wie Docker). Es gibt eine Auto-Upgrade-Funktion – nach dem Start fragt der Container nach dem neuesten Build und ersetzt, falls einer gefunden wird, die alte Version. Sie müssen kein manuelles Upgrade durchführen.

Wenn Sie manuell einen neuen EC2-Container mit einer neuen Version erstellen, erhält dieser seine eigene neue Datenbank (die interne MySQL-Datenbank ist Teil des Containers), sodass es keine einfache Möglichkeit gibt, Verbindungen und Benutzer auf den neuen EC2-Container zu übertragen.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate auf AWS{{< /button >}}
