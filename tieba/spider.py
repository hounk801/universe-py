#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'  module '

__author__ = 'hounaikuo'

from tieba.load import load_page
from tieba.write import write_file


def tieba_spider(url, begin_page, end_page):
    for i in range(begin_page, end_page):
        pn = 50 * (i - 1)
        html = load_page(url + str(pn))
        file_name = str(i) + '.html'
        write_file(file_name, html)
