#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: 50道python笔试面试真题大集合.py 
@time: 2018/05/10
@contact: banshaohuan@163.com
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃  永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""  

# li = [1, 2, 3, 4, 5]
# def fn(x):
#     return x**2
#
# res = map(fn, li)
# res = [i for i in res if i > 10]
# print(res)

# import random
# import numpy as np
# result = random.randint(10, 20)
# res = np.random.randn(5)
# ret = random.random()
# print("正整数", result)
# print("5个 随机小数", res)
# print("0-1随机小数", ret)


import re
def match_case(word):
   def replace(m):
       print(m)
       exit()
       text = m.group()
       if text.isupper():
           return word.upper()
       elif text.islower():
           return word.lower()
       elif text[0].isupper():
           return word.capitalize()
       else:
           return word
   return replace
if __name__ == '__main__':
    s = "LOVE PYTHON, love python, Love Python"
    print(re.sub('python', match_case('money'), s, flags=re.IGNORECASE))