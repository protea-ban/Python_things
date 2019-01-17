import requests
from lxml import etree
import pandas as pd
import time
import random
from tqdm import tqdm

name, score, comment = [], [], []

def danye_crawl(page):
    url = 'https://movie.douban.com/subject/6390825/comments?start=%s&limit=20&sort=new_score&status=P&percent_type='%(page*20) # 要爬取的网页
    response = requests.get(url)
    response = etree.HTML(response.content.decode('utf-8')) # xpath用的是content，本句是固定用法
    if requests.get(url).status_code == 200:
        print('\n', '第%s页爬取成功'%(page))
    else:
        print('\n', '第%s页爬取失败'%(page))

    # 爬取页面当中的每条评论
    for i in range(1, 21):
        name_list = response.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/a'%(i))
        score_list = response.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/span[2]' % (i))
        comment_list = response.xpath('//*[@id="comments"]/div[%s]/div[2]/p' % (i))

        # 是以列表形式存储内容的，将内容取出来
        name_element = name_list[0].text
        score_element = score_list[0].attrib['class'][7]
        comment_elemnt = comment_list[0].text

        # 将每个评论加到列表中
        name.append(name_element)
        score.append(score_element)
        comment.append(comment_elemnt)


for i in tqdm(range(11)):   # tqdm交互好工具，显示程序运行进度
    danye_crawl(i)
    time.sleep(random.uniform(6, 9))

res = {'name':name, 'score':score, 'comment':comment}   # 将要存储的数据放到一个字典中
res = pd.DataFrame(res, columns=['name', 'score', 'comment'])   # 建立数据对象，列名要和字典中的关键词相同
res.to_csv("豆瓣.csv")

