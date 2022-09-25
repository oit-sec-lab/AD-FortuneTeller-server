from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from urllib3.exceptions import InsecureRequestWarning
import urllib3
import requests

def integrated_filter(urls,elms,associative,driver):
    urllib3.disable_warnings(InsecureRequestWarning)
    fl_network = 0
    fl_extend = 0
    ret_network_dict = {}
    ret_extend_dict = {}

    for i in range(1,len(associative)+1):
        driver.get(associative[i])
        fl_network = 0
        fl_extend = 0
        # Access requests via the `requests` attribute
        for request in driver.requests:
            #network filter
            if fl_network == 0:
                for url in urls:
                    if url in request.url:
                        fl_network = 1
                        break
            
            #extend filter
            if fl_extend == 0:
                try:
                    content_type = request.response.headers['Content-Type']
                    if ("text/html" in content_type) or ("text/javascript" in content_type):
                        body = requests.get(request.url, verify=False).text
                        for elm in elms:
                            if elm in body:
                                fl_extend = 1
                                break
                        else:
                            continue
                    if fl_extend == 1:
                        break
                except Exception:
                    continue
                
        ret_extend_dict[i] = fl_extend
        ret_network_dict[i] = fl_network
        print(i)
    
    return ret_extend_dict, ret_network_dict

def filter(associative):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    #options.page_load_strategy = 'eager'
    # Create a new instance of the firefox driver
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

    with open("data/txt/filter_extend.txt","rt") as f:
        elms_extend = f.read().splitlines()
    
    with open("data/txt/filter_network.txt", "rt") as f:
        elms_network = f.read().splitlines()

    #with open("associative_array.txt","rt") as f:
    #    # str to dict
    #    associative = ast.literal_eval(f.read())
    
    #dict_extend = extended_filter(elms_extend,associative,driver)
    #dict_network = network_filter(elms_network,associative,driver)
    dict_extend, dict_network = integrated_filter(elms_network, elms_extend, associative, driver)
    return dict_extend, dict_network

def make_dict(dict_extend, dict_network):
    # both possible
    ret_dict = {}
    length = len(dict_extend)
    for i in range(1,length+1):
        ret_dict[i] = {"network": dict_extend[i], "extend": dict_network[i]}
    return ret_dict

def detect_malscript(associative_array):
    dict_extend, dict_network = filter(associative_array)
    final_dict = make_dict(dict_extend, dict_network)
    return final_dict