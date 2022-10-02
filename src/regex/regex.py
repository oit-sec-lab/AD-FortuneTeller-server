import csv
#from types import NoneType
import requests
from bs4 import BeautifulSoup as bs
import re

# サイト内のページを見る個数
MAX_ROOP = 20
# かける正規表現のリスト
patterns = ["いかがで[したか,しょうか]","調べ[ました,てみました,てみた]","調査しました","まとめ[ました,てみました]","[わかりました,分かりました]"]

def parse_list(list):
    flag = {}
    for i in range(len(patterns)):             # 初期値設定
        key = "regex"+str(i+1);
        flag[key] = 0
    for i, el in enumerate(list):   # リストの各要素(URL)毎に処理
        if i >= MAX_ROOP:           # ループ回数の監視
            break
        text = get_text(el)         # BSでテキストのみスクレイピング
        if type(text) == type(None):  # 取得失敗の場合次へ
            continue
        for i,pattern in enumerate(patterns):    # 正規表現リストから各パターンを読み込んで処理
            key = "regex"+str(i+1);
            if flag[key]:       # たっているフラグは無視
                continue
            else:                   # たっていないフラグのみ正規表現をかける
                cmp = re.compile(pattern)
                try:
                    if cmp.search(text):
                        flag[key] = 1
                except:
                    continue
    print(flag)
    return flag

def get_text(url):
    try:
        html = requests.get(url, timeout=5.0).text
    except:
        return
    soup = bs(html, "html.parser")
    text = soup.get_text(strip=True)                      # テキストの取得
    return text

def apply_regex(csv_file):                  # csvを引数に受け取り
    dict = {}
    for i, row in enumerate(csv_file):      # 行毎の処理(サイト毎の処理)
        append = parse_list(row)    
        dict[i+1] = append                  # {id: {regex#: bool, regex#: bool, ...}, id: {...}, ...}
                                            # id:int regex#:str bool:int{0,1}
    return dict

if __name__ == "__main__":
    csv.field_size_limit(1000000000)
    with open("url.csv", encoding="utf-8") as urlcsv:
        reader = csv.reader(urlcsv)
        dict = apply_regex(reader)
        print(dict)
        print("next")