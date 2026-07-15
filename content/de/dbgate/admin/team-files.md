---
sourceHash: 8396e36170a2f74ec485cc366db64869390b971ebf497d3127e7005ee1837c1d
language: de
title: Team-Dateien
weight: 25
---

Team-Dateien sind SQL-, Diagramm- oder andere Dateien, die im internen Speicher von DbGate abgelegt werden. Die Desktop-Version von DbGate speichert Dateien im Benutzerordner, die Team-Edition erlaubt das Speichern von Dateien auf die gleiche Weise (in einem Docker-Volume), passender ist es jedoch, die Dateien in der Speicherdatenbank abzulegen, die nicht neu erstellt wird, wenn der DbGate-Container neu erstellt wird.

- Festplattendateien
    - Dateien, die auf der Festplatte oder in einem Docker-Volume gespeichert werden
    - sofern Sie kein Docker-Volume explizit definieren (z. B. in docker-compose.yaml), werden die Dateien neu erstellt, wenn der Container neu erstellt wird.
- Team-Dateien
    - Dateien, die in der Speicherdatenbank abgelegt werden
    - gehen beim Neuerstellen des Containers nicht verloren, ohne dass ein Docker-Volume definiert werden muss
    - ermöglichen die Definition fein abgestufter Zugriffsberechtigungen für Benutzer und Rollen

## SQL-Datei als Team-Datei speichern
Aktivieren Sie beim Speichern einer SQL-Datei einfach das Kontrollkästchen "Save to team folder". Die Datei wird als Team-Datei gespeichert.
