#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import urllib
from urllib import request


def load_page(url):
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    return html
