#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'  module '

__author__ = 'hounaikuo'


def write_file(file_name, text):
    f = open(file_name, 'w+', encoding='UTF-8')
    f.write(text)
    f.close()
