---
sourceHash: f2791f82e04437cfea34f20ce37c68c887e87a2c0da52d28b9f823e0e184aab9
language: de
title: Eigene Designs
weight: 10
---

DbGate bietet eine flexible Design-Unterstützung. Sie können Ihr eigenes Design erstellen und dabei die Farben verschiedener UI-Elemente ändern.

Designs werden als JSON-Dateien erstellt. Der einfachste Weg, ein eigenes Design zu erstellen, ist die Verwendung des KI-Assistenten für Designs.

## KI-Assistent für Designs
Um den KI-Assistenten für Designs aufzurufen, öffnen Sie Einstellungen/Designs und klicken Sie dann auf die Schaltfläche "Customize with AI assistant".

![Theme settings](https://media.dbgate.io/img/app-settings-themes-light.png)

Der KI-Assistent für Designs passt Ihr Design gemäß Ihren Anweisungen an. Sie können angeben, welche Farben Sie ändern möchten und wie. Sie könnten zum Beispiel sagen: "Mache die Primärfarbe grün und die Hintergrundfarbe dunkelgrau".

![screenshot](/screenshots/dbgate-green.png)

Das Generieren eines Designs mit dem KI-Assistenten dauert einige Minuten, da etwa 280 Variablen erzeugt werden müssen. Nachdem das Design generiert wurde, können Sie auf die Schaltfläche "Apply Theme" klicken, um das neue Design zu verwenden. Sie können auch die Schaltfläche "Save theme" verwenden, um das Design als JSON-Datei zu speichern. Alle gespeicherten Designs stehen anschließend in der Design-Auswahl zur Verfügung. Sie können Designs außerdem im Dateien-Widget {{< mdi "file" >}} verwalten (umbenennen, bearbeiten, löschen).

## Designs in DbGate Cloud teilen
Sie können Ihre Designs über DbGate Cloud mit anderen DbGate-Benutzern teilen. Um ein Design zu teilen, erstellen Sie einen Pull Request im [DbGate Knowledge-Base-Repository](https://github.com/dbgate/dbgate-knowledge-base). Designs werden im Verzeichnis folder-Themes gespeichert. Sehen Sie sich die vorhandenen Designs als Beispiele an. Kopieren Sie einfach Ihre Design-JSON-Datei in dieses Verzeichnis und erstellen Sie einen Pull Request. Nach dem Zusammenführen Ihres Pull Requests steht Ihr Design allen DbGate-Benutzern in der Design-Auswahl zur Verfügung.
