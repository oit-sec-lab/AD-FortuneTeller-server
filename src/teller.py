import tldextract
import vt
import time
import csv

import jsonarray2dict as jsonarray2dict
import csv2dict as csv2dict

from domain.domain import domain_check
from mscript.filter import filter, make_dict
from crawling.crawling import Crawler
from regex.regex import apply_regex
from virustotal.virustotal import VT_search_10

# 辞書に追加
results = {}

def create_results(recv_json):
   json_array = recv_json
   url_dict = jsonarray2dict.Json2Dict(json_array)
   print(url_dict)

   start = time.time()

   #OK
   print("domain")
   domain_dict = domain_check(url_dict)
   print(domain_dict)
   #domain_dict = {1: {'domain': 1}, 2: {'domain': 0},...}


   #OK
   print("mscript")
   dict_extend, dict_network = filter(url_dict)
   mscript_dict = make_dict(dict_extend, dict_network)
   print(mscript_dict)
   #mscript_dict = {1: {"network": 0, "extend": 1}, 2: {"network": 0, "extend": 1}, ...}

   #OK
   print("regex")
   craw_dict = Crawler().clawing_check(url_dict)
   reg_dict = apply_regex(craw_dict)
   #reg_dict = {1: {"regex1": 0, "regex2": 0, "regex3": 0, "regex4": 0, "regex5": 1}, 2: {"regex1": 0, "regex2": 0, "regex3": 0, "regex4": 0, "regex5": 1}, ...}

   #OK 必要以上に回さない
   print("virustotal")
   virustotal_dict = VT_search_10(url_dict)
   #virustotal_dict = {1: {"VirusTotal": 1}, 2: {"VirusTotal": 0}, ...}

   print("time: ", time.time() - start)

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
      result['virustotal'] = virustotal_dict[id]['VirusTotal']

      results[id] = result
