import scrapy
from jxw_demo.items import JxwDemoItem
import re

class JxwSpider(scrapy.Spider):
    name = 'jxw.spider'
    
    start_urls = ['https://cosmicray001.github.io/']
    
    def parse(self, response):
        item = JxwDemoItem()
        # urls = response.css('a::attr(href)').getall()  
            
        # for res in urls:
        #     if res.startswith('http://') or res.startswith('https://'):
        #         item['link'] = res
        #         yield item
        
        alltext = response.css('::text').getall()
        myreg = '^[a-zA-Z]+\s*[a-zA-Z]*\s*[a-zA-Z]*$'
        for res in alltext:
            if re.search(myreg, res):
                item['text'] = res
                yield item
        
        
        
                
                
         