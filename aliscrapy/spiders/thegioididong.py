import time
import scrapy
from scrapy_splash import SplashRequest

from aliscrapy.items import TheGioiDiDong

class AliscrapySpider(scrapy.Spider):
    name = "thegioididong"
    custom_settings = {
        "DOWNLOAD_DELAY": 5,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 2
    }

    count_page = 0
    start_urls = [
        ('apple', 'https://www.thegioididong.com/dtdd-apple-iphone#i:1'),
        ('xiaomi', 'https://www.thegioididong.com/dtdd-xiaomi#i:1'),
        ('vivo', 'https://www.thegioididong.com/dtdd-vivo#i:1'),
        # ('realme', 'https://www.thegioididong.com/dtdd-realme#i:1'),
        # ('vsmart', 'https://www.thegioididong.com/dtdd-vsmart#i:1'),
        ('huawei', 'https://www.thegioididong.com/dtdd-huawei#i:1'),
        ('nokia', 'https://www.thegioididong.com/dtdd-nokia#i:1'),
        # ('itel', 'https://www.thegioididong.com/dtdd-itel#i:1'),
        # ('blackberry', 'https://www.thegioididong.com/dtdd-blackberry#i:1')
        ('samsung', 'https://www.thegioididong.com/dtdd-samsung#i:1')
        # ('samsung', 'https://www.thegioididong.com/dtdd/samsung-galaxy-a51'),
        # 'https://www.thegioididong.com/dtdd#i:5'
        # 'https://www.thegioididong.com/dtdd',
        # 'https://www.thegioididong.com/dtdd#i:{}'
    ]
    def start_requests(self):
        for _ in self.start_urls:
            yield SplashRequest(_[1], self.get_listproduct, args={'wait': 3}, meta={'brand':_[0]})
        
    def get_listproduct(self, response):
        brand = response.meta['brand']
        products = response.xpath('//ul[@class="homeproduct filter-cate "]//li//a[contains(@href, "/dtdd/")]/@href').getall()
        # print(products)
        list_products = ['https://www.thegioididong.com' + i for i in products]
        for link in list_products:
            yield SplashRequest(link, self.check_product, args={'wait': 3}, meta={'brand':brand})
            
    # có sản phẩm có được lồng bởi 2 sp 
    def check_product(self, response):
        # print("hha", response.url)
        brand = response.meta['brand']
        other_product = response.xpath('//div[@class="memory memory2 "]//a[contains(@href, "/dtdd/")]/@href').getall()
        if len(other_product) > 0:
            for link in other_product:
                link = 'https://www.thegioididong.com' + link
                yield scrapy.Request(link, self.get_detail, meta={'brand':brand})
                # yield SplashRequest(link, self.get_detail, args={'wait': 3}, meta={'brand':brand})
                
        else:
            link = response.url
            yield scrapy.Request(link, self.get_detail, meta={'brand':brand})
            # yield SplashRequest(response.url, self.get_detail, args={'wait': 3}, meta={'brand':brand})

    def get_detail(self, response):
        print("rooot", response.url)
        item = TheGioiDiDong()
        item['brand'] = response.meta['brand']
        item['website'] = 'thegioididong'
        name = response.xpath('.//div[@class="rowtop"]//h1//text()').extract_first()
        url = response.url
        price = response.xpath('.//div[@class="area_price"]/strong//text()').extract_first()
        score = response.xpath('.//div[@class="lcrt "]/b//text()').extract_first()
        specification = response.xpath('.//ul[@class="parameter "]/li')
        images = response.xpath('.//div[@class="owl-wrapper"]//img[contains(@src, "//cdn.tgdd.vn/Products/Images")]/@src').getall()
        images = ['https:' + i for i in images]
        list_images = ';'.join(images)
        big_image = response.xpath('.//aside[@class="picture"]//img[contains(@src, "https://cdn.tgdd.vn/Products/Images")]/@src').extract_first()
        # # print(score)
        # # images = response.xpath('.//div[@class="fs-dticolor fs-dticolor-img"]').extract()
        # # print(images, "\n", big_image, "\n", "-----------------")
        product_specification = {}
        for _ in specification:
            label = _.xpath('./span//text()').extract_first()
            value = _.xpath('./div//text()').extract_first()
            product_specification[label] = value
            # print("---", label, ":",  value)
        
        item['name'] = name
        item['url'] = url
        item['price'] = price
        item['score'] = score
        item['images'] = list_images
        item['big_image'] = big_image
        item['product_specification'] = product_specification
        # print(item)
        yield item

        # other_product = response.xpath('//aside[@class="price_sale"]//a[contains(@href, "/dtdd/")]/@href').getall()
        # if len(other_product) <= 0:
        #     price = response.xpath('.//div[@class="area_price"]/strong//text()').extract_first()
        # else:
        #     for link in other_product:
        #         link = 'https://www.thegioididong.com/' + link
        #         yield SplashRequest(link, self.get_detail, args={'wait': 3})