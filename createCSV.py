import tldextract
import vt
import time
import csv

import jsonarray2dict
import csv2dict

import regex
import script
import domain
import virustotal


#json_array = '[{"id":1, "URL":"https://www.oit.ac.jp"},{"id":2, "URL":"https://www.youtube.com/"}]'
#url_dict = jsonarray2dict.Json2Dict(json_array)
url_dict = csv2dict.Csv2Dict("ryousei.csv")
print(url_dict)

#start = time.time()

#OK
#print("domain")
domain_dict = domain.domain_check(url_dict)
#domain_dict = {1: {'domain': 1}, 2: {'domain': 2}}

#OK
#print("mscript")
mscript_dict = script.detect_malscript(url_dict)
#mscript_dict = {1: {'network': 3, 'extend': 4}, 2: {'network': 5, 'extend': 6}}

#OK
#print("regex")
reg_dict = regex.regex_check(url_dict)
#reg_dict = {1: {'regex1': 7, 'regex2': 8}, 2: {'regex1': 9, 'regex2': 10}}

#OK 必要以上に回さない
#print("virustotal")
#virustotal_dict = virustotal.virustotal_check(url_dict)
virustotal_dict = {1: {'virustotal': 11}, 2: {'virustotal': 12}}

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
csv_list = []
csv_list.append(['id', 'url', 'domain', 'network', 'extend', 'regex1', 'regex2', 'regex3', 'regex4', 'regex5', 'virustotal', 'isaffi'])
for i in range(len(url_dict)):
    id = i+1
    res = results[id]
    csv_list.append(list(res.values()))
print(csv_list)

# 出力
with open('result.csv', 'w', newline="\n") as f:
    writer = csv.writer(f)
    writer.writerows(csv_list)
    