---
sourceHash: f2791f82e04437cfea34f20ce37c68c887e87a2c0da52d28b9f823e0e184aab9
language: es
title: Temas personalizados
weight: 10
---

DbGate ofrece un soporte flexible de temas. Puedes crear tu propio tema, cambiando los colores de varios elementos de la interfaz.

Los temas se crean como archivos JSON. La forma más sencilla de crear un tema personalizado es usar el asistente de IA para temas.

## Asistente de IA para temas
Para invocar el asistente de IA para temas, abre Settings/Themes y luego haz clic en el botón "Customize with AI assistant".

![Theme settings](https://media.dbgate.io/img/app-settings-themes-light.png)

El asistente de IA para temas personalizará tu tema según tus instrucciones. Puedes especificar qué colores quieres cambiar y cómo. Por ejemplo, puedes decir "Make primary color green, and background color dark gray".

![screenshot](/screenshots/dbgate-green.png)

Generar un tema con el asistente de IA tarda unos minutos, ya que hay unas 280 variables que generar. Una vez generado el tema, puedes hacer clic en el botón "Apply Theme" para usar el nuevo tema. También puedes usar el botón "Save theme" para guardar el tema como archivo JSON. Todos los temas guardados están luego disponibles en el selector de temas. También puedes gestionar (renombrar, editar, eliminar) los temas en el widget de archivos {{< mdi "file" >}}.

## Compartir temas en DbGate Cloud
Puedes compartir tus temas con otros usuarios de DbGate mediante DbGate Cloud. Para compartir un tema, crea una pull request en el [repositorio de la base de conocimiento de DbGate](https://github.com/dbgate/dbgate-knowledge-base). Los temas se almacenan en el directorio folder-Themes. Consulta los temas existentes como ejemplos. Simplemente copia tu archivo JSON del tema a ese directorio y crea una pull request. Después de fusionar tu pull request, tu tema estará disponible para todos los usuarios de DbGate en el selector de temas.
