#!/usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:BanShaoHuan
@file: 50 行代码教你爬取猫眼电影 TOP100 榜所有信息.py 
@time: 2018/04/24
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

import requests
import re
from requests.exceptions import RequestException
import json
from multiprocessing import Pool

headers = {'User-Agent': 'Mozilla/5.0'}


def get_one_page(url):
    '''
    构造HTML下载器
    :param url: 网页URL
    :return:    成功得到返回HTML文本，否则返回空
    '''
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    '''
    构造HTML解析器
    :param html:HTML文本
    :return: 包含所有信息的字典
    '''
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a' + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>' + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

def write_to_file(content):
    '''
    构造数据存储器
    :param content:写入文件的内容
    :return:None
    '''
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    '''
    主函数
    :param offset: 网页URL的偏移量
    :return: None
    '''
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    p = Pool()
    p.map(main, [i*10 for i in range(10)])