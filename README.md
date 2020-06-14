# Reminder

## Log

### master branch から develop branch を生やして開発

### CI には、GitHub Actions を使用して開発

- 環境変数はリポジトリの GitHub の Settings の Secrets で設定しておく。
- ただし注意点が２点ある。
- １点目は、_python ./reminder/manage.py test_ のように、_manage.py_ のように、path を指定しないといけない。
- ２点目は、settings.py に環境変数を読み込む設定を記述しているが、_python manage.py test_ を実行する際に環境変数が必要になる。したがって、Sectrets で設定した値を読み込ませる設定は以下のようになる。

```yml
- name: Run Tests
  run: |
    python ./reminder/manage.py test
  env:
    LINE_CHANNEL_ID: ${{ secrets.LINE_CHANNEL_ID }}
    LINE_CHANNEL_SECRET: ${{ secrets.LINE_CHANNEL_SECRET }}
    LINE_ACCESS_TOKEN: ${{ secrets.LINE_ACCESS_TOKEN }}
    GROUP_ID: ${{ secrets.GROUP_ID }}
```

- [暗号化されたシークレットの作成と保存](https://help.github.com/ja/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets)

### LINE Bot を Django と Django Rest Framework で実装するにあたり参考にした記事

- オウム返し
- [Python(Django 2.x) + Heroku でサクッと LINE BOT を作成する](https://murabitoleg.com/line-bot/)

### 開発用サーバーで _DEBUG=False_ に設定し、Django を立ち上げていると、css などの static ファイルが読み込まれない。

### 参考

- LINE Bot 系
- [LINE Messaging API SDK for Python](https://github.com/line/line-bot-sdk-python)
- [ngrok を用いてテストする](https://qiita.com/sanpo_shiho/items/f9aa58ff8c6df2800594#ngrok%E3%82%92%E7%94%A8%E3%81%84%E3%81%A6%E3%83%86%E3%82%B9%E3%83%88%E3%81%99%E3%82%8B)

- サーバーサイドから LINE の API を叩いて Client にプッシュ通知を送る際に呼び出すメソッドの push_message
- このメソッドを呼び出す際に、あらかじめ Bot の参加しているグループの ID を知っている必要がある。
- [push_message(self, to, messages, notification_disabled=False, timeout=None)](https://github.com/line/line-bot-sdk-python#push_messageself-to-messages-notification_disabledfalse-timeoutnone)
- [Send push message](https://developers.line.biz/en/reference/messaging-api/#send-push-message)

- Django 系
- [Django で fixture を使う](https://qiita.com/zakuro9715/items/f650c087e82c01ed8366#fixture%E3%81%AE%E5%88%A9%E7%94%A8)
- [django-braces 1.14.0 ](https://pypi.org/project/django-braces/)
- [Django 歴約 3 年のエンジニアが今使っているライブラリを紹介してみる](https://qiita.com/ryu22e/items/b7149245872d54006d5c#django-braces)
- [Django CSRF Verifcation failed - Class based views](https://stackoverflow.com/questions/33052063/django-csrf-verifcation-failed-class-based-views)
- [Extra instance methods¶](https://docs.djangoproject.com/ja/3.0/ref/models/instances/#extra-instance-methods)
- [setting.py の変数値を取得する](http://flame-blaze.net/question/setting-py-%E3%81%AE%E5%A4%89%E6%95%B0%E5%80%A4%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B)

- Django で任意の処理を定期的に実行させる
- [Django で cron](https://medium.com/inet-lab/django%E3%81%A7cron-31096152aa4d)

- Python 系
- [python-dotenv を使って環境変数を設定する](https://qiita.com/harukikaneko/items/b004048f8d1eca44cba9)

- その他
- [ngrok を ubuntu18.04 上にインストール](https://qiita.com/RayDoe/items/8a68f40d165819b82463#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
