import scrapy


class HealthexpItem(scrapy.Item):
	title = scrapy.Field()
	link = scrapy.Field()
	category = scrapy.Field()
	favicon = scrapy.Field()