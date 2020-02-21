import requests
import json
import urllib

param = {
    "trafficChannel":"main",
    "catName":"cellphones",
    "CatId":"5090301",
    "ltype":"wholesale",
    "SortType":"default",
    "page":"2",
    "origin":"y"
}
# params = urllib.urlencode(param)

header = {
    "authority":"vi.aliexpress.com",
    "method":"get",
    "path":"/glosearch/api/product?trafficChannel=main&catName=luggage-bags&CatId=1524&ltype=wholesale&SortType=default&page=3&isrefine=y&origin=y",
    "scheme":"https",
    "accept":"application/json, text/plain, */*",
    "accept-encoding":"gzip, deflate, br",
    "cookie":'ali_apache_id=10.182.215.5.1580455532745.162933.1; cna=b8S6FgdB1FACAbdReIN9nWti; _ga=GA1.2.934128861.1580455540; _fbp=fb.1.1580455540661.1088407360; _bl_uid=kwkhe6IX17zuXyfenqabu5y7hed2; ali_beacon_id=10.182.215.5.1580455532745.162933.1; _fbc=fb.1.1580639454907.IwAR0MKiL-kZ1cJRXK93RBsr4ay5PEGnXNEX9N0sO7a3LmnNp1NvBqyg10sYo; aeu_cid=9868ff81cdbb4ee6ac5d615faf3512a4-1581415374930-04879-UneMJZVf; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%094000166877975%0932954335894%0932948190249%0932954335894%0932948190249%0932954335894%094000219072013%094000148128270; aep_common_f=lb4sglRtqpmzdDaEsydWzDewBVWDwlF/aDPs7k3LL+q0Ii4bXSu7xw==; xman_f=de89n0KjhDiFH2QWrE92hVKFRGLOVvWPhLTRBBrDiAicsZNJnEvCwLy9y9PqpxMvu+y5Ug+YqsjdIiVB2idHoJd7gjo5J+s4fyojNW2qQPF7U9dH4c19TOnxYX38LasUlOZYtLW1Ho5YZQXki8U52FB14cX/AaxDOIR4l7brElCNUBCpxQy+/40XvqaHJYdckMla7q17KHUTSnKTilytWnM5s84m1LneBZSyrGe2gHRSa1MiHaPA21KZqK7DSO0hqdGtgUbmgioWOqCP7pceYAkZ6mcAqXWqGBBIaZU6OPftZatCimM83zAwIPPziHETBAA0njHGmURAwf/Ls+QzXpwHpvU2uMZq4itBaOA8JNiZTqFweY3wYnBH8fMMn02M; aep_usuc_f=site=vnm&c_tp=USD&x_alimid=2401786775&isb=y&region=VN&b_locale=vi_VN; ali_apache_track=mt=1|mid=vn799645775gyoae; _m_h5_tk=d61d59fc82639728ccbcbf275529ba20_1581671013913; _m_h5_tk_enc=ed8762aaea4d3fcff33e7771bd05f450; acs_usuc_t=x_csrf=12lbfnjouedtt&acs_rt=32ba8e806bc0469ca74fedc6dac925e6; intl_locale=vi_VN; xman_t=mKnu8qaPldRlqf6TmPVo2onP3gLP85b0acXoiQEQnM0fsahocs2YVh5P62RA3nMk; AKA_A2=A; ali_apache_tracktmp=; _gid=GA1.2.133790768.1582008389; intl_common_forever=+xks8/ahLG2wOhbLeZexPju/WSIumIbAeEZL+J9/UvXqV3gxwSvzMQ==; JSESSIONID=6874CAF167955E713774CA222F86EFFA; RT="sl=1&ss=1582008392202&tt=3107&obo=0&sh=1582008396309%3D1%3A0%3A3107&dm=aliexpress.com&si=1ca963c7-c7f5-4d68-9b68-ae3c2d3cbe58&se=900&bcn=%2F%2F684d0d3d.akstat.io%2F&ld=1582008396309&nu=https%3A%2F%2Fvi.aliexpress.com%2Fcategory%2F5090301%2F-i-n-tho-i-di---ng.html%3F4cb2ba206f23d36e020ead3706300630&cl=1582008410548&r=https%3A%2F%2Fwww.aliexpress.com%2Fcategory%2F509%2Fcellphones-telecommunications.html%3F847e69d2a185c62ab62b1125ba52a08f&ul=1582008410592&hd=1582008411454"; xman_us_f=x_l=0&x_locale=vi_VN&x_user=VN|VN|shopper|ifm|2401786775&x_c_chg=0&zero_order=y&acs_rt=48468624fc6444e9a86e265e6edf592e&x_as_i=%7B%22aeuCID%22%3A%222f167669907e4b6b83ce346f0cb488e4-1580694219306-08197-dg7rmda%22%2C%22affiliateKey%22%3A%22dg7rmda%22%2C%22channel%22%3A%22AFFILIATE%22%2C%22cv%22%3A%221%22%2C%22isCookieCache%22%3A%22N%22%2C%22ms%22%3A%221%22%2C%22pid%22%3A%22726927582%22%2C%22src%22%3A%22link-c-tool%22%2C%22tagtime%22%3A1580694219306%7D; l=cBgE3LVrQ_0gYhHvBOfClurza77TzIOb8SVzaNbMiICPOpfwt3vcWZVMibLeCnHNLsCv83zwUESzBuLEJy4ohlOS4JSYDN_R.; isg=BLGxa4t9Swu3S-dn1RnOeYZowDRLniUQyL4osZPH8XgtutMM2O-u4QWc3VbcSr1I',
    "referer":'https://vi.aliexpress.com/category/5090301/cellphones.html?trafficChannel=main&catName=cellphones&CatId=5090301&ltype=wholesale&SortType=default&page=2',
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"

}

url="https://vi.aliexpress.com/category/1524/luggage-bags.html"
api_url = 'https://vi.aliexpress.com/glosearch/api/product?trafficChannel=main&catName=cellphones&CatId=5090301&ltype=wholesale&SortType=default&page=2&origin=y'
data = requests.get(api_url, params=param, headers=header).json()
print(data)
# data = requests.get(url, params=params, headers=header)
# data = urllib.request.Request(url, data=params, headers=header)
# f = urllib.request.urlopen(data)
# print(f.read().decode('utf-8'))
# print(data)
# data_page = data.text
# data_json = json.loads(data_page)
# print(data_page)
