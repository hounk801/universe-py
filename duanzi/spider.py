#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'  module '

__author__ = 'hounaikuo'

from urllib import request


class Spider:
    def load_page(self, page):
        url = 'http://www.haha56.net/xiaohua/neihan/index_7_' + str(page) + '.html'
        headers = {}

        req = request.Request(url)
        res = request.urlopen(req)
        html = res.read().decode('gbk')

        return html


if __name__ == '__main__':
    mySpider = Spider()
    the_page = mySpider.load_page(1)

    print(the_page)
