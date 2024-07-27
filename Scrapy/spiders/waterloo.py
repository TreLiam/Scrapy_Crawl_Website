import scrapy
from Lab1.items import Lab1Item

class WaterlooSpider(scrapy.Spider):
    name = "waterloo"
    allowed_domains = ["uwaterloo.ca"]
    start_urls = ["http://uwaterloo.ca/"]

    def parse(self, response):
        News = response.xpath('//*[@id="site"]/div[1]/div[11]/div/div/div/div[1]/ul')
        NewsItem = Lab1Item()
        # NewsItem['date'] = News.xpath('.//*[@class="uw-news-date"]/text()').extract()
        # NewsItem['title'] = News.xpath('.//*[@class="uw-news-title"]/text()').extract()
        # NewsItem['content'] = News.xpath('.//*[@class="uw-news-teaser"]/text()').extract()

        NewsItem['site'] = News.xpath('.//@href').extract()
        for i in range(len(NewsItem['site'])):
            yield scrapy.Request(url = NewsItem['site'][i],callback=self.parseNews)

    def parseNews(self,response):
        WholeNews = response.xpath('//*[@id="site"]')
        WholeNewsItem =Lab1Item()
        WholeNewsItem['date'] = WholeNews.xpath('.//*[@class="article-date"]/text()').extract()
        WholeNewsItem['title'] = WholeNews.xpath('.//*[@class="article-info use"]/h1/text()').extract()
        WholeNewsItem['subtitle'] = WholeNews.xpath('.//*[@class="article-info use"]/p/text()').extract()
        WholeNewsItem['author'] = WholeNews.xpath('.//*[@class="author-position"]/text()').extract()
        WholeNewsItem['content'] = WholeNews.xpath('.//*[@class="field-item even"]/p/text()').extract()

        yield WholeNewsItem