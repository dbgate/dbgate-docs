---
sourceHash: ba49d4bd53c041c5e042d07318208cea17d32dd6c3079b21b9e4072bc94c457f
language: pt
title: Filtragem de dados
weight: 10
---

O DbGate possui um poderoso mecanismo de filtragem de dados, permitindo tanto uma filtragem de dados muito simples quanto condições complexas.

Os filtros de dados podem ser usados em muitos lugares do DbGate, mas o lugar mais comum é a filtragem da grade de dados.

![filter screenshot](https://media.dbgate.io/img/data-browser-filter-light.png)

Os filtros são preenchidos com um fundo colorido:
* Fundo verde - o filtro está correto e foi aplicado
* Fundo vermelho - há um erro na expressão do filtro, o filtro é ignorado

Você tem várias opções para criar um filtro:
* {{< mdi "filter" >}} - mostra o menu com filtros e caixas de diálogo predefinidos
* {{< mdi "dots-vertical" >}} - permite escolher os valores a filtrar
* Você pode escrever o filtro diretamente - use a sintaxe muito simples descrita em [filter-expressions](#filter-expressions)
* Ou você pode criar o filtro com métodos visuais e editá-lo manualmente

Outros comandos:
* {{< mdi "filter-off" >}} - limpa todos os filtros

## Filter expressions
As expressões de filtro foram projetadas para serem intuitivas; na maioria dos casos, você simplesmente escreve diretamente o que deseja pesquisar. No entanto, a sintaxe é bastante poderosa, você pode combinar várias condições e usar diversos operadores.
A sintaxe da expressão depende do tipo de dados da coluna.

### Exemplos

| Tipo de coluna | Expressão de filtro |  Descrição |
|----------|-------------|------|
| string | canada | o valor da coluna contém o texto "canada" |
| string | canada, usa | o valor da coluna contém o texto "canada" ou "usa" |
| string | canada lake | o valor da coluna contém o texto "canada" e "lake" |
| string | NOT EMPTY NOT NULL | a string tem um valor não vazio |
| number | >10 | o valor da coluna é maior que 10 |
| number | >=5 <=10 | o valor da coluna está entre 5 e 10 |
| number | 1,2,3 | o valor da coluna é 1 ou 2 ou 3 |
| datetime | 2020-05-26 | o valor da data é de 2020-05-26 (intervalo de 24 horas)  |

### Filtros comuns (para todos os tipos de dados)
- NULL - o valor da coluna é nulo
- NOT NULL - o valor da coluna não é nulo
- {$$ is null} - condição SQL, escrita entre chaves {}. $$ é o espaço reservado para a coluna filtrada

### Filtros de texto
A comparação de texto não diferencia maiúsculas de minúsculas.
- text - o valor da coluna contém _text_. Pode estar entre 'aspas simples' ou "aspas duplas"
- +text - o valor da coluna contém _text_ (o mesmo que a linha acima)
- ^text - o valor da coluna começa com _text_
- $text - o valor da coluna termina com _text_
- !+text - o valor da coluna não contém _text_ (o mesmo que a linha acima)
- !^text - o valor da coluna não começa com _text_
- !$text - o valor da coluna não termina com _text_
- EMPTY - o valor da coluna não contém nenhum caractere que não seja espaço em branco
- NOT EMPTY - o valor da coluna contém algum caractere que não seja espaço em branco

### Filtros numéricos
- number - o valor da coluna é igual ao número
- =number - o valor da coluna é igual ao número
- !=number - o valor da coluna não é igual ao número
- <>number - o valor da coluna não é igual ao número
- <number - o valor da coluna é menor que o número
- \>number - o valor da coluna é maior que o número
- <=number - o valor da coluna é menor ou igual ao número
- \>=number - o valor da coluna é maior ou igual ao número

### Filtros de data e hora
- 2021 - ano do valor da coluna
- 2021-02 - ano, mês do valor da coluna
- 2021-02-15 - ano, mês, dia do valor da coluna
- 2021-02-15 23:15 - ano, mês, dia, hora, minuto do valor da coluna
- 2021-02-15 23:15:51 - ano, mês, dia, hora, minuto, segundo do valor da coluna
- Filtros relativos à data atual
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
- TRUE, true, 1 - o valor da coluna é true/1
- FALSE, false, 0 - o valor da coluna é false/0

### Combinações de filtros
Os filtros podem ser combinados entre si. O espaço é interpretado como o operador AND, a vírgula como o operador OR. AND tem prioridade maior que OR.
