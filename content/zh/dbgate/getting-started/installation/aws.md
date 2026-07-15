---
sourceHash: fd6032a57cb859a0d8cb5046fde87de9bf1a85de56c66586391e84ecbbdc24c1
language: zh
title: 在 AWS 上部署
subtitle: 在 Amazon EC2 集群上一键部署
icon: aws.svg
weight: 10
demo_url: https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy
demo_title: View on AWS
edition: 'premium'
---

DbGate AWS 版是一个协作式、多用户的 Web 平台，专为在 Amazon Web Services (AWS) 中进行数据库管理而设计。借助 AWS 基础设施，它为在云环境中运营的组织简化了团队协作。其共享的、基于浏览器的界面简化了协作、数据访问和数据库监管，同时与 AWS 无缝集成。

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}AWS 上的 DbGate{{< /button >}}

## DbGate AWS 主要功能
DbGate AWS 支持与 DbGate Team Premium 相同的功能，但针对 AWS 进行了优化

* 支持 AWS IAM
* 用户、连接和角色的管理
* 数据浏览、筛选和编辑
* 导入和导出数据
* 可视化查询构建器

## 安装过程
在 AWS 上安装非常简单，几乎是一键完成的过程。

我们推荐使用 t2.medium 实例类型以获得最佳用户体验，但免费套餐中提供的 t2.micro 对于少量用户来说已经足够。

安装完成后，您需要设置管理员密码，然后即可管理连接、用户、角色并授予权限。

## 订阅和许可
DbGate AWS 可通过 AWS Marketplace 订阅，价格取决于所选实例的规格。更大的实例可支持更多并发用户。

30 天免费试用让您可以使用 DbGate 的所有功能。试用期结束后，将按照所选实例规格依据 AWS 的定价方案计费。无需额外的许可，因为所有付款都通过 [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy) 订阅处理。

## DbGate AWS 更新
DbGate AWS 有其专门的构建版本，直接在 EC2 中的虚拟服务器上运行（没有像 docker 这样的额外虚拟化层）。它具有自动升级功能——启动后，容器会请求最新的构建版本，如果找到，就会替换旧版本。您无需手动升级。

如果您手动创建包含新版本的新 EC2 容器，它将拥有自己的新数据库（内部 MySQL 数据库是容器的一部分），因此没有简单的方法将连接和用户迁移到新的 EC2 容器。

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}AWS 上的 DbGate{{< /button >}}
