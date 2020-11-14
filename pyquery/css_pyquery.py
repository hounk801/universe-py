# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
# 根据css选择器获取内容  start
# doc = pq(html)
# print(doc('#container .list li'))
#
# print(type(doc('#container .list li')))
#
# for item in doc('.list li').items():
#     print(item.text())
# end

# 子节点  start
doc = pq(html)
print(type(doc))
items = doc('.list')
print(items)
print(items('li'))
print(type(items))
# find 的查找范围是节点的所有子孙节点
lis = items.find('li')
print(type(lis))
print(lis)

# 如果我们只想查找子节点，那可以用 children 方法：
children = doc('.list')
print('children:')
print(children)

grandson = doc('li')
print('grandson:')
print(grandson)
# end
