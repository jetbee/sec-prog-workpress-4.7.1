# sec-prog-workpress-4.7.1

```bash
docker compose up -d
```

## wordpressの初期設定

http://[your docker machine ip]:8080/
にアクセス

```text
db-name: wordpress
db-user: wordpress
db-password: wordpress
db-host: db

user: admin (任意)
password: abcd1234 (任意)
e-mail: almalinux@localhost.localdomain
```


### Wordpress 4.7 のREST APIの機能

- Wordpress 4.7 では、REST APIから、記事の更新ができる機能があります。ログイン済みセッションであれば、記事の更新が可能です。

### 記事の更新APIを確認する

1. 管理画面から適当な記事を作成します。

2. 記事のIDを確認します。

3. スクリプトでAPIでの更新を確認します。

```bash
cd verification/
pip install requests beautifulsoup4
vi normal.py
```

- ログインURLとREST APIのURL（ホスト名と記事のID）を書き換えます。
- 管理者のID・パスワードを書き換えます。
- スクリプトの全景を確認します。ログイン後、REST APIにPOSTして記事を書き換えています。
- スクリプトを実行します。

```bash
python3 ./normal.py
```

- 成功後、Wordpress上で記事が書き換わったことを確認します。


### ログインなしで記事の書き換えを試行します

```bash
vi attack.py
```

- ログインURLとREST APIのURL（ホスト名と記事のID）を書き換えます。
- スクリプトの全景を確認します。ID,パスワードでの認証がないことを確認します。
- REST APIにPOSTして記事を書き換えようとしています。
- スクリプトを実行します。

```bash
python3 ./attack.py
```

