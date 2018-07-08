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
		price = response.css('.p_price::text').extract()
		

		for item in zip(price):
			scraped_info = {
				'price' : item[0],
			}
			yield scraped_info

