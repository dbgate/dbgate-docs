---
sourceHash: e10360d65315ca6bef22d826b37ec0f1623808453e37fd5d2a391f720399cc17
language: de
title: Plugin-Entwicklung
weight: 30
---

DbGate unterstützt das Erstellen von Plugins. Dank des Plugin-Assistenten ist es wirklich einfach, ein grundlegendes Plugin zu erstellen. DbGate-Plugins sind NPM-Pakete (JavaScript), sie können Abhängigkeiten haben. (aber keine nativen Abhängigkeiten)

Derzeit gibt es 3 Arten von Plugins:
- Theme-Plugin
- Dateiformat-Plugin
- Datenbanktreiber-Plugin

## Voraussetzungen installieren
Sie benötigen eine Installation von [node.js](https://nodejs.org). 

Außerdem benötigen Sie [Yeoman](https://yeoman.io/) und den Yeoman-[DbGate-Plugin-Generator](https://www.npmjs.com/package/generator-dbgate):

```sh
npm install -g yo
npm install -g generator-dbgate
```

## Plugin erstellen
Führen Sie den folgenden Befehl in der Konsole aus:

```sh
yo dbgate
```

Sie müssen 3 Fragen beantworten:
- Plugin-Name, muss mit dbgate-plugin- beginnen, z. B. dbgate-plugin-myplugin
- Plugin-Typ, wählen Sie z. B. "Database driver"
- Paketmanager, wählen Sie npm oder yarn, je nach Vorliebe. DbGate verwendet yarn.

## Plugin bearbeiten und testen
Öffnen Sie einen Editor, empfohlen wird [Visual Studio Code](https://code.visualstudio.com/)  . 
Ein Theme-Plugin enthält nur eine Quelldatei, src/index.js. Sie können die Theme-Farben nach Belieben anpassen. Das Attribut themeName ist der Name, der in der Theme-Auswahl von DbGate angezeigt wird.

Wenn Sie Ihr neues Theme sehen möchten, führen Sie dies in der Konsole aus (aus dem Plugin-Verzeichnis):
```sh
yarn plugin
```
oder, wenn Sie npm verwenden, dann
```sh
npm run plugin
```
Dieser Befehl installiert Ihr Plugin in der lokal installierten DbGate-Instanz (oder aktualisiert es, wenn Sie Änderungen vornehmen). Nach einem Neustart von DbGate sollten Sie das neue Theme sehen.  
Ein Neustart ist nicht erforderlich, das Neuladen der App (Menü Ansicht/Neu laden) genügt, um nach dem Ausführen von "yarn plugin" die neue Plugin-Version zu verwenden.

## Plugin entfernen
Sie können ein Plugin über das Plugins-Widget von DbGate deinstallieren. Oder mit dem folgenden Befehl:
```sh
yarn plugout
```

## Plugin veröffentlichen
Ein Plugin ist ein normales NPM-Paket, Sie können es im NPM-Repository veröffentlichen. Nach der Veröffentlichung steht es allen DbGate-Benutzern im Widget "Plugins" zur Verfügung.

## Plugin-Symbol
Jedes Plugin wird in der Erweiterungsliste durch ein Symbol dargestellt. NPM unterstützt keine Symbole für NPM-Pakete, daher kann das Symbol im Feld description in der Datei package.json mit folgender Syntax angegeben werden:

```
    "description": "Any description ![icon](https://link_to_icon.svg)",
```

Wenn Sie den Yeoman-Generator verwenden, hilft er Ihnen dabei ein wenig.

## Datenbanktreiber-Plugin erstellen
Das Erstellen eines Treiber-Plugins ist dem Erstellen sehr ähnlich, Sie wählen lediglich "Database driver plugin". Nach `yarn plugin` sollten Sie in der Lage sein, eine Verbindung mit Ihrem neuen Treiber zu definieren und eine Dummy-Datenbankliste sowie Tabellenliste zu sehen.

Sie können sehr schnell einen einfachen Treiber mit Grundfunktionalität erstellen, komplexere Funktionen können später implementiert werden.

Das Erstellen eines Treibers kann aus folgenden Schritten bestehen:
* ein geeignetes nodejs-Paket (Treiber) finden. Wählen Sie nach Möglichkeit ein reines JavaScript-Paket. Native Pakete sind eine große Komplikation, dieses native Paket muss der DbGate-Distribution hinzugefügt werden, außerdem können Sie mit Problemen beim Build auf verschiedenen Plattformen rechnen. Auf der anderen Seite funktionieren reine JavaScript-Pakete normalerweise problemlos auf allen Plattformen, ohne dass DbGate geändert werden muss.
* Felder für die Verbindung in frontend/driver.js definieren, Funktion showConnectionField
* die Funktion connect in backend/driver.js implementieren
* die Funktion getVersion in backend/driver.js implementieren (optional, aber wenn dies erledigt ist, können Sie die Verbindung jetzt mit der Schaltfläche "Test" im Verbindungstab testen)
* die Methode _rynAnalysis in der Klasse backend/Analyser.js implementieren. Diese Methode sollte die Datenbankstruktur zurückgeben.
* die Methode query in backend/driver.js implementieren. Danach sollten Sie in der Lage sein, die Tabellenliste anzuzeigen und Tabellendaten zu durchsuchen
* weitere Methoden implementieren. Bitte verwenden Sie andere Treiber-Plugins als Inspiration, das typischste Plugin ist wahrscheinlich das PostgreSQL-Plugin, https://github.com/dbgate/dbgate/tree/master/plugins/dbgate-plugin-postgres
