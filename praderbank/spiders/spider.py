import scrapy

from scrapy.loader import ItemLoader
from ..items import PraderbankItem
from itemloaders.processors import TakeFirst


class PraderbankSpider(scrapy.Spider):
	name = 'praderbank'
	start_urls = ['http://www.praderbank.com/it/ultime-news']

	def parse(self, response):
		post_links = response.xpath('//h2/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="col-md-12"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=PraderbankItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()
