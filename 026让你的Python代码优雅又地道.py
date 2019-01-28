"""
Raymond Hettinger在2013年美国PyCon演讲的笔记(视频, 幻灯片)
传授pythonic之道
"""



colors = ['red', 'green', 'blue', 'yellow']
names = ['raymond', 'rachel', 'matthew']
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

# 遍历一个集合
for color in colors:
   print(color)

# 反向遍历
for color in reversed(colors):
   print(color)

# 遍历一个集合及其下标
for i, color in enumerate(colors):
   print(i, '--->', color)

# 遍历两个集合
for name, color in zip(names, colors):
   print(name, '--->', color)

# 有序地遍历
# 正序
for color in sorted(colors):
   print(color)

# 倒序
for color in sorted(colors, reverse=True):
   print(color)

# 自定义排序顺序
"""
def compare_length(c1, c2):
   if len(c1) < len(c2): return -1
   if len(c1) > len(c2): return1
   return0

print(sorted(colors, cmp=compare_length))
"""
print(sorted(colors, key=len)) # 更好的选择

# 调用一个函数直到遇到标记值
"""
iter接受两个参数。第一个是你反复调用的函数，第二个是标记值。
优势在于iter的返回值是个迭代器，迭代器能用在各种地方，set，sorted，min，max，heapq，sum……
"""
# blocks = []
# for block in iter(partial(f.read, 32), ''):
#    blocks.append(block)

# 在循环内识别多个退出点 for-else 语法
"""
for执行完所有的循环后就会执行else。
且for循环中没有break
"""
def find(seq, target):
   for i, value in enumerate(seq):
       if value == target:
           break
   else:
       return -1
   return i

# 遍历字典的key
"""
需要修改字典的时候使用第二种方法
d.keys()把字典里所有的key都复制到一个列表里。然后你就可以修改字典了。

"""
for k in d:
   print(k)

for k in list(d.keys()):
   if k.startswith('r'):
       del d[k]

# 遍历一个字典的key和value
for k, v in d.items():
   print(k, '--->', v)

# 用key-value对构建字典
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(zip(names, colors))
# {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

# 用字典计数
colors = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}
for color in colors:
   d[color] = d.get(color, 0) + 1
# 稍微潮点的方法，但有些坑需要注意，适合熟练的老手。
from collections import defaultdict
d = defaultdict(int)
for color in colors:
   d[color] += 1

# 用字典分组 — 第I部分和第II部分
# 在这个例子，我们按name的长度分组
names = ['raymond', 'rachel', 'matthew', 'roger',
        'betty', 'melissa', 'judith', 'charlie']

from collections import defaultdict
d = defaultdict(list)
for name in names:
   key = len(name)
   d[key].append(name)

# 字典的popitem()是原子的吗？
"""
popitem是原子的，所以多线程的时候没必要用锁包着它
"""
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
while d:
   key, value = d.popitem()
   print(key, '-->', value)

# 连接字典
import os
import argparse
from collections import ChainMap
defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k: v for k, v in vars(namespace).items() if v}

d = ChainMap(command_line_args, os.environ, defaults)

# 用namedtuple提高多个返回值的可读性
# namedtuple是tuple的子类，所以仍适用正常的元组操作，但它更友好。
# TestResults = namedTuple('TestResults', ['failed', 'attempted'])

# unpack序列
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'
fname, lname, age, email = p

# 更新多个变量的状态
def fibonacci(n):
   x, y = 0, 1
   for i in range(n):
       print(x)
       x, y = y, x + y

# 同时状态更新
# x, y, dx, dy = (x + dx * t,
#                y + dy * t,
#                influence(m, x, y, dx, dy, partial='x'),
#                influence(m, x, y, dx, dy, partial='y'))

# 连接字符串
names = ['raymond', 'rachel', 'matthew', 'roger',
        'betty', 'melissa', 'judith', 'charlie']
print(', '.join(names))

# 更新序列
from collections import deque
names = ['raymond', 'rachel', 'matthew', 'roger',
        'betty', 'melissa', 'judith', 'charlie']
names = deque(names)
# 用deque更有效率
del names[0]
names.popleft()
names.appendleft('mark')

# 如何打开关闭文件
with open('data.txt') as f:
   data = f.read()

# 如何使用锁
# 创建锁
lock = threading.Lock()
with lock:
   print('Critical section 1')
   print('Critical section 2')

# 列表解析和生成器
print(sum(i**2for i in xrange(10)))
