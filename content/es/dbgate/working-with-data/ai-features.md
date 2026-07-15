---
sourceHash: 22f2bb33edfa72684bb05dbcccca0a7b4f618485c77b184b851a079c9a3b7aff
language: es
title: Funciones de IA
weight: 55
---

DbGate incluye varias funciones basadas en IA *(Premium y Team Premium)*. Están disponibles para todos los usuarios de Premium sin necesidad de claves de API ni configuración: DbGate utiliza su propia pasarela de IA, que reenvía las solicitudes al proveedor del LLM.

![Database chat](https://media.dbgate.io/img/database-chat-light.png)

## Chat de base de datos

El chat de base de datos es un chatbot con IA que comprende tanto el esquema de tu base de datos como sus datos.

* **Conversación natural**: haz preguntas en cualquier lenguaje natural y obtén respuestas o SQL listo para ejecutar.
* **Consciente del contexto**: el modelo conoce tu esquema y (con permiso) los datos en vivo, por lo que sugiere joins, filtros y agregaciones correctos.
* **Iterativo**: refina con comandos como "añade un filtro de fecha" o "agrupa por cliente" y la consulta se actualiza al instante.
* **Gráficos**: pide un gráfico de barras, circular o de líneas creado a partir de los resultados.
* **Modo consultor**: puede analizar procedimientos almacenados y vistas, de modo que puedes preguntar cosas como "Explica el procedimiento X" o "Qué tablas se ven afectadas por el procedimiento Y". DbGate muestra qué objetos se analizaron.

### Ejecución de SQL: la seguridad primero

El chat de base de datos puede ejecutar SQL para responder preguntas. Tú eliges cómo:

* **Preguntar antes de ejecutar SQL (predeterminado)**: DbGate pregunta antes de ejecutar cada consulta.
* **Ejecutar SQL automáticamente**: las consultas que no son `SELECT` siguen requiriendo confirmación.
* **Nunca ejecutar, solo sugerir SQL**: el chat solo muestra las consultas; no se envía ningún dato de tu base de datos al LLM.

Si una consulta sugerida falla, DbGate envía el error de vuelta al modelo, que normalmente corrige la consulta automáticamente.

## Asistente de IA para SQL

Usa el chat como asistente de SQL ("Escribe una consulta SQL para los 10 principales clientes por ventas") y abre el resultado en una pestaña del [editor SQL](/es/dbgate/sql-and-queries/sql-editor/).

## Explicar error de SQL

Haz clic en **Explicar** junto a un mensaje de error para obtener una explicación de la IA sobre qué salió mal y cómo solucionarlo.

![Explain query error](https://media.dbgate.io/img/explain-query-error-light.png)

## Asistente de IA para temas

La IA también puede generar temas de color personalizados: consulta [Temas personalizados](/es/dbgate/customization/custom-themes/).

## Desactivar las funciones de IA

Las funciones de IA se pueden desactivar por completo (por ejemplo, en entornos restringidos) desde la configuración de DbGate.
