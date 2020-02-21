import json
import re
import glob

from mapping import *

dict_data = {}
dict_data['samsung'] = []
dict_data['nokia'] = []
dict_data['apple'] = []
dict_data['oppo'] = []
dict_data['xiaomi'] = []
dict_data['lg'] = []
dict_data['huawei'] = []
dict_data['vivo'] = []

def get_arr_path(path_folder):
    path_folder = path_folder + '/*.json'
    arr_path = glob.glob(path_folder)
    return arr_path

def get_name_source(path):
    data_source = read_file(path)
    arr_name = []
    for data in data_source:
        name = data['name']
        if name != None:
            brand = data['brand']
            pattern_name = get_pattern_name(name, brand)
            if brand == 'samsung':
                dict_data['samsung'].append(pattern_name)
            elif brand == 'nokia':
                dict_data['nokia'].append(pattern_name)
            elif brand == 'apple':
                dict_data['apple'].append(pattern_name)
            elif brand == 'oppo':
                dict_data['oppo'].append(pattern_name)
            elif brand == 'xiaomi':
                dict_data['xiaomi'].append(pattern_name)
            elif brand == 'vivo':
                dict_data['vivo'].append(pattern_name)
            else:
                pass

    return dict_data['nokia'], dict_data['apple'], dict_data['oppo'], dict_data['xiaomi'],dict_data['lg'], dict_data['huawei'], dict_data['vivo']

# dict_data['nokia'], dict_data['apple'], dict_data['oppo'], dict_data['xiaomi'],dict_data['lg'], dict_data['huawei'], dict_data['vivo'] = get_name_source('/home/ngocmai/CRAWL/aliscrapy/aliscrapy/data_b4/lazada.json')
# print(dict_data['apple'])
set_ram = ['512mb', '256mb', '1gb', '2gb', '3gb', '4gb', '6gb', '8gb']
set_rom = ['32gb', '64gb', '128gb', '256gb']
arr_brand = ['samsung', 'nokia', 'apple', 'oppo', 'vivo', 'xiaomi', 'lg', 'huawei']
source = ['lazada', 'fptshop', 'the']

over_arr_name = []
arr_path = get_arr_path('/home/ngocmai/CRAWL/aliscrapy/aliscrapy/data_b4')

for path in arr_path:
    dict_data['nokia'], dict_data['apple'], dict_data['oppo'], dict_data['xiaomi'],dict_data['lg'], dict_data['huawei'], dict_data['vivo'] = get_name_source(path)
    
    dict_data['nokia'] += dict_data['nokia']
    dict_data['nokia'] = list(set(dict_data['nokia']))

    dict_data['apple'] += dict_data['apple']
    dict_data['apple'] = list(set(dict_data['apple']))

    dict_data['oppo'] += dict_data['oppo']
    dict_data['oppo'] = list(set(dict_data['oppo']))

    dict_data['xiaomi'] += dict_data['xiaomi']
    dict_data['xiaomi'] = list(set(dict_data['xiaomi']))

    dict_data['lg'] += dict_data['lg']
    dict_data['lg'] = list(set(dict_data['lg']))

    dict_data['huawei'] += dict_data['huawei']
    dict_data['huawei'] = list(set(dict_data['huawei']))

    dict_data['vivo'] += dict_data['vivo']
    dict_data['vivo'] = list(set(dict_data['vivo']))

    # for brand in arr_brand:
    #     dict_data[brand] += dict_data[brand]
    #     dict_data[brand] = list(set(dict_data[brand]))
# print(lensamsung(dict_data['samsung']))
# each brand

pattern_dict = {}
for brand in arr_brand:
    pattern_dict[brand] = []
    for name in dict_data[brand]:
        product = {}
        product['pattern_name'] = name
        for rom in set_rom:
            product['rom'] = rom
            for ram in set_ram:
                product['ram'] = ram
                pattern_dict[brand].append(product)
# print(len(pattern_dict['nokia']))
pattern_lazada = mapping('aliscrapy/data_b4/tgdd.json')
# # print(pattern_lazada)
# partern_tgdd = mapping('aliscrapy/data_b4/tgdd.json')
# # print(partern_tgdd)

def compare(dict_product_a, dict_product_b):
    if dict_product_a['pattern_name'] == dict_product_b['pattern_name']:
        print("trung ten", dict_product_a, "\n", dict_product_b)
        if dict_product_a['rom'] == dict_product_b['rom']:
            print("trung", dict_product_a, "\n", dict_product_b)
        else:
            pass
            # print("cho no khac nhau")

for product_a in pattern_lazada['samsung']:
    for product_b in pattern_dict['samsung']:
        compare(product_a, product_b)
