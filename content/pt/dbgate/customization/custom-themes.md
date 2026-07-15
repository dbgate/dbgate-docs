---
sourceHash: f2791f82e04437cfea34f20ce37c68c887e87a2c0da52d28b9f823e0e184aab9
language: pt
title: Temas personalizados
weight: 10
---

O DbGate tem suporte flexível a temas. Você pode criar seu próprio tema, alterando as cores de diversos elementos da interface.

Os temas são criados como arquivos JSON. A maneira mais simples de criar um tema personalizado é usar o assistente de IA de temas.

## Assistente de IA de temas
Para acionar o assistente de IA de temas, abra Settings/Themes e clique no botão "Customize with AI assistant".

![Theme settings](https://media.dbgate.io/img/app-settings-themes-light.png)

O assistente de IA de temas vai personalizar seu tema de acordo com as suas instruções. Você pode especificar quais cores deseja alterar e como. Por exemplo, você pode dizer "Deixe a cor primária verde e a cor de fundo cinza escuro".

![screenshot](/screenshots/dbgate-green.png)

A geração do tema com o assistente de IA leva alguns minutos, pois há cerca de 280 variáveis a serem geradas. Depois que o tema for gerado, você pode clicar no botão "Apply Theme" para usar o novo tema. Você também pode usar o botão "Save theme" para salvar o tema como um arquivo JSON. Todos os temas salvos ficam então disponíveis no seletor de temas. Você também pode gerenciar (renomear, editar, excluir) os temas no widget de arquivos {{< mdi "file" >}}.

## Compartilhando temas no DbGate Cloud
Você pode compartilhar seus temas com outros usuários do DbGate usando o DbGate Cloud. Para compartilhar um tema, crie um pull request no [repositório da base de conhecimento do DbGate](https://github.com/dbgate/dbgate-knowledge-base). Os temas ficam armazenados no diretório folder-Themes. Veja os temas existentes como exemplos. Basta copiar o arquivo JSON do seu tema para esse diretório e criar um pull request. Após o merge do seu pull request, seu tema ficará disponível para todos os usuários do DbGate no seletor de temas.
