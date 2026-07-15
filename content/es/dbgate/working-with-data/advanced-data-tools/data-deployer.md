---
sourceHash: 813897622368b4a3dc176bd6e81b91d11c78d140ebe8055d76beb033560861d6
language: es
title: Implementador de datos
weight: 2
---

Con el implementador de datos, puede comparar y sincronizar visualmente sus datos en **carpetas de archivo** con una **base de datos real**
![DbGate data duplicator screenshot](https://media.dbgate.io/img/data-deployer-light.png)

## Ejecutar el implementador de datos
Puede ejecutar el implementador de datos desde el menú contextual de la base de datos o desde el menú contextual de la carpeta de archivo. Al ejecutarlo desde la base de datos, se le pedirá que elija un archivo. Al ejecutarlo desde el archivo, el implementador de datos se iniciará con la base de datos actual.

## Configuración
- Servidor de base de datos, base de datos - elija la base de datos con la que desea trabajar
- Archivo de datos - elija la carpeta con los datos que se utilizarán para comparar y sincronizar
### Relacionado con la tabla
- Clave (columnas de coincidencia) - elija las columnas que se utilizarán para hacer coincidir las filas entre la base de datos y el archivo
### Configuración del replicador
La configuración siguiente ("table" - deploy y la configuración global de implementación de datos) es específica del replicador y se describe en el tema [Replicador de datos](data-replicator)

## Copiar diferencias de datos
El implementador de datos muestra las diferencias entre los datos del archivo y los de la base de datos. Si selecciona algunas celdas con diferencias, puede escribir esas diferencias en el archivo o en la base de datos. Si estas celdas están seleccionadas, en la esquina inferior derecha aparecen botones que permiten la sincronización:
- Write x rows, y columns to archive - copia las celdas seleccionadas de la base de datos al archivo.
- Write x rows, y columns to database - copia las celdas seleccionadas del archivo a la base de datos. Primero se muestra un cuadro de diálogo de confirmación con el SQL de cambios.

## Acciones del replicador de datos
- Deploy into DB - esta acción implementa los cambios en la base de datos con la configuración establecida
- Generate shell - esta acción crea un archivo JavaScript que ejecutará la implementación. Este archivo se puede ejecutar desde la línea de comandos
- Generate SQL - crea el SQL que implementa los cambios del archivo en la base de datos

Más información sobre estas acciones en el tema [Replicador de datos](data-replicator)
