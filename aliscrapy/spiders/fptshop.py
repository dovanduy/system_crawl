import time
import scrapy
from scrapy_splash import SplashRequest

from aliscrapy.items import FPTSoft

class AliscrapySpider(scrapy.Spider):
    name = "fptshop"


    start_urls = [
        ('apple', 'https://fptshop.com.vn/dien-thoai/apple-iphone?sort=ban-chay-nhat'),
        ('samsung', 'https://fptshop.com.vn/dien-thoai/samsung?sort=ban-chay-nhat'),
        ('oppo', 'https://fptshop.com.vn/dien-thoai/oppo?sort=ban-chay-nhat'),
        ('xiaomi', 'https://fptshop.com.vn/dien-thoai/xiaomi?sort=ban-chay-nhat'),
        ('nokia', 'https://fptshop.com.vn/dien-thoai/nokia?sort=ban-chay-nhat'),
        # 'https://fptshop.com.vn/dien-thoai/vsmart-star-2gb-16gb'
        # 'https://fptshop.com.vn/dien-thoai?sort=ban-chay-nhat',
        # 'https://fptshop.com.vn/dien-thoai?sort=ban-chay-nhat&trang={}'
    ]
    def start_requests(self):
        for _ in self.start_urls:
            yield scrapy.Request(_[1], self.get_nextpage, meta={'brand':_[0]})
        # yield SplashRequest(self.start_urls[0], self.get_listcategory, args={'wait': 3})

    def get_nextpage(self, response):
        brand = response.meta['brand']
        api_url = response.url + '&trang={}'
        arr_list = response.xpath('.//ul[@class="clearfix"]/li//text()').extract()
        num_page = int(arr_list[-1])
        if num_page == 1:
            yield scrapy.Request(response.url, self.get_products, meta={'brand':brand})
        else:
            for page in range(num_page+1)[1:]:
                link_page = api_url.format(page)
                yield scrapy.Request(link_page, self.get_products, meta={'brand':brand})

    def get_products(self, response):
        brand = response.meta['brand']
        list_category = response.xpath('.//div[@class="fs-carow clearfix fs-row4phone viewgrid"]/div[@class="fs-lpil"]/a[contains(@href, "/dien-thoai/")]/@href').getall()
        for _ in list_category:
            link_product = 'https://fptshop.com.vn' + _
            yield SplashRequest(link_product, self.get_detail, args={'wait': 3}, meta={'brand':brand})
    
    def get_detail(self, response):
        item = FPTSoft()
        item['brand'] = response.meta['brand']
        item['website'] = 'fptshop'
        name = response.xpath('.//h1[@class="fs-dttname"]//text()').extract_first()
        if name != None:
            price = response.xpath('.//p[@class="fs-dtprice "]//text()').extract_first()
            score = response.xpath('.//div[@class="fs-dtrt-col fs-dtrt-c1"]/h5//text()').extract_first()
            # specification = response.xpath('.//div[@class="fs-dttskt"]/ul[@class="fs-dttsktul"]/li')
            specification = response.xpath('.//div[@class="fs-tsright"]/ul/li')
            images = response.xpath('.//div[@class="fs-dticolor fs-dticolor-img"]//img[contains(@src, "https://images.fpt.shop/unsafe/fit-in/")]/@src').getall()
            list_images = ';'.join(images)
            big_image = response.xpath('.//div[@class="easyzoom"]//img[contains(@src, "https://images.fpt.shop/unsafe/fit-in/")]/@src').extract_first()
            # print(score)
            # images = response.xpath('.//div[@class="fs-dticolor fs-dticolor-img"]').extract()
            # print(images, "\n", big_image, "\n", "-----------------")
            product_specification = {}
            for _ in specification:
                label = _.xpath('./label//text()').extract_first()
                value = _.xpath('./span//text()').extract_first()
                product_specification[label] = value
                # print("---", label, ":",  value)
            
            item['name'] = name
            item['url'] = response.url
            item['price'] = price
            item['score'] = score
            item['images'] = list_images
            item['big_image'] = big_image
            item['product_specification'] = product_specification
            yield item