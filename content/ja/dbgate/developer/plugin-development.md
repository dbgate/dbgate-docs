---
sourceHash: e10360d65315ca6bef22d826b37ec0f1623808453e37fd5d2a391f720399cc17
language: ja
title: プラグイン開発
weight: 30
---

DbGate はプラグインの作成をサポートしています。プラグインウィザードのおかげで、基本的なプラグインを作るのは非常に簡単です。DbGate プラグインは NPM (JavaScript) パッケージであり、依存関係を持つことができます。(ただしネイティブ依存関係は除きます)

現在、プラグインには 3 種類あります:
- テーマプラグイン
- ファイル形式プラグイン
- データベースドライバープラグイン

## 前提条件のインストール
[node.js](https://nodejs.org) がインストールされている必要があります。

また、[Yeoman](https://yeoman.io/) と Yeoman の [DbGate プラグインジェネレーター](https://www.npmjs.com/package/generator-dbgate) も必要です:

```sh
npm install -g yo
npm install -g generator-dbgate
```

## プラグインの作成
コンソールで次のコマンドを実行します:

```sh
yo dbgate
```

3 つの質問に答える必要があります:
- プラグイン名。dbgate-plugin- で始まる必要があります。例: dbgate-plugin-myplugin
- プラグインの種類。例として "Database driver" を選択します
- パッケージマネージャー。npm または yarn のうち、お好みのものを選択します。DbGate は yarn を使用しています。

## プラグインの編集とテスト
何らかのエディターを開きます。おすすめは [Visual Studio Code](https://code.visualstudio.com/) です。
テーマプラグインにはソースファイルが 1 つ、src/index.js だけ含まれています。テーマの色は好きなように変更できます。属性 themeName は、DbGate のテーマ選択画面に表示される名前です。

新しいテーマを確認したい場合は、コンソールから (プラグインのディレクトリで) 次を実行します:
```sh
yarn plugin
```
npm を使用している場合は、次のようにします
```sh
npm run plugin
```
このコマンドは、ローカルにインストールされた DbGate インスタンスにプラグインをインストールします (変更を加えた場合は更新します)。DbGate を再起動すると、新しいテーマが表示されるはずです。
再起動は必須ではありません。"yarn plugin" 実行後に新しいプラグインバージョンを使うには、アプリの再読み込み (メニュー View/Reload) で十分です

## プラグインの削除
DbGate のプラグインウィジェットからプラグインをアンインストールできます。または次のコマンドを使用します:
```sh
yarn plugout
```

## プラグインの公開
プラグインは通常の NPM パッケージなので、NPM リポジトリに公開できます。公開後は、すべての DbGate ユーザーが "Plugins" ウィジェットで利用できるようになります。

## プラグインのアイコン
各プラグインは拡張機能一覧でアイコンとして表示されます。NPM は NPM パッケージのアイコンをサポートしていないため、アイコンは package.json ファイルの description フィールドに次の構文で記述できます:

```
    "description": "Any description ![icon](https://link_to_icon.svg)",
```

Yeoman ジェネレーターを使用すれば、この点も少し手助けしてくれます。

## データベースドライバープラグインの作成
ドライバープラグインの作成は他の作成手順とよく似ており、"Database driver plugin" を選択するだけです。`yarn plugin` の後は、新しいドライバーを使って接続を定義し、ダミーのデータベース一覧とテーブル一覧を表示できるようになるはずです。

基本的な機能を持つシンプルなドライバーは非常に短時間で作成でき、より複雑な機能は後から実装できます。

ドライバーの作成は、次のようなステップで構成されます:
* 適切な nodejs パッケージ (ドライバー) を見つけます。可能であれば純粋な JavaScript のパッケージを選んでください。ネイティブパッケージは大きな障害になります。このネイティブパッケージは DbGate のディストリビューションに追加しなければならず、さらに異なるプラットフォームでのビルドに問題が生じることが予想されます。一方、純粋な JavaScript のパッケージは、DbGate を変更する必要なく、すべてのプラットフォームで通常どおり問題なく動作します。
* frontend/driver.js の showConnectionField 関数で、接続用のフィールドを定義します
* backend/driver.js に connect 関数を実装します
* backend/driver.js に getVersion 関数を実装します (任意ですが、実装すれば接続タブの "Test" ボタンで接続をテストできるようになります)
* backend/Analyser.js クラスに _rynAnalysis メソッドを実装します。このメソッドはデータベース構造を返す必要があります。
* backend/driver.js に query メソッドを実装します。これにより、テーブル一覧を表示し、テーブルのデータを閲覧できるようになるはずです
* その他のメソッドを実装します。他のドライバープラグインを参考にしてください。最も典型的なプラグインはおそらく PostgreSQL プラグインです。https://github.com/dbgate/dbgate/tree/master/plugins/dbgate-plugin-postgres
