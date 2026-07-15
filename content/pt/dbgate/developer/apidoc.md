---
sourceHash: 0541c2f8694b4525ff4b57619bff1885d4fc5b0f11db4338772faefd109c393d
language: pt
layout: docs
title: Documentação da API
weight: 20
---

## Funções

<dl>
<dt><a href="#copyStream">copyStream(input, output, options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Copia o leitor para o gravador. Usado para importar, exportar tabelas e transferir dados entre tabelas</p>
</dd>
<dt><a href="#deployDb">deployDb(options)</a></dt>
<dd><p>Implanta no banco de dados o modelo de banco de dados armazenado em modelFolder (tabelas como YAMLs)</p>
</dd>
<dt><a href="#dropAllDbObjects">dropAllDbObjects(options)</a> ⇒ <code>Promise</code></dt>
<dd><p>Remove todos os objetos do banco de dados</p>
</dd>
<dt><a href="#executeQuery">executeQuery(options)</a></dt>
<dd><p>Executa uma consulta SQL</p>
</dd>
<dt><a href="#generateDeploySql">generateDeploySql(options)</a></dt>
<dd><p>Gera a consulta para implantar o modelo no banco de dados</p>
</dd>
<dt><a href="#jsonLinesReader">jsonLinesReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Função de leitura que lê um arquivo ou URL JSNOL. Formato JSONL - arquivo de texto em que cada linha é uma linha de dados codificada em JSON.</p>
</dd>
<dt><a href="#jsonLinesWriter">jsonLinesWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Retorna o objeto gravador para a função <a href="#copyStream">copyStream</a>. Esse objeto gravador grava dados em um arquivo JSONL. Formato JSONL - arquivo de texto em que cada linha é uma linha de dados codificada em JSON, usado, por exemplo, pelo MongoDB.</p>
</dd>
<dt><a href="#jsonReader">jsonReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Cria o objeto leitor de um arquivo JSON para a função <a href="#copyStream">copyStream</a>.</p>
</dd>
<dt><a href="#jsonWriter">jsonWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Retorna o objeto gravador para a função <a href="#copyStream">copyStream</a>. Esse objeto gravador grava dados em um arquivo JSON.</p>
</dd>
<dt><a href="#queryReader">queryReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Retorna o objeto leitor para a função <a href="#copyStream">copyStream</a>. Esse objeto leitor lê dados de uma consulta.</p>
</dd>
<dt><a href="#tableReader">tableReader(options)</a> ⇒ <code><a href="#readerType">Promise.&lt;readerType&gt;</a></code></dt>
<dd><p>Cria o objeto leitor para a função <a href="#copyStream">copyStream</a>. Esse objeto leitor lê dados de uma tabela ou visão.</p>
</dd>
<dt><a href="#tableWriter">tableWriter(options)</a> ⇒ <code><a href="#writerType">Promise.&lt;writerType&gt;</a></code></dt>
<dd><p>Cria o objeto gravador para a função <a href="#copyStream">copyStream</a>. Esse objeto gravador grava dados em uma tabela. A tabela pode ser criada caso não exista.</p>
</dd>
</dl>

## Typedefs

<dl>
<dt><a href="#readerType">readerType</a> : <code>Object</code></dt>
<dd><p>Objeto leitor (entrada) para a função <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#writerType">writerType</a> : <code>Object</code></dt>
<dd><p>Objeto gravador (saída) para a função <a href="#copyStream">copyStream</a></p>
</dd>
<dt><a href="#engineType">engineType</a> : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> | <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> | <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> | <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> | <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> | <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> | <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> | <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> | <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> | <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> | <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> | <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> | <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> | <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code></dt>
<dd><p>Tipo de função de usuário.</p>
</dd>
<dt><a href="#connectionType">connectionType</a> : <code>Object</code></dt>
<dd></dd>
</dl>

<a name="copyStream"></a>

## copyStream(input, output, options) ⇒ <code>Promise</code>
Copia o leitor para o gravador. Usado para importar, exportar tabelas e transferir dados entre tabelas

**Tipo**: função global  

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| input | [<code>readerType</code>](#readerType) | objeto leitor |
| output | [<code>writerType</code>](#writerType) | objeto gravador |
| options | <code>object</code> | opções |

<a name="deployDb"></a>

## deployDb(options)
Implanta no banco de dados o modelo de banco de dados armazenado em modelFolder (tabelas como YAMLs)

**Tipo**: função global  

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objeto de conexão |
| options.systemConnection | <code>object</code> | conexão de sistema (resultado de driver.connect). Se não for informada, uma nova conexão será criada |
| options.driver | <code>object</code> | objeto de driver. Se não for informado, será carregado a partir da conexão |
| options.analysedStructure | <code>object</code> | estrutura analisada do banco de dados. Se não for informada, será carregada |
| options.modelFolder | <code>string</code> | pasta com os arquivos do modelo (arquivos YAML para tabelas, arquivos SQL para visões, procedimentos, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | modelo de banco de dados carregado - coleção de arquivos YAML e SQL carregados em um array |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | array de funções para transformar o modelo |
| options.dbdiffOptionsExtra | <code>object</code> | opções extras para o dbdiff |
| options.ignoreNameRegex | <code>string</code> | regex para ignorar objetos por nome |
| options.targetSchema | <code>string</code> | esquema de destino da implantação |
| options.maxMissingTablesRatio | <code>number</code> | proporção máxima de tabelas ausentes no banco de dados. Verificação de segurança: se a proporção de ausentes for maior, a implantação é interrompida (evitando a remoção acidental de todas as tabelas) |

<a name="dropAllDbObjects"></a>

## dropAllDbObjects(options) ⇒ <code>Promise</code>
Remove todos os objetos do banco de dados

**Tipo**: função global  

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objeto de conexão |
| options.systemConnection | <code>object</code> | conexão de sistema (resultado de driver.connect). Se não for informada, uma nova conexão será criada |
| options.driver | <code>object</code> | objeto de driver. Se não for informado, será carregado a partir da conexão |
| options.analysedStructure | <code>object</code> | estrutura analisada do banco de dados. Se não for informada, será carregada |

<a name="executeQuery"></a>

## executeQuery(options)
Executa uma consulta SQL

**Tipo**: função global  

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| options | <code>object</code> |  |
| [options.connection] | [<code>connectionType</code>](#connectionType) | objeto de conexão |
| [options.systemConnection] | <code>object</code> | conexão de sistema (resultado de driver.connect). Se não for informada, uma nova conexão será criada |
| [options.driver] | <code>object</code> | objeto de driver. Se não for informado, será carregado a partir da conexão |
| [options.sql] | <code>string</code> | consulta SQL |
| [options.sqlFile] | <code>string</code> | arquivo SQL |
| [options.logScriptItems] | <code>boolean</code> | se deve registrar os itens do script em vez do script inteiro |

<a name="generateDeploySql"></a>

## generateDeploySql(options)
Gera a consulta para implantar o modelo no banco de dados

**Tipo**: função global  

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objeto de conexão |
| options.systemConnection | <code>object</code> | conexão de sistema (resultado de driver.connect). Se não for informada, uma nova conexão será criada |
| options.driver | <code>object</code> | objeto de driver. Se não for informado, será carregado a partir da conexão |
| options.analysedStructure | <code>object</code> | estrutura analisada do banco de dados. Se não for informada, será carregada |
| options.modelFolder | <code>string</code> | pasta com os arquivos do modelo (arquivos YAML para tabelas, arquivos SQL para visões, procedimentos, ...) |
| options.loadedDbModel | <code>Array.&lt;object&gt;</code> | modelo de banco de dados carregado - coleção de arquivos YAML e SQL carregados em um array |
| options.modelTransforms | <code>Array.&lt;function()&gt;</code> | array de funções para transformar o modelo |
| options.dbdiffOptionsExtra | <code>object</code> | opções extras para o dbdiff |
| options.ignoreNameRegex | <code>string</code> | regex para ignorar objetos por nome |
| options.targetSchema | <code>string</code> | esquema de destino da implantação |
| options.maxMissingTablesRatio | <code>number</code> | proporção máxima de tabelas ausentes no banco de dados. Verificação de segurança: se a proporção de ausentes for maior, a implantação é interrompida (evitando a remoção acidental de todas as tabelas) |

<a name="jsonLinesReader"></a>

## jsonLinesReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Função de leitura que lê um arquivo ou URL JSNOL. Formato JSONL - arquivo de texto em que cada linha é uma linha de dados codificada em JSON.

**Tipo**: função global  
**Retorna**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objeto leitor  

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| options | <code>Object</code> |  |
| options.fileName | <code>string</code> | nome do arquivo ou URL |
| options.encoding | <code>string</code> | codificação do arquivo |
| options.limitRows | <code>number</code> | número máximo de linhas a ler |

<a name="jsonLinesWriter"></a>

## jsonLinesWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Retorna o objeto gravador para a função [copyStream](#copyStream). Esse objeto gravador grava dados em um arquivo JSONL. Formato JSONL - arquivo de texto em que cada linha é uma linha de dados codificada em JSON, usado, por exemplo, pelo MongoDB.

**Tipo**: função global  
**Retorna**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - objeto gravador  

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | nome do arquivo |
| [options.encoding] | <code>string</code> | codificação do arquivo |
| [options.header] | <code>boolean</code> | se deve gravar o cabeçalho. O cabeçalho é um JSON que descreve a estrutura da tabela de origem. O cabeçalho é específico do DbGate; se você quiser, por exemplo, importar dados para o MongoDB, não deve gravar o cabeçalho. |

<a name="jsonReader"></a>

## jsonReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Cria o objeto leitor de um arquivo JSON para a função [copyStream](#copyStream).

**Tipo**: função global  
**Retorna**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objeto leitor  

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | nome do arquivo ou URL |
| options.jsonStyle | <code>string</code> | 'object' ou 'array' |
| [options.keyField] | <code>string</code> | campo de chave para o estilo object |
| [options.rootField] | <code>string</code> | campo raiz para o estilo object |
| [options.encoding] | <code>string</code> | codificação do arquivo |
| [options.limitRows] | <code>number</code> | número máximo de linhas a ler |

<a name="jsonWriter"></a>

## jsonWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Retorna o objeto gravador para a função [copyStream](#copyStream). Esse objeto gravador grava dados em um arquivo JSON.

**Tipo**: função global  
**Retorna**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - objeto gravador  

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.fileName | <code>string</code> | nome do arquivo |
| [options.jsonStyle] | <code>string</code> | 'object' ou 'array' |
| [options.keyField] | <code>string</code> | campo de chave para o estilo object |
| [options.rootField] | <code>string</code> | campo raiz para o estilo object |
| [options.encoding] | <code>string</code> | codificação do arquivo |

<a name="queryReader"></a>

## queryReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Retorna o objeto leitor para a função [copyStream](#copyStream). Esse objeto leitor lê dados de uma consulta.

**Tipo**: função global  
**Retorna**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objeto leitor  

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objeto de conexão |
| options.query | <code>string</code> | consulta SQL |
| [options.queryType] | <code>string</code> | tipo de consulta |
| [options.sql] | <code>string</code> | consulta SQL. obsoleto; use query em vez disso |

<a name="tableReader"></a>

## tableReader(options) ⇒ [<code>Promise.&lt;readerType&gt;</code>](#readerType)
Cria o objeto leitor para a função [copyStream](#copyStream). Esse objeto leitor lê dados de uma tabela ou visão.

**Tipo**: função global  
**Retorna**: [<code>Promise.&lt;readerType&gt;</code>](#readerType) - - objeto leitor  

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objeto de conexão |
| options.systemConnection | <code>object</code> | conexão de sistema (resultado de driver.connect). Se não for informada, uma nova conexão será criada |
| options.pureName | <code>string</code> | nome da tabela |
| options.schemaName | <code>string</code> | nome do esquema |

<a name="tableWriter"></a>

## tableWriter(options) ⇒ [<code>Promise.&lt;writerType&gt;</code>](#writerType)
Cria o objeto gravador para a função [copyStream](#copyStream). Esse objeto gravador grava dados em uma tabela. A tabela pode ser criada caso não exista.

**Tipo**: função global  
**Retorna**: [<code>Promise.&lt;writerType&gt;</code>](#writerType) - - objeto gravador  

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| options | <code>object</code> |  |
| options.connection | [<code>connectionType</code>](#connectionType) | objeto de conexão |
| options.systemConnection | <code>object</code> | conexão de sistema (resultado de driver.connect). Se não for informada, uma nova conexão será criada |
| options.driver | <code>object</code> | objeto de driver. Se não for informado, será carregado a partir da conexão |
| options.pureName | <code>string</code> | nome da tabela |
| options.schemaName | <code>string</code> | nome do esquema |
| options.dropIfExists | <code>boolean</code> | remover a tabela se existir |
| options.truncate | <code>boolean</code> | truncar a tabela antes da inserção |
| options.createIfNotExists | <code>boolean</code> | criar a tabela se não existir |
| options.commitAfterInsert | <code>boolean</code> | confirmar a transação após a inserção |

<a name="readerType"></a>

## readerType : <code>Object</code>
Objeto leitor (entrada) para a função [copyStream](#copyStream)

**Tipo**: typedef global  
<a name="writerType"></a>

## writerType : <code>Object</code>
Objeto gravador (saída) para a função [copyStream](#copyStream)

**Tipo**: typedef global  
<a name="engineType"></a>

## engineType : <code>&#x27;mysql@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;mariadb@dbgate-plugin-mysql&#x27;</code> \| <code>&#x27;postgres@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;cockroach@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;redshift@dbgate-plugin-postgres&#x27;</code> \| <code>&#x27;sqlite@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;libsql@dbgate-plugin-sqlite&#x27;</code> \| <code>&#x27;oracle@dbgate-plugin-oracle&#x27;</code> \| <code>&#x27;mssql@dbgate-plugin-mssql&#x27;</code> \| <code>&#x27;mongo@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;mongo-legacy@dbgate-plugin-mongo&#x27;</code> \| <code>&#x27;cassandra@dbgate-plugin-cassandra&#x27;</code> \| <code>&#x27;clickhouse@dbgate-plugin-clickhouse&#x27;</code> \| <code>&#x27;redis@dbgate-plugin-redis&#x27;</code> \| <code>&#x27;duckdb@dbgate-plugin-duckdb&#x27;</code> \| <code>&#x27;firebird@dbgate-plugin-firebird&#x27;</code> \| <code>&#x27;cosmosdb@dbgate-plugin-cosmosdb&#x27;</code> \| <code>&#x27;dynamodb@dbgate-plugin-dynamodb&#x27;</code> \| <code>&#x27;firestore@dbgate-plugin-firestore&#x27;</code>
O identificador do mecanismo de banco de dados, no formato `engine@plugin-package`.

**Tipo**: typedef global  
<a name="connectionType"></a>

## connectionType : <code>Object</code>
**Tipo**: typedef global  
**Propriedades**

| Nome | Tipo |
| --- | --- |
| engine | [<code>engineType</code>](#engineType) | 
| server | <code>string</code> | 
| user | <code>string</code> | 
| password | <code>string</code> | 
| database | <code>string</code> | 
| port | <code>string</code> | 

