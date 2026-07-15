---
sourceHash: 747ba43f406b2590b6c5c5b4df2666c3064a1947eb2190c9b8fb634dc85b4085
language: pt
title: Implantação de banco de dados
weight: 10
---

*A funcionalidade de implantação será significativamente alterada na próxima versão, esta documentação refere-se à última versão BETA*

O DbGate oferece um mecanismo para implantação automática de banco de dados. Enquanto a forma tradicional de conseguir isso usa scripts SQL de migração, o DbGate usa por padrão uma abordagem diferente (scripts de migração também são suportados).
Você define o modelo do BD com arquivos YAML descrevendo a estrutura das tabelas e os dados de listas, e arquivos SQL descrevendo views, procedimentos armazenados e funções. Esse modelo é implantado no banco de dados, comparando a estrutura atual com a estrutura do modelo, criando colunas e tabelas ausentes e atualizando as definições de views e procedimentos. **Nenhuma ação destrutiva** (que poderia levar à perda de dados) é executada, então, quando você remove uma coluna ou tabela do modelo, ela permanece no banco de dados. Se você renomear uma coluna no modelo, uma nova coluna com o novo nome é criada e a coluna antiga permanece no banco de dados.

A implantação pode ser invocada a partir da linha de comando (usando scripts node) ou a partir da interface gráfica do DbGate. Você também pode usar a função de comparação de BD para comparar visualmente as diferenças entre o modelo e o banco de dados real.

## Formato yaml de tabela

```yaml
name: Album # table name 
columns:
  - name: AlbumId # column name 
    type: int # data type. is used directly in target SQL engine  
    autoIncrement: true # column is autoincrement 
    notNull: true # column is not nullable (default: is nullable) 
  - name: Title
    type: nvarchar(150)
    notNull: true
  - name: ArtistId
    type: int
    references: Artist # name of table. Is used for creating foreign key 
  - name: isDeleted
    type: bit
    notNull: true
    default: 0 # default value 
  - name: created
    type: timestamp
    default: current_timestamp
primaryKey:
  - AlbumId # list of primary key column names 
indexes:
  - name: UQ_AlbumTitleArtistId # index name 
    unique: true # whether index is unique. default=false 
    columns: # list of index columns 
      - Title
      - ArtistId
data: # static data (only for list tables) 
  - AlbumId: -1 # values for all columns, which should be filled 
    Title: Predefined static album
```

- Os nomes são definidos sem o nome do schema, um modelo descreve um schema
- Os valores padrão são definidos como expressões SQL, então, se você quiser definir uma string, deve usar 'aspas simples'
- Você pode definir dados estáticos para a tabela

### Uso de scripts de migração
Você pode combinar os scripts de migração mais tradicionais com o gerenciamento de implantação específico do DbGate; alguns objetos mais específicos podem ser criados com scripts de migração.
Os tipos de script são determinados pela extensão do arquivo, o layout dos diretórios é escolha do usuário, o DbGate não é afetado por isso.

As seguintes extensões de script são suportadas:
- `*.predeploy.sql` - scripts executados antes de cada processo de implantação
- `*.install.sql` - scripts executados somente se forem diferentes da implantação anterior
- `*.uninstall.sql` - este script é pareado com o arquivo `.install.sql`, é executado antes que a nova versão do arquivo `*.install.sql` seja executada
- `*.once.sql` - scripts executados apenas uma vez
- `*.postdeploy.sql` - scripts executados antes de cada processo de implantação

O DbGate usa a tabela `dbgate_deploy_journal` para rastrear os scripts de implantação aplicados ao banco de dados. Essa tabela é criada automaticamente quando você implanta qualquer projeto com pelo menos um script de migração.


### Uso na interface gráfica do DbGate

- Em conexões, no menu de contexto do banco de dados, escolha "Export DB model" (somente Premium). O modelo do BD é salvo em um diretório ou em um arquivo. Se você planeja usar a funcionalidade de implantação, escolha os destinos Data archive ou Folder (YAML + SQL).
- Abra o widget de arquivos (archives), você deverá ver o modelo baixado
- No menu de contexto do modelo, você pode realizar algumas operações com o modelo:
    - Generate deploy DB SQL - compara o banco de dados atual (você pode vê-lo na barra de status) e gera um script SQL, que implanta as alterações do modelo no banco de dados atual
    - Shell: Deploy DB - gera um shell JavaScript, que pode ser usado para implantar o BD
    - Compare with {current database} - compara graficamente o banco de dados atual com o modelo (somente Premium)

![screenshot](/img/exportdbmodel.png)

![screenshot](/img/archive-model.png)

### Uso a partir da linha de comando
Copie o script a seguir para o arquivo deploy.js e atualize a configuração do banco de dados. Você também deve alterar modelFolder, de acordo com a localização da pasta do seu modelo.  
A execução deste script requer o [NodeJs](https://nodejs.org/) instalado no seu computador.

```js
const path = require('path');
const dbgateApi = require('dbgate-api');
dbgateApi.initializeApiEnvironment();
const dbgatePluginPostgres = require('dbgate-plugin-postgres');
dbgateApi.registerPlugins(dbgatePluginPostgres);

async function run() {
	await dbgateApi.deployDb({
		connection: {
			server: process.env.DB_SERVER || 'localhost',
			engine: 'postgres@dbgate-plugin-postgres',
			password: process.env.DB_PASSWORD || 'test',
			user: process.env.DB_USER || 'postgres',
			port: process.env.DB_PORT || 5432,
			database: process.env.DB_NAME || 'my_database',
		},
		modelFolder: path.join(__dirname, 'database'),
	});
	await dbgateApi.finalizer.run();
	console.log('Finished job script');
}
dbgateApi.runScript(run);
```

Em seguida, instale os módulos necessários, executando os comandos no diretório com o deploy.js:
```sh
npm install dbgate-api
npm install dbgate-plugin-postgres
```

Execute a implantação do banco de dados com o comando:
```sh
node deploy.js
```

Este script é para PostgreSQL, outros mecanismos de banco de dados exigem alterações no driver.

Este script também pode ser gerado automaticamente a partir da interface gráfica do DbGate: use o menu de contexto "Shell: Deploy DB" na pasta do arquivo (archive), depois "Copy nodejs script" no script gerado copiará um script válido. Todos os pacotes usados no comando require devem ser instalados com npm install.
