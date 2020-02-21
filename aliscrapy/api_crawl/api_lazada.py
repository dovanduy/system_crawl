# import requests
# import json
# import urllib.request
# import re

# params = {
#     "trafficChannel":"main",
#     "catName":"luggage-bags",
#     "CatId":"1524",
#     "ltype":"wholesale",
#     "SortType":"default",
#     "page":"3",
#     "isrefine":"y",
#     "origin":"y"

# }

# header = {
#     "authority":"vi.aliexpress.com",
#     "method":"get",
#     "path":"/glosearch/api/product?trafficChannel=main&catName=luggage-bags&CatId=1524&ltype=wholesale&SortType=default&page=3&isrefine=y&origin=y",
#     "scheme":"https",
#     "accept":"application/json, text/plain, */*",
#     "accept-encoding":"gzip, deflate, br",
#     "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"

# }

# http_proxy  = "https://101.99.53.133:8888"
# # https_proxy = "https://10.10.1.11:1080"
# # ftp_proxy   = "ftp://10.10.1.10:3128"

# proxyDict = { 
#               "https"  : http_proxy, 
#             #   "https" : https_proxy, 
#             #   "ftp"   : ftp_proxy
#             }

# url="https://vi.aliexpress.com/category/1524/luggage-bags.html"

# data = requests.get(url, params=params, headers=header, proxies=proxyDict)

# data_page = data.text
# # data_json = json.loads(data_page)
# items = re.search('(\"items\":).*(\"productType\":\"ordinary_product\"}])', data_page)
# print(items)
# print(items.group(0))
# # group_items = items.group(0)
# # dumps_items = json.dumps(group_items)
# # json_items = json.loads(dumps_items)
# # print(json_items)


# # import requests 
  
# # # api-endpoint 
# # URL = "https://dantri.com.vn/the-gioi/hong-kong-so-tan-chung-cu-trong-dem-vi-ca-nhiem-n-co-v-nghi-qua-duong-ong-20200211094550813.htm"
  
# # # location given here 
# # location = "delhi technological university"
  
# # # defining a params dict for the parameters to be sent to the API 
# # PARAMS = {'address':location} 
  
# # # sending get request and saving the response as response object 
# # r = requests.get(url = URL) 
  
# # # extracting data in json format 
# # data = r.json() 
# # print(data)

# # import requests
# # r = requests.get('https://github.com/timeline.json')
# # data = r.json()
# # print(data)