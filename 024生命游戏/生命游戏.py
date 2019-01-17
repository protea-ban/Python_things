"""
生命游戏

对于网格中的每个位置，计算有多少个邻接位置中有活细胞，包括对角邻接位置，
因此一个方块的周围最多有八个活细胞(数值为1的方块)，最少为零，规则就是，
如果这个方块周围的活细胞数等于三，就繁殖，也就是值变为1，
如果这个方块周围的活细胞数少于两个或者大雨三个，则该方块中细胞死亡，值变为0。
"""
from lifemat import Matrix2D

rows = 5
cols = 5
# 存储图符号的二维数组
life_mat = Matrix2D(rows, cols)
# 存储具体数据的二维数组
nc_mat = Matrix2D(rows, cols)
# 初始化
life_mat.set_cell(1, (1, 3), (2, 1), (2, 3), (3, 2), (3, 3))
# 创建边界字符串
border_str = '_' * cols

def get_mat_str(a_mat):
    """处理打印字符串"""
    disp_str = ''
    for i in range(rows):
        lst = [get_chr(a_mat, i, j) for j in range(cols)]
        disp_str += ''.join(lst) + '\n'

    return disp_str

def get_chr(a_mat, r, c):
    """设置图符号"""
    return '1' if a_mat.get_cell(r, c) > 0 else '0'

def do_generation():
    """打印当前状态并生成下一个状态"""
    # 打印当前生命矩阵状态
    print(border_str + '\n' + get_mat_str(life_mat))

    # 数据设为0
    nc_mat.set_all_cells(0)

    # 根据符号矩阵life_mat来给nc_mat赋值
    for i in range(rows):
        for j in range(cols):
            if life_mat.get_cell(i, j):
                # 环绕图像，是有限的二维矩阵数组变成没有边界的生命游戏
                im = (i - 1) % rows
                ip = (i + 1) % rows
                jm = (j - 1) % cols
                jp = (j - 1) % cols

                # 设置数据量为1，表示有活细胞
                nc_mat.inc_cell((im, jm), (im, j), (im, jp), (i, jm),
                                 (i, jp), (ip, jm), (ip, j), (ip, jp))
    # 根据邻居数量举着按规则生成下一代
    for i in range(rows):
        for j in range(cols):
            n = nc_mat.get_cell(i, j)
            if n < 2 or n > 3:  # 死亡现象
                life_mat.set_cell(0, (i, j))
            elif n == 3:    # 繁殖现象
                life_mat.set_cell(1, (i, j))


import time
for i in range(1000):
    do_generation()
    time.sleep(1)
