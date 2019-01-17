'''
1. 找到图片路径，获取所有图片真实URL
2. 设置文件名
3. 下载
'''

import requests
import re
import json

def getLOLImages():

    # 包含英雄名字和ID的js文件路径
    js_url = "http://lol.qq.com/biz/hero/champion.js"

    # 获取js文件内容
    js_content = requests.get(js_url).text

    # 截取需要的内容 .*? 代表所有内容
    req = '"keys":(.*?),"data"'
    # 取到的是列表，真正想要的是列表中的第一个元素
    js_want = re.findall(req, js_content)[0]

    # 转成字典形式
    js_dict = json.loads(js_want)

    # 获取图片的真实URL，并保存到列表中
    # http://ossweb-img.qq.com/images/lol/web201310/skin/big266000.jpg
    pic_url_list = []

    for hero_id in js_dict:
        for skin_id in range(20):
            skin_id = str(skin_id)
            if len(skin_id) == 1:
                num_str = '00' + skin_id
            elif len(skin_id) == 2:
                num_str = '0' + skin_id

            pic_url = "http://ossweb-img.qq.com/images/lol/web201310/skin/big" + hero_id + num_str +".jpg"

            pic_url_list.append(pic_url)

    # 设置文件名称
    path = "D://lol/"
    path_file_list = []
    for pic_name in js_dict.values():
        for skin_id in range(20):
            skin_id = str(skin_id)
            if len(skin_id) == 1:
                num_str = '00' + skin_id
            elif len(skin_id) == 2:
                num_str = '0' + skin_id

            path_file = path + pic_name + num_str + ".jpg"
            path_file_list.append(path_file)

    # 下载
    n = 0
    for dl_url in pic_url_list:
        # n += 1
        res = requests.get(dl_url)
        if res.status_code == 200:
            print("正在下载{}".format(path_file_list[n]))
            with open(path_file_list[n], "wb") as f:
                f.write(res.content)

        n += 1


if __name__ == '__main__':
    getLOLImages()
