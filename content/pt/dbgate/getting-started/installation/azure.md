---
sourceHash: 4f9596eb7ab62bc22f186ebb87b019eb2986c18eb704368b8634ffc2cd471482
language: pt
title: Implantar no Azure
weight: 20
---

O DbGate Azure edition é uma plataforma web colaborativa e multiusuário, projetada especificamente para o gerenciamento de bancos de dados dentro do Azure. Aproveitando a infraestrutura do Azure, ele agiliza o trabalho em equipe para organizações que operam em ambientes de nuvem. Sua interface compartilhada, baseada em navegador, simplifica a colaboração, o acesso aos dados e a supervisão dos bancos de dados, ao mesmo tempo em que se integra perfeitamente ao Azure.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate no Azure{{< /button >}}


## Principais recursos do DbGate Azure
O DbGate Azure oferece os mesmos recursos do DbGate Team Premium, mas é otimizado para o Azure

* Suporta identidade gerenciada do Azure
* Administração de usuários, conexões e funções
* Navegação, filtragem e edição de dados
* Importação e exportação de dados
* Construtor visual de consultas

## Processo de instalação
A instalação no Azure é muito simples, sendo praticamente um processo de um clique.

Recomendamos máquinas virtuais com 2 GB de RAM.

Após a instalação, você precisa definir a senha de administrador e, em seguida, poderá administrar conexões, usuários, funções e conceder permissões.

## Assinatura e licenciamento
O DbGate Azure pode ser assinado através do Azure Marketplace, com preços baseados no número de processadores da máquina virtual escolhida.

Um teste gratuito de 30 dias dá acesso a todos os recursos do DbGate. Após o período de teste, a cobrança segue o plano de preços do Azure de acordo com o tamanho da instância selecionada. Nenhum licenciamento adicional é necessário, pois todos os pagamentos são processados pela assinatura do [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview).

## Atualizações do DbGate Azure
O DbGate Azure tem sua compilação especial e roda diretamente no servidor virtual (não há camada adicional de virtualização como o docker). Existe uma funcionalidade de atualização automática — após a inicialização, o contêiner faz uma requisição para verificar a compilação mais recente e, se encontrada, substitui a versão antiga. Você não precisa fazer a atualização manualmente.

Se você criar manualmente uma nova máquina virtual com a nova versão, ela terá seu próprio banco de dados novo (o banco de dados MySQL interno faz parte da máquina virtual), portanto não há uma maneira simples de mover conexões e usuários para a nova máquina virtual.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate no Azure{{< /button >}}
