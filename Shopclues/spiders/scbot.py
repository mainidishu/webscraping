# -*- coding: utf-8 -*-
import scrapy

class ShopcluesSpider(scrapy.Spider):
	name = 'scbot'
	allowed_domains = ['www.shopclues.com/mobiles-featured-store-4g-smartphone.html']
	start_urls = ['http://www.shopclues.com/mobiles-featured-store-4g-smartphone.html']
	custom_settings = {
		'FEED_URI' : 'tmp/SC.csv'
	}

	def parse(self, response):
		Discount = response.css('.prd_discount::text').extraxt()
		Price = response.css('.p_price::text').extract()
		Old_price = response.css('.old_prices::text').extract()

		for item in zip(Discount,Price,Old_price):
			scraped_info = {
				'Price' : item[0],
				'Discount' : item[1],
				'Old_Price' : item[2],
			}
			yield scraped_info

