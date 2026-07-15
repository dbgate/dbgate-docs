---
sourceHash: 3dab8886ac4d4e94fd5a5f1cfcbccab5e941b303d64e8ba9fc96bc2ee264040b
language: pt
title: Navegador e editor de dados
weight: 5
---

O navegador de dados é a visualização principal do DbGate para consultar e editar dados de tabelas. Abra qualquer tabela, view ou coleção para obter uma grade rápida e semelhante ao Excel. Esta página aborda a navegação, a edição e o acesso a dados relacionados; para expressões de filtro, consulte [Filtragem de dados](data-filtering).

![Data browser](https://media.dbgate.io/img/common-data-browser-light.png)

## Navegando pelos dados

* **Navegação pelo teclado** - percorra a grade com as teclas de seta, como em uma planilha.
* **Ordenar** - clique no cabeçalho de uma coluna para ordenar por ela.
* **Filtrar** - filtre linhas usando a linha de filtro acima da grade; consulte [Filtragem de dados](data-filtering) para a sintaxe completa das expressões.
* **Gerenciador de colunas** - encontre colunas pelo nome e oculte as que você não precisa.
* **Cópia avançada** - copie as células selecionadas como CSV, YAML, `INSERT`s SQL ou inserts do MongoDB.

## Editando dados

A edição de dados funciona diretamente na grade:

* **Edição semelhante ao Excel** - edite células no próprio local; copie e cole intervalos de linhas, inclusive entre tabelas.
* **Alterações pendentes** - suas edições são reunidas como alterações pendentes. Revise o script SQL de alteração gerado antes que ele chegue ao banco de dados e, em seguida, salve ou reverta.
* **Inserir e excluir linhas** pela grade ou pelo menu de contexto.

![Save changes](https://media.dbgate.io/img/data-browser-save-changes-light.png)

### Macros do editor de dados *(Premium)*

Aplique macros predefinidas às células selecionadas - por exemplo, alterar a caixa do texto, remover diacríticos ou gerar um UUID.

## Trabalhando com dados relacionados

O DbGate facilita seguir as relações entre tabelas:

* **Dicas de relação** - veja um valor textual da tabela referenciada ao lado de uma chave estrangeira numérica.
* **Expansão de coluna de chave estrangeira** - expanda uma coluna de chave estrangeira para ver os dados referenciados na própria grade.
* **Abrir detalhe** - salte para a linha referenciada por uma chave estrangeira.
* **Visualizações mestre/detalhe** *(Premium)* - explore linhas relacionadas em um layout mestre/detalhe vinculado.

![Master/detail](https://media.dbgate.io/img/data-browser-master-detail-light.png)

## Visualização em formulário

A visualização em formulário mostra uma única linha como uma lista vertical, "transposta" - ideal para tabelas com muitas colunas. Ela funciona como uma visualização em árvore, de modo que colunas de chave estrangeira podem ser expandidas para explorar dados relacionados.

![Form view](https://media.dbgate.io/img/data-browser-form-view-light.png)

## Agrupamento *(Premium)*

Aplique agrupamento (`GROUP BY`) na visualização em grade para agregar linhas diretamente durante a navegação.

## Páginas relacionadas

* [Filtragem de dados](data-filtering) - sintaxe das expressões de filtro
* [Exportação e importação](export-import) - mova dados para dentro e para fora das tabelas
* [Perspectivas](perspectives) - visualizações aninhadas e somente leitura sobre dados relacionados complexos
* [Editor SQL](/pt/dbgate/sql-and-queries/sql-editor/) - edite os resultados de consultas da mesma forma *(Premium)*
