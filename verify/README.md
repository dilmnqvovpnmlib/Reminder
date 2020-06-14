# Log
まず、これ以下のディレクトリは検証用のディレクトリである。

[LINE の Bot 開発 超入門（前編） ゼロから応答ができるまで](https://qiita.com/nkjm/items/38808bbc97d6927837cd)をベースに一通り LINE Bot で Hello World してみた

### js から.env を読み込む方法

- [環境変数の代わりに .env ファイルを使用する (dotenv)](https://maku77.github.io/nodejs/env/dotenv.html)

```js
require("dotenv").config();
console.log("Hello", process.env.LINE_CHANNEL_SECRET);
```

### heroku でデプロイする際に注意すること

- heroku の設定画面の Deploy の項目の GitHub 連携の箇所で連携させる

### heroku でデプロイする際に必要な設定

```bash
 !     No default language could be detected for this app.

			HINT: This occurs when Heroku cannot detect the buildpack to use for this application automatically.

			See https://devcenter.heroku.com/articles/buildpacks

 !     Push failed
```

- ビルドパックする際にどの言語を使うかを設定しておく必要がある。今回の node.js のケースだと、以下のコマンドを叩いた。

```bash
heroku buildpacks:set heroku/nodejs
```

- [heroku で悩んだところ](https://qiita.com/takuto_neko_like/items/52c6c52385386544aa62)
- [Setting a buildpack on an application](https://devcenter.heroku.com/articles/buildpacks#setting-a-buildpack-on-an-application)

### heroku のバージョンを上げる

- heroku のバージョンを heroku/7.42.0 から heroku/7.42.1 に上げたかったので、heroku update をしたが、上手く行かず。
- ググっても上手くいく方法が見つからなかったので、再インストールすることに。
- もとは、snap 経由でインストールしてたので、sudo snap remove heroku で uninstall
- 再度 sudo snap install --classic heroku 経由でインストールするも、バージョンは heroku/7.42.0 ままだったので、シェルでインストールに切り替える
- curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
- which heroku で heroku コマンドの path を確認して、path を通すとバージョンが上がる
- echo 'PATH="/usr/bin/heroku/bin:\$PATH"' >> ~/.bashrc && source ~/.bash_profile

```
heroku --version
heroku/7.42.1 linux-x64 node-v12.16.2
```

- [linux での heroku のインストール＆パスの通し方](https://skill-up-engineering.com/2016/06/21/post-1611/)
- [The Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

- 結局 GUI で環境変数をセットした
- [Using the Heroku Dashboard](https://devcenter.heroku.com/articles/config-vars#using-the-heroku-dashboard)

### heroku のリポジトリに git push できない

- 設定をしていないと、*git push heroku master*でリモートリポジトリに push できない。これは、現在リモート接続されている URL が無いためである。これは、*git remote -v*で確認することができる。以下のようになっていない時は、heroku の接続 URL を変更する。以下のコマンドで、heoroku の接続 URL を設定する。https://git.heroku.com/test-reminder.git は、heroku create したときに生成される url である。

```bash
git remote add heroku https://git.heroku.com/test-reminder.git
git remote set-url heroku https://git.heroku.com/test-reminder.git
```

```bash
heroku	https://git.heroku.com/test-reminder.git (fetch)
heroku	https://git.heroku.com/test-reminder.git (push)
origin	git@github.com:dilmnqvovpnmlib/Reminder.git (fetch)
origin	git@github.com:dilmnqvovpnmlib/Reminder.git (push)
```

- [Heroku の Push 先を変更](https://qiita.com/Tattsum/items/b86c9d698b0727934836)
- [No such remote 'origin'](https://qiita.com/KTakata/items/3e5073072e037c289a3a)

### heroku でデプロイする際は、ソースコードをルートディレクトリに置く必要がある

### LINE bot をグループに招待されても参加されない

- LINE Messaging API の設定画面のチャットのこう m 区のチャットへの参加のラジオボタンのグループ・複数人チャットへの参加を許可するの項目にチェックする。
- [グループトークに招待した LINEBOT にお帰りいただく処理](https://qiita.com/q_masa/items/8589046025dc84709ed8#bot%E3%81%AE%E8%A8%AD%E5%AE%9A%E5%A4%89%E6%9B%B4)
