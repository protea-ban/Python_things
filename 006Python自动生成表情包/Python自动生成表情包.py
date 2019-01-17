#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: Python自动生成表情包.py 
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

from PIL import Image,ImageDraw,ImageFont

img = Image.open('hah.png')
draw = ImageDraw.Draw(img)
ttfont = ImageFont.truetype('simhei.ttf', 24)
draw.text((32,190), '我的内心毫无波动', fill=(0, 0, 0), font=ttfont)
draw.text((64,220), '甚至还想笑', fill=(0, 0, 0), font=ttfont)
# img.show()
img.save('nice.png')