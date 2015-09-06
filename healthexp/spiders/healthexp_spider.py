from scrapy import Spider
from scrapy.selector import Selector

from healthexp.items import HealthexpItem

class Healthexp(Spider):
	name = "health"
	allowed_domains = ["http://www.health.com"]
	start_urls = [
				"http://www.health.com/health/cardio-workouts/",
				"http://www.health.com/health/must-eat-foods",
				"http://www.health.com/health/mind-and-body/",
				"http://www.health.com/health/lose-weight/",
				"http://www.health.com/health/get-stronger/",
				"http://www.health.com/health/yoga-pilates/"
	]
	

	def parse(self, response):
		articles = Selector(response).xpath('//ul[@class="tout"]/li')

		for article in articles:
			item = HealthexpItem()
			item['title'] = article.xpath('a/text()').extract()[0]
			item['link'] = article.xpath('a/@href').extract()[0]
			if response.url == "http://www.health.com/health/cardio-workouts/":
				item['category'] = 'cardio'
			elif response.url == "http://www.health.com/health/must-eat-foods":
				item['category'] = 'food'
			elif response.url == "http://www.health.com/health/mind-and-body/":
				item['category'] = 'general'
			elif response.url == "http://www.health.com/health/lose-weight/":
				item['category'] = 'weightloss'
			elif response.url == "http://www.health.com/health/get-stronger/":
				item['category'] = 'workout'
			elif response.url == "http://www.health.com/health/yoga-pilates/":
				item['category'] = 'yoga'

			yield item