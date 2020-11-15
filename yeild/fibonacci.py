#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'  module '

__author__ = 'hounaikuo'

li = []


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


for n in fibonacci(10):
    li.append(n)

print(li)
# while True:
#     try:
#         result = next(self.fibonacci(10))
#         print(result, end=" ")
#         # self.li.append(result)
#     except StopIteration:
#         sys.exit()

# print(self.li)
