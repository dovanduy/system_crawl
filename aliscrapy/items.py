# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AliscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WebanalysisItem(scrapy.Item):
	website = scrapy.Field()
	date = scrapy.Field()
	product_id = scrapy.Field()
	title = scrapy.Field()
	original_price = scrapy.Field()
	current_price = scrapy.Field()
	detail_info = scrapy.Field()
	rating = scrapy.Field()
	number_of_rating = scrapy.Field()
	number_of_comment = scrapy.Field()
	list_of_comment = scrapy.Field()
	description = scrapy.Field()
	url_product = scrapy.Field()
	category = scrapy.Field()

class StackItem(scrapy.Item):
	url = scrapy.Field()
	title = scrapy.Field()

class Lazada(scrapy.Item):
	brand = scrapy.Field()
	website = scrapy.Field()
	name = scrapy.Field()
	url = scrapy.Field()
	price = scrapy.Field()
	score = scrapy.Field()
	images = scrapy.Field()
	big_image = scrapy.Field()
	product_specification = scrapy.Field()

class Shopee(scrapy.Item):
	link_category = scrapy.Field()
	name_category = scrapy.Field()
	url_product = scrapy.Field()
	website = scrapy.Field()
	date = scrapy.Field()
	name_product = scrapy.Field()
	price_discount = scrapy.Field()
	price_sell = scrapy.Field()
	score = scrapy.Field()
	image = scrapy.Field()
	number_evaluated = scrapy.Field()

class FPTSoft(scrapy.Item):
	brand = scrapy.Field()
	website = scrapy.Field()
	name = scrapy.Field()
	url = scrapy.Field()
	price = scrapy.Field()
	score = scrapy.Field()
	images = scrapy.Field()
	big_image = scrapy.Field()
	product_specification = scrapy.Field()

class TheGioiDiDong(scrapy.Item):
	brand = scrapy.Field()
	website = scrapy.Field()
	name = scrapy.Field()
	url = scrapy.Field()
	price = scrapy.Field()
	score = scrapy.Field()
	images = scrapy.Field()
	big_image = scrapy.Field()
	product_specification = scrapy.Field()