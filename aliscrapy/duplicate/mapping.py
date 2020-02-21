import json
import re

def read_file(file):
    items = []
    with open(file, 'r', encoding='utf8', errors='ignore') as f:
        lines = f.readlines()
        lines = lines[1:-1]
        for line in lines:
            line = line.lower()
            try:
                data_line = line[:-2]
                item = json.loads(data_line)
            except:
                item = json.loads(line)

            items.append(item)
    return items

def get_pattern_name(name, brand):
    if brand == 'apple' and name.find('iphone') > 0:
        brand = 'iphone'

    if brand in name:
        ind_brand = name.index(brand)
        name = name[ind_brand:]
        if name.find('plus') > 0 or name.find('edge') > 0:
            partert = re.search('(plus)|(edge)', name)
            string = partert.group(0)
            ind_end = name.index(string) + 4
            name = name[:ind_end]
        if name.find('giá') > 0 or name.find('giảm') > 0:
            try:
                special_1 = re.search('(\d+ giá)|(\d+ giảm)', name)
                str_special1 = special_1.group(0)
                ind_str_special1 = name.index(str_special1)
                if ind_str_special1 > 0:
                    if name.find('giá') > 0:
                        ind_str_special1 = ind_str_special1 + 3
                        name = name[:ind_str_special1]
                    elif name.find('giảm') > 0:
                        ind_str_special1 = ind_str_special1 + 4
                        name = name[:ind_str_special1]
                    else:
                        name = name
            except:
                name = name
        try:
            partert = re.search('(rom)|(ram)|(\d+g)|(\d+ g)|(\(.*\))|(\,)|(mới)|(mỚi)|(điện thoại)', name)
            string = partert.group(0)
            ind_end = name.index(string)
            name = name[:ind_end]
        except:
            name = name
        
        name = re.sub('(\()|(\))|(\.)|(\-)|(\_)|(new)|(fullbox)|(bộ nhớ trong)|(kết nối)', ' ', name)
        name = re.sub('\s\s+', ' ', name)
        name = name.strip()
    return name

# name = get_pattern_name('Điện thoại iphone 11 64gb - mới 100% - nguyên seal - trắng', 'apple')
# print(name)

def pattern_product(brand, name, website, url, rom, ram, price):
    dict_product = {}
    name = get_pattern_name(name, brand)
    dict_product['website'] = website
    dict_product['pattern_name'] = name
    dict_product['url'] = url
    dict_product['rom'] = rom
    dict_product['ram'] = ram
    dict_product['price'] = price
    # print("dict_product", dict_product)
    return dict_product

def mapping(path):
    dict_data = {}
    dict_data['samsung'] = []
    dict_data['nokia'] = []
    dict_data['apple'] = []
    dict_data['oppo'] = []
    dict_data['xiaomi'] = []
    dict_data['lg'] = []
    dict_data['huawei'] = []
    dict_data['vivo'] = []
    data_lazada = read_file(path)
    for data in data_lazada:
        name = data['name']
        if name != None:
            name = name.lower()
            website = data['website']
            try:
                rom = data['product_specification']['bộ nhớ trong']
            except:
                rom = ''
            try:
                ram = data['product_specification']['ram']
            except:
                ram = ''
            url = data['url']
            price = data['price']
            brand = data['brand']

            # if brand == 'apple' and name.find('iphone') > 0:
            #     brand = 'iphone'

            dict_product = pattern_product(brand, name, website, url,rom, ram, price)
            
            if brand == 'samsung':
                dict_data['samsung'].append(dict_product)
            elif brand == 'nokia':
                dict_data['nokia'].append(dict_product)
            elif brand == 'apple':
                dict_data['apple'].append(dict_product)
            elif brand == 'oppo':
                dict_data['oppo'].append(dict_product)
            elif brand == 'xiaomi':
                dict_data['xiaomi'].append(dict_product)
            elif brand == 'vivo':
                dict_data['vivo'].append(dict_product)
            else:
                pass
    return dict_data
           
# pattern_lazada = mapping('aliscrapy/data_b4/tgdd.json')
# print(pattern_lazada)
# partern_tgdd = mapping('aliscrapy/data_b4/tgdd.json')
# print(partern_tgdd)

# def compare(dict_product_a, dict_product_b):
#     if dict_product_a['pattern_name'] == dict_product_b['pattern_name']:
#         if dict_product_a['rom'] == dict_product_b['rom']:
#             print("trung", dict_product_a, "\n", dict_product_b)
#         else:
#             print("cho no khac nhau")

# for product_a in pattern_lazada['samsung']:
#     for product_b in partern_tgdd['samsung']:
#         compare(product_a, product_b)

# def get_over_dict_manysource():
#     data_source = read_file(path)
#     for data in data_source:
#         name = data['name']
#         pattern_name = get_pattern_name


