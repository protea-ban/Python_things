#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: 设计模式之代理模式.py 
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

class GiveGift(object):
    def GiveDolls(self):
        pass

    def GiveFlowers(self):
        pass

    def GiveChocolate(self):
        pass

# 被追求者类
class SchoolGirl(object):
    def __init__(self, name):
        self.name = name


# 追求者类
class Pursuit(GiveGift):
    def __init__(self, Girl):
        self.Girl = Girl

    def GiveDolls(self):
        print(self.Girl.name, 'song ni yang wa wa')

    def GiveFlowers(self):
        print(self.Girl.name, 'songni hua')

    def GiveChocolate(self):
        print(self.Girl.name, 'song ni qiao ke li')

# 代理类
class Proxy(GiveGift):
    def __init__(self, Girl):
        self.proxy = Pursuit(Girl)

    def GiveDolls(self):
        self.proxy.GiveDolls()

    def GiveFlowers(self):
        self.proxy.GiveFlowers()

    def GiveChocolate(self):
        self.proxy.GiveChocolate()

if __name__ == '__main__':
    jiaojiao = SchoolGirl('jiaojiao')
    daili = Proxy(jiaojiao)
    daili.GiveDolls()
    daili.GiveFlowers()
    daili.GiveChocolate()