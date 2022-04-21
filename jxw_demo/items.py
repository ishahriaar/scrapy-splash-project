from scrapy.item import Item, Field



class JxwDemoItem(Item):
    text = Field()
    link = Field()
