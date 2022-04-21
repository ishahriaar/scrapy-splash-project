from scrapy.item import Item, Field



class JxwDemoItem(Item):
    name = Field()
    link = Field()
