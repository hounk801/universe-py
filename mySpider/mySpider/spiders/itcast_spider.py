#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'  module '

__author__ = 'hounaikuo'

import sys
import scrapy as scrapy
from mySpider.items import ItcastItem


# 在mySpider下执行  scrapy crawl itcast
# 其中 itcast 为 ItcastSpider 类的 name 属性。


class ItcastSpider(scrapy.spiders.Spider):
    name = "itcast"
    # 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页
    allowed_domains = ["http://www.itcast.cn"]
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#ac"]

    # def parse(self, response):
    #     filename = "teacher.html"
    #     open(filename, 'wb').write(response.body)

    def parse(self, response):
        items = []
        for site in response.xpath('//div[@class="li_txt"]'):
            item = ItcastItem()
            print("---------------")
            teacher_name = site.xpath('h3/text()').extract()
            teacher_level = site.xpath('h4/text()').extract()
            teacher_info = site.xpath('p/text()').extract()

            unicode_teacher_name = teacher_name[0]
            unicode_teacher_level = teacher_level[0]
            unicode_teacher_info = teacher_info[0]
            print(unicode_teacher_name)
            print(unicode_teacher_level)
            print(unicode_teacher_info)

            item['name'] = unicode_teacher_name
            item['level'] = unicode_teacher_level
            item['info'] = unicode_teacher_info

            items.append(item)

            print("++++++++++++++")

        return items
