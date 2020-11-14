#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'  module '

__author__ = 'hounaikuo'

from tieba.load import load_page
from tieba.write import write_file

if __name__ == '__main__':
    baseurl = 'https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn='
    begin_page = int(input('please input start page:'))
    end_page = int(input('please input end page:'))

    for i in range(begin_page, end_page):
        pn = 50 * (i - 1)
        html = load_page(baseurl + str(pn))
        file_name = str(i) + '.html'
        write_file(file_name, html)
