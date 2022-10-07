import vt
import time
import os

from dotenv import load_dotenv
load_dotenv()
apikey1 = os.environ['API_KEY1']
apikey2 = os.environ['API_KEY2']
apikey3 = os.environ['API_KEY3']

def VT_search_10(url_dict):
    url_parm_dict = {}
    for d in url_dict.items():
        if int(d[0]) % 3 == 0:
            # vtの処理開始
            client = vt.Client(apikey1)
            analysis = client.scan_url(d[1])
            while True:
                analysis = client.get_object("/analyses/{}", analysis.id)
                print(analysis.status)
                if analysis.status == "completed":
                    break
                time.sleep(15)

            client.close()
            print("1")
            # vtの処理終了
            # 受け取ったJsonからmaliciousかsuspiciousの値が1以上で異常と判定
            # 参考https://developers.virustotal.com/reference/analyses-object
            if(analysis.get("stats").get("malicious") >= 1) or (analysis.get("stats").get("suspicious") >= 1):
                url_parm_dict[d[0]] = {"VirusTotal": 1}

            else:
                url_parm_dict[d[0]] = {"VirusTotal": 0}

        elif int(d[0]) % 3 == 1:
            # vtの処理開始
            client = vt.Client(apikey2)
            analysis = client.scan_url(d[1])
            while True:
                analysis = client.get_object("/analyses/{}", analysis.id)
                print(analysis.status)
                if analysis.status == "completed":
                    break
                time.sleep(15)

            client.close()
            print("2")
            # vtの処理終了
            # 受け取ったJsonからmaliciousかsuspiciousの値が1以上で異常と判定
            if(analysis.get("stats").get("malicious") >= 1) or (analysis.get("stats").get("suspicious") >= 1):
                url_parm_dict[d[0]] = {"VirusTotal": 1}

            else:
                url_parm_dict[d[0]] = {"VirusTotal": 0}

        else:
            client = vt.Client(apikey3)
            analysis = client.scan_url(d[1])
            while True:
                analysis = client.get_object("/analyses/{}", analysis.id)
                print(analysis.status)
                if analysis.status == "completed":
                    break
                time.sleep(15)

            client.close()
            print("3")
            # 受け取ったJsonからmaliciousかsuspiciousの値が1以上で異常と判定
            if(analysis.get("stats").get("malicious") >= 1) or (analysis.get("stats").get("suspicious") >= 1):
                url_parm_dict[d[0]] = {"VirusTotal": 1}
                
            else:
                url_parm_dict[d[0]] = {"VirusTotal": 0}

    print(url_parm_dict)
    return url_parm_dict


if __name__ == '__main__':
    VT_search_10(url_dict)
