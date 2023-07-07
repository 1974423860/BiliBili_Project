import json

import scrapy
import numpy as np
from ..items import ScrapyAnimeItem

class CommitsSpider(scrapy.Spider):
    name = 'AnimeSpider'
    allowed_domains = ['api.bilibili.com']
    start_urls = ['https://api.bilibili.com/pgc/web/rank/list?day=3&season_type=1']
    current_page = 1

    def parse(self, response):#下载器返回了相应文件，然后开始处理响应文件
        #print(response.body)
        #bilibiliitem=ScrapyAnimeItem()
        result = response.json().get('result').get('list')

        for data in result :
            # bilibiliitem['rank_detail'] = data.get('rank')
            # bilibiliitem['titles_detail'] = data.get('title')
            # bilibiliitem['watch_detail'] = data.get('stat').ger('view')
            rank_detail = data.get('rank')
            titles_detail = data.get('title')
            grade_detail = data.get('rating')
            result1 = data.get('stat')
            data1 = []
            for i in result1.values():
                data1.append(i)
                if len(data1) == 4:
                    danmaku_datail = data1[0]
                    collection_detail = data1[1]
                    watch_detail = data1[3]

            dict={
                'rank_detail':rank_detail,
                'titles_detail':titles_detail,
                'grade_detail':grade_detail,
                'danmaku_datail': danmaku_datail,
                'collection_detail': collection_detail,
                'watch_detail':watch_detail,
            }
            yield dict


