import json

# urllibという標準ライブラリからurlopen関数だけをインポートする。
from urllib.request import urlopen

# url変数にYoutubeのURLを代入する。
#url = "https://raw.githubusercontent.com/koki0702/introducingpython/master/dummy_api/youTube_top_rated.json"
url = "https://www.youtube.com/watch?v=Ntn1-SocNiY"

# 指定されたURLのウェブサーバーに接続し、特定のウェブサービスを要求する。
response = urlopen(url)

# 応答データを受け取り、contents変数に代入する。
contents = response.read()

# contentsをJSON形式の文字列にデコードし、結果をtext変数に代入する。
text = contents.decode('utf8')

# textをdata、すなわちPythonのデータ構造に変換する。
data = json.loads(text)

# 動画についての情報を一度にひとつずつvideo変数に取り出す。
# 2レベルのPython辞書（data['feed']['entry']）とスライス（[0:6]）を使って情報を切り出す。
for video in data['feed']['entry'][0:6]:
    
    # print関数を使って動画のタイトルだけを表示する。
    print(video['title']['$t'])