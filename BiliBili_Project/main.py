#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 00:21:51 2023

@author: ciao
"""

from scrapy.cmdline import execute

# 执行刚生成的 douban_spider 爬虫
#execute("scrapy crawl spider1 -s LOG_FILE=debug.log".split())
execute("scrapy crawl AnimeSpider".split())
#execute("scrapy crawl AnimeSpider -s LOG_FILE=debug.log".split())