---
sourceHash: ba49d4bd53c041c5e042d07318208cea17d32dd6c3079b21b9e4072bc94c457f
language: es
title: Filtrado de datos
weight: 10
---

DbGate cuenta con un potente motor de filtrado de datos, que permite tanto un filtrado muy sencillo como condiciones complejas.

Los filtros de datos se pueden usar en muchos lugares de DbGate, pero el lugar más habitual es el filtrado de la cuadrícula de datos.

![filter screenshot](https://media.dbgate.io/img/data-browser-filter-light.png)

Los filtros se rellenan con un fondo de color:
* Fondo verde: el filtro es correcto y está aplicado
* Fondo rojo: hay un error en la expresión del filtro, el filtro se ignora

Tiene varias opciones para crear un filtro:
* {{< mdi "filter" >}} - muestra un menú con filtros y diálogos predefinidos
* {{< mdi "dots-vertical" >}} - le permite elegir los valores por los que filtrar
* Puede escribir el filtro directamente: use la sintaxis muy sencilla descrita en [filter-expressions](#filter-expressions)
* O puede crear el filtro con métodos visuales y editarlo manualmente

Otros comandos:
* {{< mdi "filter-off" >}} - borra todos los filtros

## Expresiones de filtro
Las expresiones de filtro están diseñadas para ser intuitivas; en la mayoría de los casos simplemente escribe directamente lo que quiere buscar. Sin embargo, la sintaxis es bastante potente, puede combinar varias condiciones y usar diversos operadores.
La sintaxis de la expresión depende del tipo de datos de la columna.

### Ejemplos

| Tipo de columna | Expresión de filtro |  Descripción |
|----------|-------------|------|
| string | canada | el valor de la columna contiene el texto "canada" |
| string | canada, usa | el valor de la columna contiene el texto "canada" o "usa" |
| string | canada lake | el valor de la columna contiene el texto "canada" y "lake" |
| string | NOT EMPTY NOT NULL | la cadena tiene un valor no vacío |
| number | >10 | el valor de la columna es mayor que 10 |
| number | >=5 <=10 | el valor de la columna está entre 5 y 10 |
| number | 1,2,3 | el valor de la columna es 1 o 2 o 3 |
| datetime | 2020-05-26 | el valor de fecha es del 2020-05-26 (intervalo de 24 horas)  |

### Filtros comunes (para todos los tipos de datos)
- NULL - el valor de la columna es nulo
- NOT NULL - el valor de la columna no es nulo
- {$$ is null} - condición SQL, escrita entre llaves {}. $$ es el marcador de posición de la columna filtrada

### Filtros de texto
La comparación de texto no distingue entre mayúsculas y minúsculas.
- text - el valor de la columna contiene _text_. Puede ir entre 'comillas simples' o "comillas dobles"
- +text - el valor de la columna contiene _text_ (igual que la línea anterior)
- ^text - el valor de la columna empieza por _text_
- $text - el valor de la columna termina en _text_
- !+text - el valor de la columna no contiene _text_ (igual que la línea anterior)
- !^text - el valor de la columna no empieza por _text_
- !$text - el valor de la columna no termina en _text_
- EMPTY - el valor de la columna no contiene ningún carácter que no sea un espacio en blanco
- NOT EMPTY - el valor de la columna contiene algún carácter que no es un espacio en blanco

### Filtros numéricos
- number - el valor de la columna es igual al número
- =number - el valor de la columna es igual al número
- !=number - el valor de la columna no es igual al número
- <>number - el valor de la columna no es igual al número
- <number - el valor de la columna es menor que el número
- \>number - el valor de la columna es mayor que el número
- <=number - el valor de la columna es menor o igual que el número
- \>=number - el valor de la columna es mayor o igual que el número

### Filtros de fecha y hora
- 2021 - año del valor de la columna
- 2021-02 - año y mes del valor de la columna
- 2021-02-15 - año, mes y día del valor de la columna
- 2021-02-15 23:15 - año, mes, día, hora y minuto del valor de la columna
- 2021-02-15 23:15:51 - año, mes, día, hora, minuto y segundo del valor de la columna
- Filtros relativos a la fecha actual
  - YESTERDAY
  - TODAY
  - TOMORROW
  - LAST WEEK
  - THIS WEEK
  - NEXT WEEK
  - LAST MONTH
  - THIS MONTH
  - NEXT MONTH
  - LAST YEAR
  - THIS YEAR
  - NEXT YEAR

### Filtros lógicos (booleanos)
- TRUE, true, 1 - el valor de la columna es true/1
- FALSE, false, 0 - el valor de la columna es false/0

### Combinaciones de filtros
Los filtros se pueden combinar entre sí. El espacio se interpreta como el operador AND y la coma como el operador OR. AND tiene mayor prioridad que OR.
