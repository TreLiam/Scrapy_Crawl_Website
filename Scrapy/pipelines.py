# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Lab1Pipeline:
    def open_spider(self,spider):
        #打开文件
        self.file = open('news.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        #输入文件
        WholeContent = ''
        for i in range(len(item['content'])):
            WholeContent = WholeContent + item['content'][i] + '\n'
        PieceOfNews=item['date'][0]+'\n'+item['title'][0]+'\n'+item['subtitle'][0]+'\n'+item['author'][0]+'\n'+WholeContent + '\n'
        self.file.write(PieceOfNews + '\n')
        return item

    def close_spider(self,spider):
        #关闭文件
        self.file.close()