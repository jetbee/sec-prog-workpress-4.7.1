import requests
from bs4 import BeautifulSoup

# WordPressのURLと更新対象の投稿ID
rest_api_url = http://[マシンのIPアドレス]:8080/wp-json/wp/v2/posts/[記事のID]?id=[記事のID]'  # 更新用URL
login_url = 'http://[マシンのIPアドレス]:8080/wp-login.php'

# WordPressのログイン情報と書き換えたい記事の内容
username = 'admin'
password = 'abcd1234'
title: 'Updated Title by Authorized User',
content: 'This post was updated using a valid session.'

# セッションを作成
session = requests.Session()

# ログインページにアクセスして、ログイン用のnonceを取得
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.content, 'html.parser')

# nonce を取得する (ログインページに埋め込まれている hidden input の値)
nonce_input = soup.find('input', {'name': 'log'})  # WordPressのnonceを探す
if nonce_input:
    nonce = nonce_input.get('value')
else:
    nonce = None  # nonce が見つからない場合の対策

# ログインに必要なデータを送信
login_data = {
    'log': username,           # ユーザー名
    'pwd': password,           # パスワード
    'wp-submit': 'Log In',     # ボタン名
    'redirect_to': base_url,   # リダイレクト先
    'testcookie': '1'          # WordPressのクッキーをテスト
}

# ログインリクエストを送信
login_response = session.post(login_url, data=login_data)

# ログイン成功を確認
if "dashboard" in login_response.url:
    print("Login successful!")
else:
    print("Login failed. Check your credentials.")

# 認証済みのセッションを使って、投稿を更新する
update_data = {
    'title': title,
    'content': content
}

# 認証されたセッションを使って投稿を更新
response = session.post(rest_api_url, json=update_data)

# レスポンス確認
print("Status code: ", response.status_code)
if response.status_code == 200:
    print("Post update successful!")
    print(response.json())
else:
    print("Failed to update the post.")

