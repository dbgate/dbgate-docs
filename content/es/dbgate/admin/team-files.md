---
sourceHash: 8396e36170a2f74ec485cc366db64869390b971ebf497d3127e7005ee1837c1d
language: es
title: Archivos de equipo
weight: 25
---

Los archivos de equipo son archivos SQL, de diagramas u otros archivos almacenados en el almacenamiento interno de DbGate. DbGate de escritorio guarda los archivos en la carpeta del usuario; la edición Team permite almacenar los archivos de la misma manera (en un volumen de docker), pero lo más adecuado es almacenarlos en la base de datos de almacenamiento, que no se vuelve a crear cuando se recrea el contenedor de DbGate.

- Archivos en disco
    - archivos almacenados en disco o en un volumen de docker
    - a menos que definas explícitamente un volumen de docker (por ejemplo, en docker-compose.yaml), los archivos se vuelven a crear cuando se recrea el contenedor.
- Archivos de equipo
    - archivos almacenados en la base de datos de almacenamiento
    - no se pierden cuando se recrea el contenedor, sin necesidad de definir un volumen de docker
    - permiten definir permisos de acceso detallados para usuarios y roles

## Guardar un archivo SQL como archivo de equipo
Al guardar un archivo SQL, simplemente marca la casilla "Save to team folder". El archivo se guardará como archivo de equipo.
