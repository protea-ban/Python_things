#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: 动态规划.py 
@time: 2018/05/11
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

def climbStairs(n):
    '''
    计算n级台阶的走法，每次可走1步或者2步
    :param n: 台阶总数
    :return: n级台阶的走法
    '''
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbStairs(n-1) + climbStairs(n-2)

def climbStairs2(n, value):
    if value.get(n) is not None:
        return value.get(n)
    else:
        if n < 1:
            value[n] = 0
        elif n == 1:
            value[n] = 1
        elif n == 2:
            value[n] = 2
        else:
            value[n] = climbStairs2(n - 1, value) + climbStairs2(n-2, value)

        return value[n]

