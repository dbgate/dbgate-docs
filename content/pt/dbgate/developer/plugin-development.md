---
sourceHash: e10360d65315ca6bef22d826b37ec0f1623808453e37fd5d2a391f720399cc17
language: pt
title: Desenvolvimento de plugins
weight: 30
---

O DbGate suporta a criação de plugins. Graças ao assistente de plugins, é realmente simples criar um plugin básico. Os plugins do DbGate são pacotes NPM (JavaScript) e podem ter dependências. (mas não dependências nativas)

Atualmente existem 3 tipos de plugins:
- Plugin de tema
- Plugin de formato de arquivo
- Plugin de driver de banco de dados

## Instalar pré-requisitos
Você precisa ter o [node.js](https://nodejs.org) instalado. 

Você também vai precisar do [Yeoman](https://yeoman.io/) e do [gerador de plugins do DbGate](https://www.npmjs.com/package/generator-dbgate) para o yeoman:

```sh
npm install -g yo
npm install -g generator-dbgate
```

## Criar plugin
Execute o seguinte comando no console:

```sh
yo dbgate
```

Você precisa responder 3 perguntas:
- Nome do plugin, deve começar com dbgate-plugin-, por exemplo dbgate-plugin-myplugin
- Tipo do plugin, escolha por exemplo "Database driver"
- Gerenciador de pacotes, escolha npm ou yarn, o que preferir. O DbGate usa yarn.

## Editar e testar o plugin
Abra algum editor, a opção recomendada é o [Visual Studio Code](https://code.visualstudio.com/)  . 
O plugin de tema contém apenas um arquivo fonte, src/index.js. Você pode modificar as cores do tema como quiser. O atributo themeName é o nome que é exibido no seletor de temas do DbGate.

Quando quiser ver seu novo tema, execute isto no console (a partir do diretório do plugin):
```sh
yarn plugin
```
ou, se você usa npm, então
```sh
npm run plugin
```
Este comando instala seu plugin na instância do DbGate instalada localmente (ou o atualiza, quando você faz alterações). Após reiniciar o DbGate, você deve ver o novo tema.  
Reiniciar não é necessário, recarregar o aplicativo (menu View/Reload) é suficiente para usar a nova versão do plugin depois de executar "yarn plugin"

## Remover plugin
Você pode desinstalar o plugin pelo widget de plugins do DbGate. Ou usando o seguinte comando:
```sh
yarn plugout
```

## Publicar plugin
O plugin é um pacote NPM comum, você pode publicá-lo no repositório NPM. Após a publicação, ele ficará disponível para todos os usuários do DbGate no widget "Plugins".

## Ícone do plugin
Cada plugin é representado por um ícone na lista de extensões. O NPM não suporta ícones para pacotes NPM, portanto o ícone pode ficar no campo description do arquivo package.json com a seguinte sintaxe:

```
    "description": "Any description ![icon](https://link_to_icon.svg)",
```

Se você usar o gerador do yeoman, ele vai te ajudar um pouco com isso.

## Criar plugin de driver de banco de dados
Criar um plugin de driver é muito parecido com criar qualquer outro, você apenas seleciona "Database driver plugin". Depois de `yarn plugin`, você deve conseguir definir uma conexão usando seu novo driver e ver uma lista de bancos de dados e uma lista de tabelas fictícias.

Você pode criar um driver simples com funcionalidade básica muito rapidamente, recursos mais complexos podem ser implementados depois.

A criação de um driver pode consistir nas seguintes etapas:
* encontrar um pacote nodejs (driver) apropriado. Escolha um pacote em JavaScript puro se possível. Pacotes nativos são uma grande complicação, esse pacote nativo precisa ser adicionado à distribuição do DbGate, e você também pode esperar problemas com a compilação em diferentes plataformas. Por outro lado, pacotes em JavaScript puro funcionam normalmente sem problemas em todas as plataformas, sem necessidade de alterar o DbGate.
* definir os campos da conexão em frontend/driver.js, função showConnectionField
* implementar a função connect em backend/driver.js 
* implementar a função getVersion em backend/driver.js (opcional, mas quando pronta, você já pode testar a conexão com o botão "Test" na aba de conexão)
* implementar o método _rynAnalysis na classe backend/Analyser.js. Esse método deve retornar a estrutura do banco de dados.
* implementar o método query em backend/driver.js. Depois disso, você deve conseguir ver a lista de tabelas e navegar pelos dados das tabelas
* implementar os demais métodos. Use outros plugins de driver como inspiração, o plugin mais típico é provavelmente o plugin do PostgreSQL, https://github.com/dbgate/dbgate/tree/master/plugins/dbgate-plugin-postgres
