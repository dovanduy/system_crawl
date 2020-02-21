# import requests
# import json
# import urllib.request
# import re

# params = {
#     "by":"relevancy",
#     "limit":"50",
#     "match_id":"77",A
#     "newest":"0",
#     "order":"desc",
#     "page_type":"search",
#     "version":"2",
# }

# header_nu = {
#     "authority":"shopee.vn",
#     "method":"get",
#     "path":"/api/v2/search_items/?by=relevancy&limit=50&match_id=77&newest=50&order=desc&page_type=search&version=2",
#     "scheme":"https",
#     "accept":"*/*",
#     "accept-encoding":"gzip, deflate, br",
#     "accept-language":"en-US,en;q=0.9",
#     "cookie":'_gcl_au=1.1.621707165.1579161766; _fbp=fb.1.1579161767014.388585047; SPC_IA=-1; SPC_EC=-; SPC_U=-; SPC_F=1tElh3F4GuVHcyHosAoSlESfEBNEYisi; REC_T_ID=9578b82a-3836-11ea-b67e-20283e72225b; _ga=GA1.2.181062124.1579161770; _hjid=c9000383-684a-42c0-89a4-6bc73ccc5579; _gcl_aw=GCL.1580525555.Cj0KCQiAvc_xBRCYARIsAC5QT9mGGQDGmJEZ5u8QzCWynlQMrFkUsJ86EZKALsuvNZHzQBzQnkebBA8aAtsHEALw_wcB; _gac_UA-61914164-6=1.1580525563.Cj0KCQiAvc_xBRCYARIsAC5QT9mGGQDGmJEZ5u8QzCWynlQMrFkUsJ86EZKALsuvNZHzQBzQnkebBA8aAtsHEALw_wcB; _med=refer; csrftoken=M3St8mEpriXuv13g6rseiXGAlbkpZdZM; SPC_SI=zd520pzgc5k3s6osu533dfsx9ppj6oq8; welcomePkgShown=true; _gid=GA1.2.685027162.1581824112; REC_MD_20=1581828762; AMP_TOKEN=%24NOT_FOUND; SPC_R_T_ID="wjlM/O/Qt3FnuHQ2+JxFQZ/N3GNN6d79oHCOGNArTUTQqNe057G/ZWzyT5s8AC/JzDsz9HcS+x2TdoLRVimyKFNFg94ezT/Eg7vsU+4odjc="; SPC_T_IV="ueCIBBIFNFJba2Z6NOdbvg=="; SPC_R_T_IV="ueCIBBIFNFJba2Z6NOdbvg=="; SPC_T_ID="wjlM/O/Qt3FnuHQ2+JxFQZ/N3GNN6d79oHCOGNArTUTQqNe057G/ZWzyT5s8AC/JzDsz9HcS+x2TdoLRVimyKFNFg94ezT/Eg7vsU+4odjc="',
#     "if-none-match-":"55b03-da4f79148eb0e74e8dc3e80686650983",
#     "referer":"https://shopee.vn/Th%E1%BB%9Di-Trang-N%E1%BB%AF-cat.77?page=1",
#     "sec-fetch-dest":"empty",
#     "sec-fetch-mode":"cors",
#     "sec-fetch-site":"same-origin",
#     "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
#     "x-requested-with":"XMLHttpRequest",
#     "x-api-source":"pc",
# }
# header = {
#     "authority":"shopee.vn",
#     "method":"get",
#     "path":"/api/v2/search_items/?by=relevancy&limit=50&match_id=77&newest=50&order=desc&page_type=search&version=2",
#     "scheme":"https",
#     "accept":"*/*",
#     "accept-encoding":"gzip, deflate, br",
#     "accept-language":"en-US,en;q=0.9",
#     "cookie":'_gcl_au=1.1.621707165.1579161766; _fbp=fb.1.1579161767014.388585047; SPC_IA=-1; SPC_EC=-; SPC_U=-; SPC_F=1tElh3F4GuVHcyHosAoSlESfEBNEYisi; REC_T_ID=9578b82a-3836-11ea-b67e-20283e72225b; _ga=GA1.2.181062124.1579161770; _hjid=c9000383-684a-42c0-89a4-6bc73ccc5579; _gcl_aw=GCL.1580525555.Cj0KCQiAvc_xBRCYARIsAC5QT9mGGQDGmJEZ5u8QzCWynlQMrFkUsJ86EZKALsuvNZHzQBzQnkebBA8aAtsHEALw_wcB; _gac_UA-61914164-6=1.1580525563.Cj0KCQiAvc_xBRCYARIsAC5QT9mGGQDGmJEZ5u8QzCWynlQMrFkUsJ86EZKALsuvNZHzQBzQnkebBA8aAtsHEALw_wcB; _med=refer; csrftoken=M3St8mEpriXuv13g6rseiXGAlbkpZdZM; SPC_SI=zd520pzgc5k3s6osu533dfsx9ppj6oq8; welcomePkgShown=true; _gid=GA1.2.685027162.1581824112; REC_MD_20=1581828762; AMP_TOKEN=%24NOT_FOUND; SPC_R_T_ID="wjlM/O/Qt3FnuHQ2+JxFQZ/N3GNN6d79oHCOGNArTUTQqNe057G/ZWzyT5s8AC/JzDsz9HcS+x2TdoLRVimyKFNFg94ezT/Eg7vsU+4odjc="; SPC_T_IV="ueCIBBIFNFJba2Z6NOdbvg=="; SPC_R_T_IV="ueCIBBIFNFJba2Z6NOdbvg=="; SPC_T_ID="wjlM/O/Qt3FnuHQ2+JxFQZ/N3GNN6d79oHCOGNArTUTQqNe057G/ZWzyT5s8AC/JzDsz9HcS+x2TdoLRVimyKFNFg94ezT/Eg7vsU+4odjc="',
#     # "if-none-match-":"55b03-da4f79148eb0e74e8dc3e80686650983",
#     "referer":"https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.78?page=1",
#     "sec-fetch-dest":"empty",
#     "sec-fetch-mode":"cors",
#     "sec-fetch-site":"same-origin",
#     "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
#     "x-requested-with":"XMLHttpRequest",
#     "x-api-source":"pc",
# }

# http_proxy  = "https://101.99.53.133:8888"
# # https_proxy = "https://10.10.1.11:1080"
# # ftp_proxy   = "ftp://10.10.1.10:3128"

# proxyDict = { 
#               "https"  : http_proxy, 
#             #   "https" : https_proxy, 
#             #   "ftp"   : ftp_proxy
#             }

# # api_url = "https://shopee.vn/api/v2/category_list/get"
# api_url = 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=78&newest=50&order=desc&page_type=search&version=2'
# api_url_nu = 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=77&newest=50&order=desc&page_type=search&version=2'
# list_api = [
#     'thời trang nam', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=78&newest=100&order=desc&page_type=search&version=2',
#     'thời trang nữ', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=77&newest=0&order=desc&page_type=search&version=2',
#     'thời trang nữ', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=77&newest=50&order=desc&page_type=search&version=2',
#     'Điện-Thoại-Phụ-Kiện-cat.84', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=84&newest=0&order=desc&page_type=search&version=2',
#     'mẹ và bé', 'ps://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=163&newest=0&order=desc&page_type=search&version=2',
#     'thiết bị điện tử', 'ps://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=2365&newest=50&order=desc&page_type=search&version=2',
#     'nhà cửa đời sống ', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=87&newest=0&order=desc&page_type=search&version=2',
#     'máy tính laptop', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=13030&newest=0&order=desc&page_type=search&version=2',
#     'sức khỏe sắc đẹp', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=160&newest=0&order=desc&page_type=search&version=2',
#     'máy ảnh máy quay phim', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=13033&newest=0&order=desc&page_type=search&version=2',
#     'dày dép nữ', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=161&newest=0&order=desc&page_type=search&version=2',
#     'đồng hồ', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=9607&newest=0&order=desc&page_type=search&version=2',
#     'túi ví', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=162&newest=0&order=desc&page_type=search&version=2',
#     'giày dép nam', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=2429&newest=0&order=desc&page_type=search&version=2',
#     'phụ kiện thời trang', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=80&newest=0&order=desc&page_type=search&version=2',
#     'thiết bị gia dụng', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=2353&newest=0&order=desc&page_type=search&version=2',
#     'bách hóa online', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=9824&newest=0&order=desc&page_type=search&version=2',
#     'thể thao du lịch', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=9675&newest=0&order=desc&page_type=search&version=2',
#     'voutch và dịch vụ', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=12938&newest=0&order=desc&page_type=search&version=2',
#     'ô tô xe máy', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=12494&newest=0&order=desc&page_type=search&version=2',
#     'đồ chơi', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=13242&newest=0&order=desc&page_type=search&version=2',
#     'giawtj dũ chăm sóc nhà cửa', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=17101&newest=0&order=desc&page_type=search&version=2',
#     'chăm sóc thú cưng', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=18977&newest=0&order=desc&page_type=search&version=2',
#     'thời trang trẻ em', 'https://shopee.vn/api/v2/search_items/?by=relevancy&limit=50&match_id=16770&newest=0&order=desc&page_type=search&version=2'
# ]

# # data = requests.get(api_url, params=params).json()
# data = requests.get(api_url, params=params, headers=header_nu).json()
# print(data)
# items = data['items']
# products = {}
# for _ in items:
#     products['itemid'] = _['itemid']
#     # products[]

# # data_page = data.text
# # # data_json = json.loads(dcustom_settingsata_page)
# # items = re.search('(\"items\":).*(\"productType\":\"ordinary_product\"}])', data_page)
# # print(items)