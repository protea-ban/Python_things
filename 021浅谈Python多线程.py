#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: 浅谈Python多线程.py 
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
import threading
def func(n):
    while n > 0:
        print("当前线程数：", threading.active_count())
        n -= 1

for x in range(5):
    t = threading.Thread(target=func, args=(2, ))
    t.start()

print("主线程：", threading.current_thread().name)