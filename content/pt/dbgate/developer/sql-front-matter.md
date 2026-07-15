---
sourceHash: 07f2dbb06f919740569e0975a516c83ac340bda36ad1c3cd06455da1b904ba3a
language: pt
title: Front Matter SQL
weight: 50
---

O front matter SQL são metadados em formato YAML no início de um arquivo SQL. Esse conceito é inspirado no gohugo e no Jekyll, que introduziram o front matter para arquivos markdown. ([Front matter no Hugo](https://gohugo.io/content-management/front-matter/))

O front matter SQL começa logo no início do arquivo SQL com a marca `-- >>>` e termina com uma linha contendo apenas `-- <<<`. Cada linha do conteúdo YAML é precedida pelo prefixo `-- `, de modo que o arquivo inteiro continua sendo SQL válido.

Esses metadados são usados especialmente para gráficos (salvando a configuração do gráfico) e para atributos da base de conhecimento pública (como título e descrição do script). Mas também há alguns atributos utilizáveis em qualquer script SQL no DbGate.

## Atributos genéricos
- autoExecute: `true` ou `false`, define se o script será executado automaticamente ao ser aberto
- splitterInitialValue: porcentagem (como 20%) ou tamanho absoluto (como 220px) - use para definir o tamanho da área SQL superior. O restante será usado para o resultado da consulta

## Atributos da base de conhecimento pública
- title: título do script (padrão - nome do arquivo sem extensão)
- description: descrição do script (padrão - vazio)
- icon: ícone do script (dos [ícones Material design](https://pictogrammers.com/library/mdi/), no formato `mdi mdi-chart-pie`)

## Atributos de gráfico
- selected-chart: número (a partir de 1) do gráfico a ser selecionado automaticamente
- chart-N: definição do N-ésimo gráfico
    - title: título do gráfico
    - pieRatioLimit - limite para o gráfico de pizza; se o valor for menor que este, ele será agrupado em "Other" (padrão: 0.05)
    - pieCountLimit - limite para o número de fatias do gráfico de pizza; se o número de fatias for maior que este, elas serão agrupadas em "Other" (padrão: 10)
    - dataLabelFormatter - formatador do rótulo de dados, um dos valores 'number' | 'size:bytes' | 'size:kb' | 'size:mb' | 'size:gb'

Para a lista completa e atualizada de campos, você pode usar a [definição TypeScript](https://github.com/dbgate/dbgate/blob/master/packages/datalib/src/chartDefinitions.ts), veja a interface `ChartDefinition`

## Exemplo

```sql
-- >>>
-- selected-chart: 1
-- chart-1:
--   chartType: bar
--   xdef:
--     field: InvoiceDate
--     transformFunction: date:month
--   ydefs:
--     - field: Total
--       aggregateFunction: sum
-- <<<
SELECT
  `InvoiceId`,
  `CustomerId`,
  `InvoiceDate`,
  `BillingAddress`,
  `BillingCity`,
  `BillingState`,
  `BillingCountry`,
  `BillingPostalCode`,
  `Total`
FROM
  `Invoice`
```
