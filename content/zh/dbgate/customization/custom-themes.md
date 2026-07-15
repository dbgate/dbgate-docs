---
sourceHash: f2791f82e04437cfea34f20ce37c68c887e87a2c0da52d28b9f823e0e184aab9
language: zh
title: 自定义主题
weight: 10
---

DbGate 提供灵活的主题支持。您可以创建自己的主题，更改各种 UI 元素的颜色。

主题以 JSON 文件的形式创建。创建自定义主题最简单的方法是使用主题 AI 助手。

## 主题 AI 助手
要调用主题 AI 助手，请打开“设置/主题”，然后单击“使用 AI 助手自定义”按钮。

![Theme settings](https://media.dbgate.io/img/app-settings-themes-light.png)

主题 AI 助手将根据您的指示自定义主题。您可以指定要更改哪些颜色以及如何更改。例如，您可以说“将主色改为绿色，将背景色改为深灰色”。

![screenshot](/screenshots/dbgate-green.png)

使用 AI 助手生成主题需要几分钟时间，因为大约有 280 个变量需要生成。主题生成后，您可以单击“应用主题”按钮来使用新主题。您也可以使用“保存主题”按钮将主题保存为 JSON 文件。所有已保存的主题随后都会出现在主题选择器中。您还可以在文件小部件 {{< mdi "file" >}} 中管理（重命名、编辑、删除）主题。

## 在 DbGate Cloud 中共享主题
您可以通过 DbGate Cloud 与其他 DbGate 用户共享主题。要共享主题，请在 [DbGate 知识库仓库](https://github.com/dbgate/dbgate-knowledge-base) 中创建拉取请求。主题存储在 folder-Themes 目录中。请参阅现有主题作为示例。只需将您的主题 JSON 文件复制到该目录，并创建拉取请求即可。在您的拉取请求合并后，您的主题将在主题选择器中提供给所有 DbGate 用户。
