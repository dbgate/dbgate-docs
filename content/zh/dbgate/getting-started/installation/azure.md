---
sourceHash: 4f9596eb7ab62bc22f186ebb87b019eb2986c18eb704368b8634ffc2cd471482
language: zh
title: 在 Azure 上部署
weight: 20
---

DbGate Azure 版是一个协作式、多用户的 Web 平台，专为在 Azure 中进行数据库管理而设计。借助 Azure 基础设施，它为在云环境中运营的组织简化了团队协作。其共享的、基于浏览器的界面简化了协作、数据访问和数据库监管，并与 Azure 无缝集成。

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}Azure 上的 DbGate{{< /button >}}


## DbGate Azure 主要功能
DbGate Azure 支持与 DbGate Team Premium 相同的功能，但针对 Azure 进行了优化

* 支持 Azure 托管标识
* 用户、连接和角色的管理
* 数据浏览、筛选和编辑
* 导入和导出数据
* 可视化查询构建器

## 安装过程
在 Azure 上安装非常简单，几乎是一键式过程。

我们建议使用具有 2 GB 内存的虚拟机。

安装完成后，您需要设置管理员密码，然后即可管理连接、用户、角色并授予权限。

## 订阅和许可
DbGate Azure 可以通过 Azure Marketplace 进行订阅，价格取决于所选虚拟机的处理器数量。

30 天免费试用让您可以使用 DbGate 的所有功能。试用期结束后，将根据所选实例大小按照 Azure 定价方案计费。无需额外的许可证，因为所有付款均通过 [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview) 订阅处理。

## DbGate Azure 更新
DbGate Azure 有其特殊的构建版本，直接在虚拟服务器上运行（没有像 docker 这样的额外虚拟化层）。它具有自动升级功能——启动后，容器会请求最新的构建版本，如果找到，就会替换旧版本。您无需手动升级。

如果您手动创建具有新版本的新虚拟机，它将拥有自己的新数据库（内部 MySQL 数据库是虚拟机的一部分），因此没有简单的方法将连接和用户迁移到新的虚拟机。

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}Azure 上的 DbGate{{< /button >}}
