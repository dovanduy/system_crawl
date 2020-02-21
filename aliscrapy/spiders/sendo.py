import time
import scrapy
import re
from scrapy_splash import SplashRequest

from aliscrapy.items import Lazada

class AliscrapySpider(scrapy.Spider):
    name = "sendo"


    start_urls = [
        'https://www.sendo.vn/thiet-bi-di-dong?p=3&q=samsung'
        # ('nokia', 'https://www.sendo.vn/thiet-bi-di-dong?q=nokia'),
        # ('xiaomi', 'https://www.sendo.vn/thiet-bi-di-dong?q=xiaomi'),
        # ('samsung', 'https://www.sendo.vn/thiet-bi-di-dong?q=samsung'),
        # ('oppo', 'https://www.sendo.vn/thiet-bi-di-dong?q=oppo'),
        # ('apple', 'https://www.sendo.vn/thiet-bi-di-dong?q=apple'),
        # ('zip', 'https://www.lazada.vn/dien-thoai-di-dong/zip-mobile/?spm=a2o4n.searchlistcategory.card.7.1f492590106FR9&from=onesearch_category_4518'),
        # ('lg', 'https://www.sendo.vn/thiet-bi-di-dong?q=lg'),
        # ('vivo', 'https://www.sendo.vn/thiet-bi-di-dong?q=vivo'),
        # ('vsmart', 'https://www.sendo.vn/thiet-bi-di-dong?q=vsmart'),
        # ('itel', 'https://www.sendo.vn/thiet-bi-di-dong?q=itel'),
        # 'https://www.lazada.vn/dien-thoai-di-dong/?spm=a2o4n.home.cate_1.1.6e096afe2JiBA2'
        # 'https://www.lazada.vn/products/dien-thoai-vsmart-bee-1g16g-2sim-2-song-4g-moi-100-bao-hanh-12-thang-the-gioi-tao-khuyet-i436826234-s783052400.html?spm=a2o4n.searchlistcategory.list.160.3a0825900Xjsmn&search=1'
    ]
    def start_requests(self):
        yield SplashRequest(self.start_urls[0], self.get_listproduct, args={'wait': 3}, meta={'brand':'samsung'})
        # for _ in self.start_urls:
        #     yield SplashRequest(_[1], self.get_nextpage, args={'wait': 3}, meta={'brand':_[0]})
    
    def get_nextpage(self, response):
        brand = response.meta['brand']
        arr_root = response.url.split('?')
        print(arr_root)
        api_link = arr_root[0] + '?p={}' + arr_root[1]
        try:
            str_page = response.xpath('.//div[@class="paginationWrapper_lnTQ"]/span[@class="text_R-cM"]//text()').extract_first()
            num_page = re.sub('([^0-9])', '', str_page)
            num_page = int(num_page[1:])
            for i in range(num_page + 1)[:1]:
                link = api_link.format(i)
                print(link)
                yield SplashRequest(link, self.get_listproduct, args={'wait': 3}, meta={'brand':brand})
        except:
            print("error link", response.url)


    def get_listproduct(self, response):
        print("root", response.url)
        brand = response.meta['brand']
        try:
            # list_product = response.xpath('.//div[@class="ReactVirtualized__Grid__innerScrollContainer"]//div[@class="list_1VuX grid2_1GZq"]//a[@class="item_3KnU"]/@href').extract()
            list_product = response.xpath('.//div[@class="ReactVirtualized__Grid__innerScrollContainer"]//div[@class="list_1VuX grid2_1GZq"]').extract()
            print(list_product)
        except Exception:
            return
        # list_products = ['https:' + i for i in list_product]
        # for _ in list_products:
        #     yield SplashRequest(_, self.get_info_product, args={'wait': 3}, meta={'brand':brand})

    def get_info_product(self, response):
        i = Lazada()
        i['brand'] = response.meta['brand']
        try:
            name = response.xpath('//span[@class="pdp-mod-product-badge-title"]//text()').extract()
            name = ' '.join(name)
            i['name'] = name
        except Exception:
            i['name'] = ""
        try:
            i['url'] = response.url
            # i['website'] = 'Lazada'
            # i['date'] = time.time()
        except Exception:
            i['url'] = ""
        
        # try:
        #     i['price_discount'] = response.xpath('//span[@class=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl"]//text()').extract_first()
        # except Exception:
        #     i['price_discount'] = ""
        try:
            i['price'] = response.xpath('//span[@class=" pdp-price pdp-price_type_deleted pdp-price_color_lightgray pdp-price_size_xs"]//text()').extract_first()
        except Exception:
            i['price'] = ""
        try:
            i['score'] = response.xpath('//span[@class="score-average"]//text()').extract_first()
        except Exception:
            i['score'] = ""

        try:
            i['big_image'] = response.xpath('//img[@class="pdp-mod-common-image gallery-preview-panel__image"]/@src').extract_first()
        except Exception:
            i['big_image'] = ""

        try:
            images = response.xpath('//div[@class="next-slick-list"]//img[contains(@src, "//vn-test-11.slatic.net/p/")]/@src').getall()
            images = ['https:' + i for i in images]
            list_images = ';'.join(images)
            i['images'] = list_images
        except Exception:
            i['images'] = ""
        product_specification = {}
        try:
            specification = response.xpath('.//div[@class="html-content pdp-product-highlights"]/ul/li')
            for _ in specification:
                value = _.xpath('.//text()').extract_first()
                # print('value', value)
                if ':' in value:
                    split_value = value.split(':')
                    product_specification[split_value[0]] = split_value[1]
            i['product_specification'] = product_specification
        except Exception:
            i['product_specification'] = ""
        yield i