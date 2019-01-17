#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaohuan
@file: 真-有趣的一行 Python 代码.py 
@time: 2018/06/02
@contact: banshaohuan@163.com
@software: PyCharm  
"""  

# 一行打印迷宫
# print(''.join(__import__('random').choice('\u2571\u2572') for i in range(50*24)))
# print(''.join(__import__('random').choice('/\\') for i in range(50*24)))

# 一行打印桃心
# print('\n'.join([''.join([('Lovepanpan'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

#一行输出九九乘法表
# print('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))


# 一行代码画Mandelbrot
print('\n'.join([''.join(['*'if abs((lambda a:lambda z,c,n:a(a,z,c,n))(lambda s,z,c,n:z if n==0else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))<2else' 'for x in range(-80,20)])for y in range(-20,20)]))