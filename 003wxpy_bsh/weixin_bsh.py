from wxpy import *
import re
# 初始化机器人，扫码登录
bot = Bot()

# 获取所有好友
my_friends = bot.friends()
# 使用一个字典统计好友男性和女性的数量
sex_dict = {'male':0, 'female':0}

# for friend in my_friends:
#     # 统计性别
#     if friend.sex == 1:
#         sex_dict['male'] += 1
#     elif friend.sex == 2:
#         sex_dict['female'] += 1

# print(sex_dict)
# print(type(my_friends))

# 使用一个字典统计各省好友数量
# province_dict = {'北京': 0, '上海': 0, '天津': 0, '重庆': 0,
#    '河北': 0, '山西': 0, '吉林': 0, '辽宁': 0, '黑龙江': 0,
#    '陕西': 0, '甘肃': 0, '青海': 0, '山东': 0, '福建': 0,
#    '浙江': 0, '台湾': 0, '河南': 0, '湖北': 0, '湖南': 0,
#    '江西': 0, '江苏': 0, '安徽': 0, '广东': 0, '海南': 0,
#    '四川': 0, '贵州': 0, '云南': 0,
#    '内蒙古': 0, '新疆': 0, '宁夏': 0, '广西': 0, '西藏': 0,
#    '香港': 0, '澳门': 0}
#
# # 统计省份
# for friend in my_friends:
#     if friend.province in province_dict.keys():
#         province_dict[friend.province] += 1
#
# # 为了方便数据的呈现，生成JSON Array格式数据
# data = []
# for key, value in province_dict.items():
#     data.append({'name':key, 'value':value})
#
# print(data)

def write_txt_file(path, txt):
    '''
    写入txt文本
    :param path:
    :param txt:
    :return:
    '''
    # utf-8-sig
    with open(path, 'a', encoding='utf-8-sig', newline='') as f:
        f.write(txt)

# 统计签名
for friend in my_friends:
    # 对数据进行清洗，将标点符号等对词频统计造成影响的因素剔除
    pattern = re.compile(r'[一-龥]+')
    filterdata = re.findall(pattern, friend.signature)
    write_txt_file('signature.txt', ''.join(filterdata))