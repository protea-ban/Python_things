#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: Python中的闭包.py 
@time: 2018/04/13
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

# def make_printer(msg):
#    def printer():
#        print(msg)  # 夹带私货（外部变量）
#    return printer  # 返回的是函数，带私货的函数
# printer = make_printer('Foo!')
# printer()


def tag(tag_name):
    def add_tag(content):
        return "<{0}>{1}</{0}>".format(tag_name, content)

    return add_tag


content = 'Hello'

add_tag = tag('a')
print(add_tag(content))
# <a>Hello</a>

add_tag = tag('b')
print(add_tag(content))
# <b>Hello</b>


# how to define
def wrapper(func1):  # 必须接受一个且仅一个函数作为参数
   return func1  # 返回一个且仅一个callable对象，一般为函数

# how to use
def target_func(args):# 目标函数
   pass

# 调用方式一，直接包裹
result = wrapper(target_func)(args)

# 调用方式二，使用@语法，等同于方式一
@wrapper
def target_func(args):
   pass

result = target_func()


def html_tags(tag_name):
   def wrapper_(func):
       def wrapper(*args, **kwargs):
           content = func(*args, **kwargs)
           return "<{tag}>{content}</{tag}>".format(tag=tag_name, content=content)
       return wrapper
   return wrapper_

@html_tags('b')
def hello(name='Toby'):
   return'Hello {}!'.format(name)

# 不用@的写法如下
# hello = html_tag('b')(hello)
# html_tag('b') 是一个闭包，它接受一个函数，并返回一个函数

print(hello())  # <b>Hello Toby!</b>
print(hello('world'))  # <b>Hello world!</b>