# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item,Field


class Lab1Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = Field()
    title = Field()
    subtitle = Field()
    content = Field()
    author = Field()


    site = Field()

    #Primary fields
    # title = Field()
    # price = Field()
    # description = Field()
    # address = Field()
    # image_URL = Field()
    # #
    # # #Calculated fields
    # images = Field()
    # location = Field()
    # #
    # # #Housekeeping fields
    # url = Field()
    # project = Field()
    # spider = Field()
    # server = Field()
    # date = Field()



