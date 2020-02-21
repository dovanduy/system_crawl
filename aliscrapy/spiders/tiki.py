import time
import scrapy
from scrapy_splash import SplashRequest

from aliscrapy.items import Lazada

class AliscrapySpider(scrapy.Spider):
    name = "lazada"


    start_urls = [
        ('nokia', 'https://tiki.vn/dien-thoai-smartphone/c1795/nokia?src=mega-menu'),
        # ('xiaomi', 'https://tiki.vn/thuong-hieu/xiaomi.html?src=mega-menu'),
        # ('samsung', 'https://tiki.vn/dien-thoai-smartphone/c1795/samsung?src=mega-menu'),
        # ('apple', 'https://tiki.vn/dien-thoai-may-tinh-bang/c1789/apple?src=mega-menu'),
        # ('oppo', 'https://tiki.vn/dien-thoai-smartphone/c1795/oppo?src=mega-menu'),
    ]
    def start_requests(self):
        for _ in self.start_urls:
            yield SplashRequest(_[1], self.get_nextpage, args={'wait': 3}, meta={'brand':_[0]})
    
    def get_nextpage(self, response):
        brand = response.meta['brand']
        api_link = response.url + '?page={}'
        arr_page = response.xpath('.//ul[@class="ant-pagination "]//a[contains(@href, "/dien-thoai-di-dong/")]//text()').getall()
        num_page = int(arr_page[-2])
        for i in range(num_page + 1):
            link = api_link.format(i)
            yield SplashRequest(link, self.get_listproduct, args={'wait': 3}, meta={'brand':brand})

    def get_listproduct(self, response):
        brand = response.meta['brand']
        try:
            list_product = response.xpath('.//div[@class="c1_t2i"]//a[contains(@href, "//www.lazada.vn/products/")]/@href').getall()
        except Exception:
            return
        list_products = ['https:' + i for i in list_product]
        for _ in list_products:
            yield SplashRequest(_, self.get_info_product, args={'wait': 3}, meta={'brand':brand})

    def get_info_product(self, response):
        i = Lazada()
        i['brand'] = response.meta['brand']
        i['website'] = 'lazada'
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