# AD-FortuneTeller-server
AD-FortuneTeller(https://github.com/oit-sec-lab/AD-FortuneTeller-front) のサーバープログラムです。
<br>
現在外部公開用のリソースで公開していないので、ローカルで利用してもらう事が前提となっています。

## 起動手順
本リポジトリをクローン後、VirusTotalのAPIキーを取得し、/src/.envに
API_KEY1="APIキー1"API_KEY1="APIキー2"API_KEY1="APIキー3"を設定してください。
```
// /src/.env
API_KEY1="APIキー1"
API_KEY2="APIキー2"
API_KEY3="APIキー3"
```
その後、リポジトリ内のserver.pyを実行してください。
<br>

## 利用手順
AD-FortuneTeller(https://github.com/oit-sec-lab/AD-FortuneTeller-front) のcontent.jsを一行目のURLを
<br>
**"http://127.0.0.1:5000/"** に変更する必要があります。

```
// content.js

let URL = "http://127.0.0.1:5000/"
```
その後、AD-FortuneTellerをchromeの拡張として読み込ませると利用が可能です。
<br>
詳しくはAD-FortuneTeller(https://github.com/oit-sec-lab/AD-FortuneTeller-front) のREADMEを参照してください。
