---
sourceHash: 1565401b5cbe564d5dea5c98e8e060786cb30e1952808c41e0a5542a29f3ef42
language: pt
title: Team Premium no Docker
weight: 30
---

Uma instalação típica do Team Premium consiste em dois componentes: 
- Contêiner Docker do servidor DbGate
- Servidor de banco de dados (MS SQL, MySQL, PostgreSQL, Oracle) - banco de dados de armazenamento interno para conexões, usuários e funções. Você pode usar um servidor de banco de dados existente ou instalar um novo.

## Contêiner Docker do Servidor DbGate
Use a [imagem do DbGate Team Premium](https://hub.docker.com/r/dbgate/dbgate-premium) do Docker Hub:
```
docker pull dbgate/dbgate-premium
```

O contêiner do DbGate Team Premium exige que algumas variáveis de ambiente sejam definidas:
- `STORAGE_SERVER`, `STORAGE_DATABASE`, `STORAGE_USER`, `STORAGE_PASSWORD`, `STORAGE_ENGINE` - definem a conexão com o banco de dados de armazenamento interno

Consulte a [documentação das variáveis de ambiente](/pt/dbgate/customization/env-variables/#team-premium-edition-configuration) para mais detalhes sobre as variáveis de ambiente disponíveis.

## Requisitos de Recursos

Na verdade, o DbGate Team Premium tem um consumo de recursos muito baixo, mas para o melhor desempenho recomendamos a seguinte configuração (para 10 usuários simultâneos):
- 2 núcleos de CPU
- 4 GB de RAM (inclui o consumo de RAM do banco de dados de armazenamento interno MySQL ou PostgreSQL)
- 10 GB de espaço livre em disco (para a instalação do docker, banco de dados de armazenamento, arquivos temporários, resultados de consultas, etc. O consumo real de espaço em disco depende dos padrões de uso)

Para um número menor de usuários, você pode usar limites de recursos menores (1 GB de RAM, 1 núcleo de CPU).  
Quando você precisar minimizar o consumo de recursos em instalações pequenas, recomendamos usar MySQL/MariaDB como armazenamento interno.  

## Configurando o docker

Se você quiser usar arquivos em disco para armazenar arquivos de usuário (como a exportação de resultados de consultas), você deve mapear o caminho `/root/.dbgate` no contêiner.

Abaixo está um exemplo de arquivo `docker-compose.yml`, definindo o contêiner do DbGate Team Premium com PostgreSQL como banco de dados de armazenamento interno.
- Você pode definir a variável de ambiente `DBGATE_LICENSE` para configurar a chave de licença. Se não for definida, o DbGate solicitará a chave de licença na primeira inicialização.
-  Você pode definir a variável de ambiente 'ADMIN_PASSWORD' para configurar a senha do usuário admin. Se não for definida, o DbGate solicitará a senha do admin na primeira inicialização.

```yaml
version: '3'
services:
  dbgate:
    image: dbgate/dbgate-premium
    restart: always
    ports:
      - 80:3000
    environment:
      STORAGE_SERVER: postgres_service
      STORAGE_USER: postgres
      STORAGE_PASSWORD: XXXStoragePwd
      STORAGE_PORT: 5432
      STORAGE_DATABASE: dbgate
      STORAGE_ENGINE: postgres@dbgate-plugin-postgres
      STORAGE_SCHEMA: public
    volumes:
      - dbgate_data:/root/.dbgate

  postgres_service:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: XXXStoragePwd
      POSTGRES_DB: dbgate
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
    postgres_data:
      driver: local
    dbgate_data:
      driver: local
```

## Stateless/Statefulness
O contêiner do DbGate é stateful. 

Os seguintes dados são armazenados dentro do contêiner:
* Sessões de usuários logados
* Estados de execução de consultas
* Arquivos temporários (como resultados)
* Transações de banco de dados abertas
* Conexões de banco de dados abertas

Não é possível executar corretamente múltiplos contêineres do DbGate atrás de um balanceador de carga, porque os dados acima não são compartilhados entre os contêineres.

## Servidor DbGate a partir do NPM
Se a sua infraestrutura não suportar Docker, você pode usar o [pacote NPM do DbGate Team Premium](https://www.npmjs.com/package/dbgate-serve-premium):
```
npm install -g dbgate-serve-premium
```
 
## Isolamento de processos
O DbGate Team Premium usa isolamento de processos no nível da conexão de banco de dados, de modo que vários usuários possam usar o mesmo servidor de banco de dados sem interferência. O processo derivado do DbGate cresce com o número de usuários e conexões ativas, portanto certifique-se de que seu servidor tenha recursos suficientes.
As seguintes entidades são isoladas em um novo processo:
* Conexões de servidor
* Conexões de banco de dados
* Sessões de consulta
* Execução de tarefas de exportação/importação
* Túnel SSH
