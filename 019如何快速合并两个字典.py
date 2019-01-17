#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: 如何快速合并两个字典.py 
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
def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z

def merge_dicts(*dict_args):
    result = {}

    for dictionary in dict_args:
        result.update(dictionary)
    return result


if __name__ == '__main__':
    x = {'a': 1, 'b': 2}
    y = {'b': 10, 'c': 11}
    z = merge_two_dicts(x, y)
    print(z)

    w = merge_dicts(x, y, z)