class Matrix2D(object):
    """通用二维矩阵类"""

    def __init__(self, rows, cols):
        """初始化矩阵row行，col列"""
        self.grid = [[0] * cols for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_cell(self, r, c):
        """获取单元格（r,c）的值"""
        return self.grid[r][c]

    def set_cell(self, n, *args):
        """设置某个单元格的值"""
        for r, c in args:
            self.grid[r][c] = n

    def inc_cell(self, *args):
        """将单元格 +1"""
        for r, c in args:
            self.grid[r][c] += 1

    def set_all_cells(self, n=0):
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = n
