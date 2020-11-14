#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from urllib import request


def load_page(url):
    req = request.Request(url)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    return html
