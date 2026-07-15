---
sourceHash: 0f10d627c0492363d84834c24da993d0686916c833728726a2d34648885161b1
language: es
title: Editor de tablas y esquemas
weight: 5
---

DbGate puede crear y modificar la estructura de la base de datos mediante una interfaz gráfica, sin escribir DDL a mano. Abre el editor de estructura de una tabla desde su menú contextual ("Edit table") o crea una nueva tabla desde el menú contextual de la base de datos.

![Table structure editor](https://media.dbgate.io/img/table-structure-editor-light.png)

## Edición de tablas

* **Columnas y tipos de datos** - define columnas, tipos de datos, nulabilidad y valores predeterminados para tablas nuevas o existentes.
* **Claves e índices** - gestiona claves primarias, claves foráneas e índices.
* **Propiedades específicas del motor** - configura opciones específicas de la base de datos, como el motor de tablas de MySQL.

## Vista previa de SQL y cambios seguros

* **Vista previa de SQL** - antes de guardar nada, DbGate muestra el SQL generado para que puedas revisarlo.
* **Advertencia de recreación de tabla** - cuando un cambio requiere recrear la tabla (una limitación de algunas bases de datos), DbGate te avisa y te permite inspeccionar primero el script generado.

## Otros objetos de base de datos

También puedes crear, eliminar y modificar otros objetos - vistas, procedimientos almacenados y funciones - y explorar tablas, vistas, procedimientos, funciones y colecciones de MongoDB desde el árbol de objetos.

## Páginas relacionadas

* [Comparar y desplegar modelos](model-compare-deploy) - compara la estructura entre bases de datos y despliega los cambios *(Premium)*
* [Despliegue de base de datos](dbdeploy) - archivos de modelo YAML/SQL y despliegue desde la CLI
