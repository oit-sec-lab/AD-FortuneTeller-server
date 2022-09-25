import tldextract
import vt
import time
import csv

import jsonarray2dict as jsonarray2dict
import csv2dict as csv2dict

import regex as regex
import script as script
import domain as domain
import virustotal as virustotal


json_array = '[{"id":1, "URL":"https://www.oit.ac.jp"},{"id":2, "URL":"https://www.youtube.com/"}]'
url_dict = jsonarray2dict.Json2Dict(json_array)
# url_dict = csv2dict.Csv2Dict("data/csv/ryousei.csv")
# print(url_dict)

#start = time.time()

#OK
#print("domain")
# domain_dict = domain.domain_check(url_dict)
domain_dict = {1: {'domain': 1}, 2: {'domain': 0}}

#OK
#print("mscript")
# mscript_dict = script.detect_malscript(url_dict)
mscript_dict = {1: {'network': 1, 'extend': 1}, 2: {'network': 1, 'extend': 0}}

#OK
#print("regex")
# reg_dict = regex.regex_check(url_dict)
reg_dict = {1: {'regex1': 1, 'regex2': 0, 'regex3': 1, 'regex4': 1, 'regex5': 1}, 2: {'regex1': 1, 'regex2': 0, 'regex3': 1, 'regex4': 1, 'regex5': 1}}

#OK 必要以上に回さない
#print("virustotal")
#virustotal_dict = virustotal.virustotal_check(url_dict)
virustotal_dict = {1: {'virustotal': 0}, 2: {'virustotal': 1}}

#print("time: ", time.time() - start)

# 辞書に追加 
results = {}

for i in range(len(url_dict)):
   id = i+1
   result = {}

   result['id'] = id
   result['url'] = url_dict[id]
   result['domain'] = domain_dict[id]['domain']
   result['network'] = mscript_dict[id]['network']
   result['extend'] = mscript_dict[id]['extend']
   result['regex1'] = reg_dict[id]['regex1']
   result['regex2'] = reg_dict[id]['regex2']
   result['regex3'] = reg_dict[id]['regex3']
   result['regex4'] = reg_dict[id]['regex4']
   result['regex5'] = reg_dict[id]['regex5']
   result['virustotal'] = virustotal_dict[id]['virustotal']
   result['isaffi'] = 1

   results[id] = result

# csvファイルの作成
# csv_list = []
# csv_list.append(['id', 'url', 'domain', 'network', 'extend', 'regex1', 'regex2', 'regex3', 'regex4', 'regex5', 'virustotal', 'isaffi'])
# for i in range(len(url_dict)):
#     id = i+1
#     res = results[id]
#     csv_list.append(list(res.values()))
# print(csv_list)

# 出力
# with open('result.csv', 'w', newline="\n") as f:
#    writer = csv.writer(f)
#    writer.writerows(csv_list)
    