from flask import Flask
from flask import request
from flask_cors import CORS
import json

import teller
import checkURL

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)

@app.route("/", methods=['POST'])
def postURL():
    # POSTで送られてきたjson配列データ受け取り
    post_url_data = request.get_data()
    # json配列データをtellerに渡して結果をteller.resultsに保存
    teller.create_results(post_url_data)
    # 機械学習を用いて判定した結果を受け取り
    ml_results = checkURL.makedict()
    #print(ml_results)
    #dic = {1: {"ad": True}, 2: {"ad": False}, 3: {"ad": False}, 4: {"ad": False}, 5: {"ad": True}, 6: {"ad": False}, 7: {"ad": True}}
    ret_dict = json.dumps(ml_results)

    print("ret_dict")
    print(ret_dict)

    return  ret_dict, 200

app.run(host="127.0.0.1", port=5000)