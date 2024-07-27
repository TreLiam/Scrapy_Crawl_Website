from scrapy import cmdline
FEED_EXPORT_ENCODING='utf-8'

cmdline.execute('scrapy crawl waterloo'.split())