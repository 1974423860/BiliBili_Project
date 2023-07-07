# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ScrapyAnimeItem(scrapy.Item):
    #构造一个数据域存放排名
    rank_detail = scrapy.Field()
    #构造一个数据域存放番剧名
    titles_detail = scrapy.Field()
    #构造一个数据域存放总播放量
    watch_detail = scrapy.Field()
    #构造一个数据域存放收藏量
    collection_detail = scrapy.Field()
    #构造一个数据域存放评分
    grade_detail = scrapy.Field()
    #构造一个数据域存放弹幕数
    danmaku_datail = scrapy.Field()
    