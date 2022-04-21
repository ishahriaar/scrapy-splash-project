import scrapy
from jxw_demo.items import JxwDemoItem

class JxwSpider(scrapy.Spider):
    name = 'jxw.spider'
    
    start_urls = ['https://cosmicray001.github.io/', 'https://ishahriar94.github.io/']
    
    def parse(self, response):
        item = JxwDemoItem()
        for result in response.css('div.portrait-title'):
            
            item['name'] = result.css('h2::text').get()
            item['link'] = result.css('a').attrib['href']
            yield item