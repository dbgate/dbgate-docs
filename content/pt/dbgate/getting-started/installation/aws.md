---
sourceHash: fd6032a57cb859a0d8cb5046fde87de9bf1a85de56c66586391e84ecbbdc24c1
language: pt
title: Implantar na AWS
subtitle: Implantação com um clique em cluster Amazon EC2
icon: aws.svg
weight: 10
demo_url: https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy
demo_title: View on AWS
edition: 'premium'
---

O DbGate AWS edition é uma plataforma web colaborativa e multiusuário projetada especificamente para o gerenciamento de bancos de dados dentro da Amazon Web Services (AWS). Aproveitando a infraestrutura da AWS, ele agiliza o trabalho em equipe para organizações que operam em ambientes de nuvem. Sua interface compartilhada, baseada em navegador, simplifica a colaboração, o acesso aos dados e a supervisão de bancos de dados, ao mesmo tempo em que se integra perfeitamente à AWS.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate na AWS{{< /button >}}

## Principais recursos do DbGate AWS
O DbGate AWS oferece os mesmos recursos do DbGate Team Premium, mas é otimizado para a AWS

* Suporte para AWS IAM
* Administração de usuários, conexões e funções
* Navegação, filtragem e edição de dados
* Importação e exportação de dados
* Construtor visual de consultas

## Processo de instalação
A instalação na AWS é muito simples, é praticamente um processo de um clique.

Recomendamos o tipo de instância t2.medium para a melhor experiência do usuário, mas a t2.micro, disponível no nível gratuito, será suficiente para um número pequeno de usuários.

Após a instalação, você precisa definir a senha de administrador e, em seguida, poderá administrar conexões, usuários, funções e conceder permissões.

## Assinatura e licenciamento
O DbGate AWS pode ser assinado através do AWS Marketplace, com preços baseados no tamanho da instância escolhida. Instâncias maiores suportam mais usuários simultâneos.

Um teste gratuito de 30 dias dá a você acesso a todos os recursos do DbGate. Após o período de teste, a cobrança segue o plano de preços da AWS de acordo com o tamanho da instância selecionada. Nenhum licenciamento adicional é necessário, pois todos os pagamentos são processados através da assinatura do [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy).

## Atualizações do DbGate AWS
O DbGate AWS tem uma compilação especial e é executado diretamente em um servidor virtual no EC2 (não há camada adicional de virtualização como o docker). Existe uma funcionalidade de atualização automática - após a inicialização, o contêiner faz uma solicitação da compilação mais recente e, se encontrada, substitui a versão antiga. Você não precisa atualizar manualmente.

Se você criar manualmente um novo contêiner EC2 com uma nova versão, ele terá seu próprio banco de dados novo (o banco de dados MySQL interno faz parte do contêiner), portanto não há uma maneira simples de mover conexões e usuários para o novo contêiner EC2.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate na AWS{{< /button >}}
