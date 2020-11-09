#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'  module '

__author__ = 'hounaikuo'

import re
from urllib import request
from urllib.error import HTTPError


class Spider:

    @staticmethod
    def load_page():
        url = 'http://www.haha56.net/xiaohua/neihan/index_7_1.html'
        user_agent = 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 63.0.3239.132 Safari / 537.36'
        headers = {'User-Agent': user_agent}

        req = request.Request(url, headers=headers)
        try:
            res = request.urlopen(req)

            html = res.read().decode('GBK')  # .encode('utf-8').decode('utf-8')

            # 用正则将html过滤 得到所有段子
            # 所有段子在<h3> —————————— <hr>之间

            #  这里需要注意一个是 re.S 是正则表达式中匹配的一个参数，
            #  如果 没有re.S 则是 只匹配一行 有没有符合规则的字符串，如果没有则下一行重新匹配
            #  如果 加上re.S 则是将 所有的字符串 将一个整体进行匹配
            pattern = re.compile(r'<h3>(.*?)<hr>', re.S)
            item_list = pattern.findall(html)

            return item_list
        except HTTPError:
            print('error')
            return []

    def do_work(self):
        item_list = self.load_page()
        my_file = open('./myStory.txt', 'a')
        for item in item_list:
            my_file.write(item.replace('</h3>', '').replace('<br />', '').replace('<p>', '').replace('</p>', '').replace(
                '&rdquo;', ''))
            my_file.write('\n'+'--------')
        my_file.close()


if __name__ == '__main__':
    mySpider = Spider()
    mySpider.do_work()
