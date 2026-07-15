---
sourceHash: e10360d65315ca6bef22d826b37ec0f1623808453e37fd5d2a391f720399cc17
language: zh
title: 插件开发
weight: 30
---

DbGate 支持创建插件。借助插件向导，创建基础插件非常简单。DbGate 插件就是 NPM（JavaScript）包，它们可以有依赖项。（但不能有原生依赖项）

目前有 3 种类型的插件：
- 主题插件
- 文件格式插件
- 数据库驱动插件

## 安装先决条件
你需要安装 [node.js](https://nodejs.org)。

此外，你还需要 [Yeoman](https://yeoman.io/) 和 yeoman [DbGate 插件生成器](https://www.npmjs.com/package/generator-dbgate)：

```sh
npm install -g yo
npm install -g generator-dbgate
```

## 创建插件
在控制台中运行以下命令：

```sh
yo dbgate
```

你需要回答 3 个问题：
- 插件名称，必须以 dbgate-plugin- 开头，例如 dbgate-plugin-myplugin
- 插件类型，例如选择 "Database driver"
- 包管理器，根据你的偏好选择 npm 或 yarn。DbGate 使用 yarn。

## 编辑和测试插件
打开某个编辑器，推荐选择 [Visual Studio Code](https://code.visualstudio.com/)。
主题插件只包含一个源文件 src/index.js。你可以按自己的意愿修改主题颜色。属性 themeName 是显示在 DbGate 主题选择器中的名称。

当你想查看你的新主题时，从控制台（在插件目录中）运行：
```sh
yarn plugin
```
或者如果你使用 npm，则运行
```sh
npm run plugin
```
此命令会将你的插件安装到本地安装的 DbGate 实例中（或者在你做出修改后更新它）。重启 DbGate 后，你应该会看到新主题。
其实不必重启，运行 "yarn plugin" 之后只需重新加载应用（菜单 View/Reload）即可使用新的插件版本。

## 删除插件
你可以从 DbGate 插件小部件中卸载插件。或者使用以下命令：
```sh
yarn plugout
```

## 发布插件
插件就是普通的 NPM 包，你可以将其发布到 NPM 仓库。发布之后，所有 DbGate 用户都可以在 "Plugins" 小部件中使用它。

## 插件图标
每个插件在扩展列表中都以图标表示。NPM 不支持为 NPM 包设置图标，因此图标可以放在 package.json 文件的 description 字段中，语法如下：

```
    "description": "Any description ![icon](https://link_to_icon.svg)",
```

如果你使用 yeoman 生成器，它会在这方面为你提供一些帮助。

## 创建数据库驱动插件
创建驱动插件与前面的创建过程非常相似，只需选择 "Database driver plugin"。执行 `yarn plugin` 之后，你应该能够使用新驱动定义连接，并看到虚拟的数据库列表和表列表。

你可以很快创建出具有基本功能的简单驱动，更复杂的功能可以稍后实现。

创建驱动可以包含以下步骤：
* 找到合适的 nodejs 包（驱动）。如果可能，请选择纯 JavaScript 包。原生包会带来很大的麻烦，这类原生包必须被加入 DbGate 的发行版中，而且你可能会遇到在不同平台上构建的问题。另一方面，纯 JavaScript 包通常在所有平台上都能正常工作，无需修改 DbGate。
* 在 frontend/driver.js 的 showConnectionField 函数中定义连接字段
* 在 backend/driver.js 中实现 connect 函数
* 在 backend/driver.js 中实现 getVersion 函数（可选，但完成之后，你就可以用连接选项卡上的 "Test" 按钮测试连接了）
* 在 backend/Analyser.js 类中实现 _rynAnalysis 方法。该方法应返回数据库结构。
* 在 backend/driver.js 中实现 query 方法。完成之后，你应该能够查看表列表并浏览表数据
* 实现其他方法。请参考其他驱动插件作为灵感来源，最典型的插件大概是 PostgreSQL 插件，https://github.com/dbgate/dbgate/tree/master/plugins/dbgate-plugin-postgres
