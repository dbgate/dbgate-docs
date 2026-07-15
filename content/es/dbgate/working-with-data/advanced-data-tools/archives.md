---
sourceHash: 80df2a73525118cee579014e200ff5f67715aa6f35468656abb3f8b70c254566
language: es
title: Archivos de datos
weight: 1
---

Los archivos son carpetas con datos en formato JSONL (NDJSON). DbGate permite trabajar con ellos de forma muy eficiente: puedes importarlos a una base de datos, exportarlos a otros formatos o editar directamente los datos del archivo. Un archivo se comporta como una base de datos muy rápida y ligera almacenada en ficheros locales.

## Formato JSONL
DbGate utiliza el formato JSONL internamente en todas partes. JSONL es un fichero de texto en el que cada línea contiene una fila serializada como JSON. DbGate asume que la primera línea puede contener una cabecera (también como JSON) con la estructura de la tabla. Cuando usas JSONL con estructura dinámica (sin la primera línea fija), este formato está estandarizado y se puede cargar en muchas otras herramientas.

## Carpetas de archivos
Un archivo está organizado en carpetas con ficheros JSONL. Tiene una estructura similar a la de una base de datos. Así puedes exportar toda una base de datos a un nuevo archivo: cada tabla se exporta a un fichero JSON y, gracias a la línea de cabecera, la estructura de la tabla también se conserva.

## Ver y editar ficheros de archivo
Puedes abrir los ficheros JSONL en diferentes modos:
- menú contextual "Open" - abre la cuadrícula de datos, que permite ordenar, filtrar y editar tus datos JSONL
- menú contextual "Open in text editor" - permite editar manualmente el fichero JSONL

## Archivos y modelos de BD
Las carpetas de archivos también se usan como almacenamiento para modelos de BD. Puedes exportar el modelo de BD desde el menú contextual de la base de datos, "Export DB model". Después puedes editar este modelo (ficheros YAML para la estructura de tablas, ficheros SQL para vistas y procedimientos almacenados), compararlo con la base de datos real y desplegarlo en la base de datos
