---
sourceHash: 9faead63589d3a58402650e29cd85afd2223ffa5317dbd506eb962c893c3c04e
language: es
title: Comparar e implementar modelos
weight: 15
---

DbGate puede comparar la estructura de bases de datos e implementar cambios *(Premium)*. Esto resulta útil para mantener los entornos sincronizados y para controlar las versiones de tu esquema.

![Compare database](https://media.dbgate.io/img/compare-database-settings-light.png)

## Comparar bases de datos

* **Comparar dos bases de datos** - encuentra diferencias en columnas, definiciones de vistas y otros objetos SQL.
* **Sincronizar la estructura** - genera y ejecuta las acciones necesarias para que una base de datos coincida con otra.
* **Comparar con un modelo YAML** - compara una base de datos real con un modelo almacenado en YAML e implementa las diferencias.
* **Configuración** - controla la comparación, por ejemplo ignorar claves foráneas, excluir objetos concretos o elegir qué acciones de sincronización realizar.

## Exportar un modelo de base de datos

* **Generar en una carpeta** - guarda el modelo de una base de datos existente en una carpeta o en un único archivo JSON.
* **Archivos YAML de tablas** - las tablas se almacenan como sencillos archivos YAML que puedes mantener en un repositorio Git.
* **Archivos de definición SQL** - las vistas, los procedimientos almacenados y las funciones se almacenan como archivos SQL.

## Implementar

Implementa el modelo visualmente con la herramienta de comparación, o desde la línea de comandos como parte de una canalización de CI/CD. Para conocer el formato del archivo de modelo y el flujo de trabajo de la CLI, consulta [Implementación de bases de datos](dbdeploy).

## Páginas relacionadas

* [Editor de tablas y esquemas](schema-editor) - edita la estructura de las tablas mediante la interfaz gráfica
* [Implementación de bases de datos](dbdeploy) - formato del archivo de modelo e implementación desde la línea de comandos
