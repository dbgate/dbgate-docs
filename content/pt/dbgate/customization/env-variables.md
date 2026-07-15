---
sourceHash: 6a778b62fabbf4d369471e1389f59f802cd10bfc93f10385cb07ce401a02c972
language: pt
title: Variáveis de ambiente
weight: 20
---

A configuração por meio de variáveis de ambiente pode ser usada em containers docker, e também ao usar o pacote npm. O pacote NPM suporta arquivos .env.
  * [dbgate-serve](https://www.npmjs.com/package/dbgate-serve) - pacote NPM para a edição Community
  * [dbgate-serve-premium](https://www.npmjs.com/package/dbgate-serve-premium) - pacote NPM para a edição Premium
  * [dbgate/dbgate](https://hub.docker.com/r/dbgate/dbgate) - imagem Docker para a edição Community
  * [dbgate/dbgate-premium](https://hub.docker.com/r/dbgate/dbgate-premium) - imagem Docker para a edição Premium

## Edição Premium vs Team Community
A edição Community (FOSS) usa apenas a configuração das variáveis de ambiente listadas abaixo. A edição Team Premium usa armazenamento em banco de dados para as configurações, com [interface de administração](/pt/features/administration); apenas algumas configurações básicas são definidas por variáveis de ambiente.

## Configuração da edição Team Premium
Estas variáveis estão disponíveis apenas na edição Team Premium.
  * STORAGE_SERVER - servidor de banco de dados (nome do host) para o banco de dados de armazenamento
  * STORAGE_USER - usuário do banco de dados
  * STORAGE_PASSWORD - senha do banco de dados
  * STORAGE_PORT - porta do banco de dados (opcional. Se omitida, é usada a porta padrão do mecanismo de banco de dados selecionado)
  * STORAGE_DATABASE - nome do banco de dados de armazenamento
  * STORAGE_SCHEMA - schema do banco de dados de armazenamento (opcional, ex. para PostgreSQL (tipicamente public) ou MS SQL (tipicamente dbo))
  * STORAGE_ENGINE - mecanismo usado para o banco de dados de armazenamento. Atualmente, MySQL, PostgreSQL, SQL Server e Oracle. Use um dos seguintes valores:
    * mysql@dbgate-plugin-mysql
    * postgres@dbgate-plugin-postgres
    * mssql@dbgate-plugin-mssql
    * oracle@dbgate-plugin-oracle
  * ADMIN_PASSWORD - senha do administrador. A administração está disponível na URL https://dbgate_url/admin.html. Se a senha não for definida e STORAGE_DATABASE estiver definida, o DbGate solicitará a senha de administrador na primeira vez.
  * DBGATE_LICENSE - chave de licença do DbGate. Entre em contato com sales@dbgate.eu para obter uma licença de avaliação. Se não for definida, o DbGate Premium solicitará a licença na primeira vez. O DbGate Community não exige nenhuma licença.
  
### Parâmetros adicionais de conexão do armazenamento
  * STORAGE_SOCKET_PATH - caminho do socket para a conexão de armazenamento
  * STORAGE_DATABASE_URL - URL do banco de dados para a conexão de armazenamento
  * STORAGE_AUTH_TYPE - tipo de autenticação para a conexão de armazenamento. Os valores são os mesmos da variável AUTH_TYPE_xxx
  * STORAGE_USE_SSL - defina o valor 1 ou true quando SSL deve ser usado
  * STORAGE_KEY_FILE - caminho para o arquivo de chave
  * STORAGE_KEY_FILE_PASSWORD - senha do arquivo de chave
  * STORAGE_SSL_CA_FILE - caminho para o arquivo de certificado CA
  * STORAGE_SSL_CERT_FILE - caminho para o arquivo de certificado
  * STORAGE_SSL_CERT_FILE_PASSWORD - senha do arquivo de chave do certificado
  * STORAGE_SSL_KEY_FILE - caminho para o arquivo de chave
  * STORAGE_SSL_KEY_FILE_PASSWORD - senha do arquivo de chave
  * STORAGE_SSL_REJECT_UNAUTHORIZED - defina o valor 1 ou true para rejeitar conexões não autorizadas
  * STORAGE_SSL_TRUST_SERVER_CERTIFICATE - defina o valor 1 ou true para configurar a opção trustServerCertificate do MSSQL

As variáveis a seguir estão disponíveis tanto na edição Community quanto na Premium. No entanto, na edição Premium, a forma preferida é usar o banco de dados de armazenamento e a interface de administração para a configuração.

## Configuração da web e de permissões
* WEB_ROOT - se você precisar executar o DbGate em um subdiretório virtual (ex. para o valor /dbadmin , o dbgate ficará acessível em localhost:3000/dbadmin )
* LOGIN , PASSWORD - credenciais para acessar a aplicação web
* PERMISSIONS - lista de permissões separadas por vírgula. Veja também a lista de permissões abaixo
* SHELL_CONNECTION - se true ou 1, as conexões podem ser definidas em scripts de shell. Caso contrário, apenas conexões pré-configuradas são permitidas. Por padrão, isso não é permitido por motivos de segurança. Atenção: quando permitido, senhas criptografadas são enviadas ao frontend.
* SHELL_SCRIPTING - se true ou 1, scripts de shell JavaScript personalizados são permitidos. Por padrão, isso não é permitido por motivos de segurança.
* LOGIN_PASSWORD_[login] - senha para o login especificado
* LOGIN_PERMISSIONS_[login] - lista de permissões separadas por vírgula para o login informado. Veja também a lista de permissões abaixo
* TOKEN_LIFETIME - tempo de vida do token de acesso. Após esse tempo, o usuário logado será redirecionado para a página de login. O padrão é 1d (significa 1 dia). São possíveis valores como 3h (3 horas), 10m (10 minutos), 2d (2 dias)
* SINGLE_CONNECTION - ID da conexão. Se definida, apenas esta conexão estará disponível (deve ser usada com SINGLE_DATABASE)
* SINGLE_DATABASE - nome do banco de dados; apenas este banco de dados estará disponível. (deve ser usada com SINGLE_CONNECTION)
* BASIC_AUTH - se true ou 1 , é usada autenticação básica tanto na web quanto na API. Caso contrário, são usados o formulário de login e a autenticação de API baseada em token JWT. A autenticação básica não pode ser usada para autenticação OAuth.
* SKIP_ALL_AUTH - se true ou 1, toda a autenticação é ignorada
* ALLOW_DBGATE_PRIVATE_CLOUD - por padrão, o DbGate cloud está desabilitado na versão web. Com esta variável, você pode habilitá-lo
* REDIRECT_TO_DBGATE_CLOUD_LOGIN - na versão web, redireciona para o login do DbGate cloud, em vez de abrir uma nova janela
* LANGUAGE - idioma da interface, ex. en, cs, de, fr, etc. Veja a tabela de configuração de idiomas abaixo. Defina "auto" para usar o idioma do navegador

## Configuração de idiomas
| Idioma | Valor |
|----------|-------|
| Inglês | en |
| Alemão | de |
| Espanhol | es |
| Francês | fr |
| Italiano | it |
| Português (Brasil) | pt |
| Japonês | ja |
| Chinês - simplificado | zh |
| Tcheco | cs |
| Eslovaco | sk |


## Configuração de logs
* LOG_LEVEL - todas as mensagens com este nível de log ou superior serão registradas. Um dos valores trace, debug, info, warn, error, fatal. O padrão é info
* FILE_LOG_LEVEL - nível de log para registro em arquivo de log. Para o log em arquivo, tem prioridade maior que LOG_LEVEL
* CONSOLE_LOG_LEVEL - nível de log para registro em arquivo de log. Para o log no console, tem prioridade maior que LOG_LEVEL

## Configuração de OAuth (apenas versão web)
* OAUTH_AUTH - endpoint de autenticação do protocolo OAuth
* OAUTH_TOKEN - endpoint de token do protocolo OAuth
* OAUTH_LOGOUT - URL de logout do provedor OAuth. O usuário será redirecionado para esta URL quando solicitar o logout
* OAUTH_CLIENT_ID - ID do cliente
* OAUTH_CLIENT_SECRET - segredo do cliente
* OAUTH_LOGIN_FIELD - nome do campo do payload que contém o nome de login. Para ver os campos disponíveis, você pode inspecionar o log do dbgate; o payload enviado pelo provedor OAuth é registrado no console. Este nome de login é usado, por exemplo, para configurar permissões. Não é necessariamente o login informado no OAuth. Se não for especificado, todos os usuários do provedor OAuth terão o mesmo nome de login.
* OAUTH_ALLOWED_LOGINS - nomes de login separados por vírgula que terão permissão para fazer login. Se não for especificado, todos os logins poderão usar a aplicação DbGate.
* OAUTH_SCOPE - escopo enviado aos endpoints de authorize e token do OAuth
* OAUTH_GROUP_FIELD - campo do payload do OAuth que indica o grupo
* OAUTH_ALLOWED_GROUPS - nomes de grupos permitidos separados por vírgula

## Configuração de Active Directory/LDAP (apenas versão web)
* AD_URL - URL do provedor LDAP (ex. ldap://domain.com)
* AD_BASEDN - ex. dc=domain,dc=com
* AD_USERNAME - nome de usuário do active directory
* AD_PASSWORD - senha do active directory
* AD_ALLOWED_LOGINS - nomes de login separados por vírgula que terão permissão para fazer login. Se não for especificado, todos os logins poderão usar a aplicação DbGate.

## Configuração do cliente Oracle  
* ORACLE_INSTANT_CLIENT - caminho para o [Oracle instant client](https://www.oracle.com/cz/database/technologies/instant-client/downloads.html)

## Configuração de conexões
Você pode configurar a lista de conexões com variáveis de ambiente; nesse caso, os comandos "Add connection" e "Edit connection" não estarão disponíveis.

* CONNECTIONS - lista de nomes de conexões pré-configuradas, separados por vírgula. Nas opções a seguir, [connection id] é o ID dessa lista
* LABEL_[connection id] - rótulo (nome de exibição) da conexão. 
* SERVER_[connection id] - servidor (nome do host) da conexão.
* USER_[connection id] - nome de usuário para a conexão com o BD.
* PASSWORD_[connection id] - senha para a conexão com o BD.
* PASSWORD_MODE_[connection id] - determina se a senha e o nome de usuário são armazenados ou devem ser preenchidos pelo usuário. Um dos seguintes valores:
  * askPassword - o DbGate solicita a senha ao conectar
  * askUser - o DbGate solicita o nome de usuário e a senha
* PORT_[connection id] - porta para a conexão com o BD.
* FILE_[connection id] - caminho do arquivo de banco de dados (para SQLite).
* URL_[connection id] - URL do banco de dados (funciona para MongoDB, PostgreSQL, CockroachDb, Redshift, Oracle).
* SERVICE_NAME_[connection id] - nome do serviço Oracle.
* DATABASE_[connection id] - nome do banco de dados padrão.
* READONLY_[connection id] - conectar em modo somente leitura
* ENGINE_[connection id] - mecanismo da conexão (**obrigatório**, nome do mecanismo com plugin), um de:
  * mssql@dbgate-plugin-mssql - Microsoft SQL Server
  * mysql@dbgate-plugin-mysql - MySQL
  * mariadb@dbgate-plugin-mysql - MariaDB
  * postgres@dbgate-plugin-postgres - PostgreSQL
  * cockroach@dbgate-plugin-postgres - CockroachDB
  * redshift@dbgate-plugin-postgres - Amazon Redshift
  * sqlite@dbgate-plugin-sqlite - SQLite
  * mongo@dbgate-plugin-mongo - MongoDB
  * redis@dbgate-plugin-redis - Redis
* USE_SSH_[connection id] - defina o valor 1 ou true quando o túnel SSH deve ser usado
* SSH_HOST_[connection id] - nome do host SSH
* SSH_PORT_[connection id] - número da porta SSH
* SSH_MODE_[connection id] - um dos seguintes valores
  * userPassword - autenticar com usuário e senha
  * agent - autenticar com agente SSH
  * keyFile - autenticar com arquivo de chave
* SSH_LOGIN_[connection id] - login SSH
* SSH_PASSWORD_[connection id] - senha SSH
* SSH_KEY_FILE_[connection id] - caminho completo para o arquivo de chave
* SSH_KEY_FILE_PASSWORD_[connection id] - senha do arquivo de chave
* USE_SSL_[connection id] - defina o valor 1 ou true quando SSL deve ser usado
* SSL_CA_FILE_[connection id] - caminho para o arquivo de certificado CA
* SSL_CERT_FILE_[connection id] - caminho para o arquivo de certificado
* SSL_CERT_FILE_PASSWORD_[connection id] - senha do arquivo de chave do certificado
* SSL_KEY_FILE_[connection id] - caminho para o arquivo de chave
* SSL_REJECT_UNAUTHORIZED_[connection id] - defina o valor 1 ou true para rejeitar conexões não autorizadas
* SSL_TRUST_CERTIFICATE_[connection id] - defina o valor 1 ou true para configurar a opção trustServerCertificate do MSSQL
* SETTINGS_[settings key] - valor de configuração pré-definido. A chave de configuração pode ser consultada no código-fonte, https://github.com/dbgate/dbgate/blob/master/packages/web/src/settings/
* SOCKET_PATH_[connection id] - caminho para o arquivo de socket, se a conexão for via socket
* AUTH_TYPE_[connection id] - tipo de autenticação
  * hostPort (padrão)
  * socket - o valor é definido implicitamente ao configurar SOCKET_PATH
  * tedious - autenticação portátil padrão para MS SQL, usando o driver tedious
  * sspi - autenticação integrada do Windows (apenas Windows, MS SQL), usando o driver nativo MSSQL
  * sql - autenticação SQL (apenas Windows, MS SQL), usando o driver nativo MSSQL
* ALLOWED_DATABASES_[connection id] - nomes de bancos de dados permitidos para a conexão especificada, separados por barra vertical ("|")
* ALLOWED_DATABASES_REGEX_[connection id] - expressão regular para os nomes de bancos de dados permitidos na conexão especificada
* USE_SEPARATE_SCHEMAS_[connection id] - defina o valor 1 ou true para carregar os schemas separadamente. Use isso se você tiver schemas grandes.
* LOCAL_DATA_CENTER_[connection id] - data center local (para Apache Cassandra)
* CONNECTION_[connection id]_parameterName - define um nome de parâmetro específico do mecanismo

SettingsModal.svelte , procure a string "name="/ Se você precisar definir "true", use o valor "1". Se precisar de "false", use uma string vazia ("0" não funcionará)

## Configuração de perfis (roles)
Esta configuração pode ser usada apenas na edição Team Premium, quando o banco de dados de armazenamento é usado para as configurações. Os perfis definidos em variáveis de ambiente são importados para o banco de dados de armazenamento na inicialização do container docker.
Você pode definir perfis com permissões específicas e atribuir conexões ao perfil. A atribuição de perfis aos usuários é feita na interface de administração.
* `ROLE_[role_name]_PERMISSIONS` - lista de permissões separadas por vírgula para o perfil informado. Veja a lista de permissões abaixo
* `ROLE_[role_name]_CONNECTIONS` - lista de IDs de conexão separados por vírgula atribuídos ao perfil informado
* `ROLE_[role_name]_DATABASES_[db_perm_id]_CONNECTION` - ID da conexão para a permissão de banco de dados com o ID informado
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES` - lista de nomes de bancos de dados separados por barra vertical ("|") para a permissão de banco de dados com o ID informado
* `ROLE_[role_name]_DATABASES_[db_perm_id]_DATABASES_REGEX` - expressão regular para os nomes de bancos de dados da permissão de banco de dados com o ID informado
* `ROLE_[role_name]_DATABASES_[db_perm_id]_PERMISSION` - um de: deny | run_script | write_data | read_content | view
* `ROLE_[role_name]_TABLES_[db_perm_id]_CONNECTION` - ID da conexão para a permissão de tabela com o ID informado
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES` - lista de nomes de bancos de dados separados por barra vertical ("|") para a permissão de banco de dados com o ID informado
* `ROLE_[role_name]_TABLES_[db_perm_id]_DATABASES_REGEX` - expressão regular para os nomes de bancos de dados da permissão de banco de dados com o ID informado
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS` - lista de nomes de schemas separados por barra vertical ("|") para a permissão de tabela com o ID informado
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCHEMAS_REGEX` - expressão regular para os nomes de schemas da permissão de tabela com o ID informado
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES` - lista de nomes de tabelas separados por barra vertical ("|") para a permissão de banco de dados com o ID informado
* `ROLE_[role_name]_TABLES_[db_perm_id]_TABLES_REGEX` - expressão regular para os nomes de tabelas da permissão de banco de dados com o ID informado
* `ROLE_[role_name]_TABLES_[db_perm_id]_PERMISSION` - um de: deny | run_script | create_update_delete | update_only | read
* `ROLE_[role_name]_TABLES_[db_perm_id]_SCOPE` - um de: collections | sql_objects | triggers | functions | procedures | tables_views_collections | views | tables | all_objects
## Permissões
Por padrão, todas as permissões estão disponíveis. Se você usar o prefixo \~, a permissão é revogada.

### Exemplos
* ~*, widgets/database - todas as permissões são revogadas, apenas o widget de banco de dados fica visível
* ~widgets/*, widgets/database - todas as permissões de widgets são revogadas, apenas o widget de banco de dados fica visível
* ~connections/*, connections/con1 - todas as conexões, exceto con1, ficam ocultas e desabilitadas

### Lista de permissões
* settings/change - permite alterar as configurações
* plugins/install - permite instalar plugins
* widgets/[widget_name] - se não for concedida, o widget fica oculto. O widget é a faixa no lado esquerdo. Widgets disponíveis:
  * database
  * file
  * history
  * archive
  * plugins
  * cell-data
  * app
* files/[folder]/read - ler arquivos da pasta informada
* files/[folder]/write - gravar arquivos na pasta informada
* apps/write - salvar no conteúdo de apps
* archive/write - salvar no conteúdo do arquivo (archive)
* connections/[connection_id] - permite ver e usar a conexão definida
* internal-storage = acesso ao armazenamento interno (Premium)
* admin/auth - Administração - aba Autenticação (Premium)
* admin/connections - Administração - aba Conexões (Premium)
* admin/users - Administração - aba Usuários (Premium)
* admin/roles - Administração - aba Perfis (Premium)
* dbops/sql-template/* - modelos SQL (ex. SQL: CREATE TABLE, SQL: SELECT)
* dbops/sql-generator - gerador de SQL
* dbops/sql-dump/import - importar dump SQL
* dbops/sql-dump/export - exportar dump SQL
* dbops/query - executar consulta SQL
* dbops/import - importar dados
* dbops/export - exportar dados
* dbops/charts - ver gráficos
* dbops/profiler - profiler de banco de dados
* dbops/createdb - criar banco de dados
* dbops/dropdb - excluir banco de dados
* dbops/model/view - ver o modelo do banco de dados (diagramas, JSON)
* dbops/model/edit - editar o modelo do banco de dados (criar/alterar tabelas, views, etc.)
* dbops/model/compare - comparar modelos de bancos de dados
* dbops/table/rename - renomear tabela
* dbops/table/truncate - truncar tabela
* dbops/table/backup - criar backup da tabela

