import vt
import time
import os

from dotenv import load_dotenv
load_dotenv()

def virustotal_check(url_dict):
    url_parm_dict = {}
    for d in url_dict.items():
        if int(d[0]) % 3 == 1:
            #print(d[0])
            # vtの処理開始
            client = vt.Client(os.environ['API_KEY1'])
            analysis = client.scan_url(d[1])
            while True:
                analysis = client.get_object("/analyses/{}", analysis.id)
                #print(analysis.status)
                if analysis.status == "completed":
                    break
                time.sleep(15)
            
            client.close()
            # vtの処理終了
            # 受け取ったJsonからmaliciousかsuspiciousの値が1以上で異常と判定
            # 参考https://developers.virustotal.com/reference/analyses-object
            if(analysis.get("stats").get("malicious") >= 1) or (analysis.get("stats").get("suspicious") >= 1):
                url_parm_dict.update({d[0]: {"virustotal": 1}})

            else:
                url_parm_dict.update({d[0]: {"virustotal": 0}})
        
        elif int(d[0]) % 3 == 2:
            #print(d[0])
            # vtの処理開始
            client = vt.Client(os.environ['API_KEY2'])
            analysis = client.scan_url(d[1])
            while True:
                analysis = client.get_object("/analyses/{}", analysis.id)
                #print(analysis.status)
                if analysis.status == "completed":
                    break
                time.sleep(15)
            
            client.close()
            # vtの処理終了
            # 受け取ったJsonからmaliciousかsuspiciousの値が1以上で異常と判定
            if(analysis.get("stats").get("malicious") >= 1) or (analysis.get("stats").get("suspicious") >= 1):
                url_parm_dict.update({d[0]: {"virustotal": 1}})

            else:
                url_parm_dict.update({d[0]: {"virustotal": 0}})

        else:
            # print(d[0])
            # vtの処理開始
            client = vt.Client(os.environ['API_KEY3'])
            analysis = client.scan_url(d[1])
            while True:
                analysis = client.get_object("/analyses/{}", analysis.id)
                # print(analysis.status)
                if analysis.status == "completed":
                    break
                time.sleep(15)
            
            client.close()
            # vtの処理終了
            # 受け取ったJsonからmaliciousかsuspiciousの値が1以上で異常と判定
            if(analysis.get("stats").get("malicious") >= 1) or (analysis.get("stats").get("suspicious") >= 1):
                url_parm_dict.update({d[0]: {"virustotal": 1}})

            else:
                url_parm_dict.update({d[0]: {"virustotal": 0}})

    return url_parm_dict

def virustotal_check_1000(url_dict):
    # ML作る用
    url_parm_dict = {}
    for d in url_dict.items():
        if int(d[0]) % 3 == 1:
            print(d[0])
            # vtの処理開始
            client = vt.Client(os.environ['API_KEY1'])
            analysis = client.scan_url(d[1])
            while True:
                analysis = client.get_object("/analyses/{}", analysis.id)
                print(analysis.status)
                if analysis.status == "completed":
                    break
                time.sleep(15)
            
            client.close()
            # vtの処理終了
            # 受け取ったJsonからmaliciousかsuspiciousの値が1以上で異常と判定
            # 参考https://developers.virustotal.com/reference/analyses-object
            if(analysis.get("stats").get("malicious") >= 1) or (analysis.get("stats").get("suspicious") >= 1):
                url_parm_dict.update({d[0]: {"VirusTotal": 1}})

            else:
                url_parm_dict.update({d[0]: {"VirusTotal": 0}})
        
        elif int(d[0]) % 3 == 2:
            print(d[0])
            # vtの処理開始
            client = vt.Client(os.environ['API_KEY2'])
            analysis = client.scan_url(d[1])
            while True:
                analysis = client.get_object("/analyses/{}", analysis.id)
                print(analysis.status)
                if analysis.status == "completed":
                    break
                time.sleep(15)
            
            client.close()
            # vtの処理終了
            # 受け取ったJsonからmaliciousかsuspiciousの値が1以上で異常と判定
            if(analysis.get("stats").get("malicious") >= 1) or (analysis.get("stats").get("suspicious") >= 1):
                url_parm_dict.update({d[0]: {"VirusTotal": 1}})

            else:
                url_parm_dict.update({d[0]: {"VirusTotal": 0}})

        else:
            print(d[0])
            # vtの処理開始
            client = vt.Client(os.environ['API_KEY3'])
            analysis = client.scan_url(d[1])
            while True:
                analysis = client.get_object("/analyses/{}", analysis.id)
                print(analysis.status)
                if analysis.status == "completed":
                    break
                time.sleep(15)
            
            client.close()
            # vtの処理終了
            # 受け取ったJsonからmaliciousかsuspiciousの値が1以上で異常と判定
            if(analysis.get("stats").get("malicious") >= 1) or (analysis.get("stats").get("suspicious") >= 1):
                url_parm_dict.update({d[0]: {"VirusTotal": 1}})

            else:
                url_parm_dict.update({d[0]: {"VirusTotal": 0}})

        path_virustotal = './virustotal_dump.json'
        json_virustotal_dump = open(path_virustotal, mode="w")
        json.dump(url_parm_dict, json_virustotal_dump)
        json_virustotal_dump.close()

    print("ID: category: true or false")
    print(url_parm_dict)
    return url_parm_dict