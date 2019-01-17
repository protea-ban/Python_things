#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: 闭包面试题.py 
@time: 2018/05/05
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

from functools import partial
from operator import mul

def testFun():
    temp = [lambda x : i * x for i in range(4)]
    return temp

def testFun():
    temp = [lambda x, i = i: i*x for i in range(4)]
    return temp


def testFun():
    return [partial(mul, i) for i in range(4)]

def testFun():
    return (lambda x, i=i:i*x for i in range(4))

def testFun():
    for i in range(4):
        yield lambda x:i*x

if __name__ == '__main__':
    for everyLambda in testFun():
        print(everyLambda(2))