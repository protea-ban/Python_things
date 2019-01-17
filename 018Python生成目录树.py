#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: Python生成目录树.py 
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

from pathlib import Path
import sys

# p = Path('E:\老男孩Python全栈3期\老男孩全栈3课件\day22\day22课堂代码\day22')
# pit = p.iterdir()
# print(p.is_file())
# print(p.is_dir())

tree_str = ''

def generate_tree(pathname, n=0):
    global tree_str
    if pathname.is_file():
        tree_str += '  |' * n + '-' * 4 + pathname.name + '\n'
    elif pathname.is_dir():
        tree_str += '  |' * n + '-' * 4 + \
            str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1)

def save_file(tree, filename = 'tree.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(tree)

if __name__ == '__main__':
    # 命令参数个数为2并且目录存在
    if len(sys.argv) == 2 and Path(sys.argv[1]).exists():
        generate_tree(Path(sys.argv[1]), 0)
    if len(sys.argv) == 3 and Path(sys.argv[1]).exists():
        generate_tree(Path(sys.argv[1]), 0)
        save_file(tree_str, sys.argv[2])
    else:
        generate_tree(Path.cwd(), 0)
    print(tree_str)