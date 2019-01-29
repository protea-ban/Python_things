# 1、冒泡排序
lis = [56,12,1,8,354,10,100,34,56,7,23,456,234,-58]

def sortport():
   for i in range(len(lis)-1):
       for j in range(len(lis)-1-i):
           if lis[j]>lis[j+1]:
               lis[j],lis[j+1] = lis[j+1],lis[j]
   return lis


# 2、计算 x 的 n 次方
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x

    return s


# 3、计算a*a + b*b + c*c + …
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n

    return sum


# 4、计算阶乘 n!
# 方法一
def fac():
   num = int(input("请输入一个数字："))
   factorial = 1
   #查看数字是负数，0或者正数
   if num<0:
       print("抱歉，负数没有阶乘")
   elif num == 0:
       print("0的阶乘为1")
   else:
       for i in range(1,num+1):
           factorial = factorial*i
       print("%d的阶乘为%d"%(num,factorial))

#方法二
def fac():
   num = int(input("请输入一个数字："))
   #查看数字是负数，0或者正数
   if num<0:
       print("抱歉，负数没有阶乘")
   elif num == 0:
       print("0的阶乘为1")
   else:
       print("%d的阶乘为%d"%(num,factorial(num)))

def factorial(n):
   result = n
   for i in range(1,n):
       result=result*i
   return result

#方法三
def fac():
   num = int(input("请输入一个数字："))
   #查看数字是负数，0或者正数
   if num<0:
       print("抱歉，负数没有阶乘")
   elif num == 0:
       print("0的阶乘为1")
   else:
       print("%d的阶乘为%d"%(num,fact(num)))

def fact(n):
   if n == 1:
       return1
   return n * fact(n - 1)


# 5、列出当前目录下的所有文件和目录名
import os

for d in os.listdir('.'):
   print(d)
# [d for d in os.listdir('.')] 列表推导式代码

# 6、把一个list中所有的字符串变成小写
L = ['Hello','World','IBM','Apple']

for s in L:
   s=s.lower()
   print(s)     #将list中每个字符串都变成小写，返回每个字符串

print(' '.join([s.lower() for s in L]))#整个list所有字符串都变成小写，返回一个list


# 7、输出某个路径下的所有文件和文件夹的路径
def print_dir():
 filepath = input("请输入一个路径：")
 if filepath == "":
   print("请输入正确的路径")
 else:
   for i in os.listdir(filepath):       #获取目录中的文件及子目录列表
     print(os.path.join(filepath,i))  #把路径组合起来


# 8、输出某个路径及其子目录下的所有文件路径
import os
def show_dir(filepath):
 for i in os.listdir(filepath):
   path = (os.path.join(filepath, i))
   print(path)
   if os.path.isdir(path):      #isdir()判断是否是目录
     show_dir(path)             #如果是目录，使用递归方法


# 9、输出某个路径及其子目录下所有以.html为后缀的文件
def print_dir(filepath):
 for i in os.listdir(filepath):
   path = os.path.join(filepath, i)
   if os.path.isdir(path):
     print_dir(path)
   if path.endswith(".html"):
     print(path)


# 10、把原字典的键值对颠倒并生产新的字典
dict1 = {"A":"a","B":"b","C":"c"}
dict2 = {y:x for x,y in dict1.items()}

# 11、打印九九乘法表
for i in range(1,10):
   for j in range(1,i+1):
       # 通过指定end参数的值，可以取消在末尾输出回车符，实现不换行。
       print('%d x %d = %d \t'%(j,i,i*j),end='')
   print()


# 12、替换列表中所有的3为3a
num = ["harden","lampard",3,34,45,56,76,87,78,45,3,3,3,87686,98,76]
print(num.count(3))
print(num.index(3))
for i in range(num.count(3)):      #获取3出现的次数
   ele_index = num.index(3)        #获取首次3出现的坐标
   num[ele_index]="3a"            #修改3为3a
print(num)


# 13、合并去重
list1 = [2,3,8,4,9,5,6]
list2 = [5,6,10,17,11,2]
list3 = list1 + list2
print(list3)              #不去重只进行两个列表的组合
print(set(list3))         #去重，类型为set需要转换成list
print(list(set(list3)))


# 14、随机生成验证码的两种方式(数字字母)
import random
list1=[]
for i in range(65,91):
   list1.append(chr(i))        #通过for循环遍历asii追加到空列表中
for j in range (97,123):
   list1.append(chr(j))
for k in range(48,58):
   list1.append(chr(k))
ma = random.sample(list1,6)
print(ma)                      #获取到的为列表
ma = ''.join(ma)              #将列表转化为字符串
print(ma)


# 15、判断字符串是否只由数字组成
#方法一
def is_number(s):
   try:
       float(s)
       return  True
   except ValueError:
       pass
   try:
       import unicodedata
       unicodedata.numeric(s)
       return  True
   except(TypeError,ValueError):
       pass
   return False
t="a12d3"
print(is_number(t))


#方法二
t = "q123"
print(t.isdigit())   #检测字符串是否只由数字组成


#方法三
t = "123"
print(t.isnumeric())   #检测字符串是否只由数字组成,这种方法是只针对unicode对象


# 16、判断闰年
#方法一
year = int(input("请输入一个年份："))
if (year % 4) == 0:
   if (year % 100) == 0:
       if(year % 400) ==0:
           print("{0}是闰年".format(year))       #整百年能被400整除的是闰年
       else:
           print("{0}不是闰年".format(year))
   else:
       print("{0}是闰年".format(year))           #非整百年能被4整除的为闰年
else:
   print("{0}不是闰年".format(year))


#方法二
year = int(input("请输入一个年份："))
if (year % 4) == 0 and (year % 100)!=0 or (year % 400) == 0:
   print("{0}是闰年".format(year))
else:
   print("{0}不是闰年".format(year))


#方法三
import calendar
year = int(input("请输入年份："))
check_year=calendar.isleap(year)
if check_year == True:
   print("%d是闰年"%year)
else:
   print("%d是平年"%year)


# 17、十进制转二进制、八进制、十六进制
# 获取输入十进制数
dec = int(input("输入数字："))

print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))


# 18、最大公约数
def hcf(x, y):
 """该函数返回两个数的最大公约数"""

 # 获取最小值
 if x > y:
   smaller = y
 else:
   smaller = x

 for i in range(1, smaller + 1):
   if ((x % i == 0) and (y % i == 0)):
     hcf = i

 return hcf

# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))



# 19、最小公倍数
# 定义函数
def lcm(x, y):

  #  获取最大的数
  if x > y:
      greater = x
  else:
      greater = y

  while(True):
      if((greater % x == 0) and (greater % y == 0)):
          lcm = greater
          break
      greater += 1

  return lcm

# 获取用户输入
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print( num1,"和", num2,"的最小公倍数为", lcm(num1, num2))


# 20、简单计算器
# 定义函数
def add(x, y):
   """相加"""
   return x + y

def subtract(x, y):
   """相减"""
   return x - y

def multiply(x, y):
   """相乘"""
   return x * y

def divide(x, y):
   """相除"""
   return x / y

# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

choice = input("输入你的选择(1/2/3/4):")

num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

if choice == '1':
   print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
   print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
   print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
   if num2 != 0:
       print(num1, "/", num2, "=", divide(num1, num2))
   else:
       print("分母不能为0")
else:
   print("非法输入")


# 21、生成日历
# 引入日历模块
import calendar

# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))

# 显示日历
print(calendar.month(yy, mm))


# 22、字符串判断
str = "runoob.com"
print(str.isalnum()) # 判断所有字符都是数字或者字母
print(str.isalpha()) # 判断所有字符都是字母
print(str.isdigit()) # 判断所有字符都是数字
print(str.islower()) # 判断所有字符都是小写
print(str.isupper()) # 判断所有字符都是大写
print(str.istitle()) # 判断所有单词都是首字母大写，像标题
print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r


# 23、字符串大小写转换
str = "https://www.cnblogs.com/banshaohuaun/"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写


# 24、获取昨天的日期
# 引入 datetime 模块
import datetime
defgetYesterday():
   today=datetime.date.today()
   oneday=datetime.timedelta(days=1)
   yesterday=today-oneday
   return yesterday

# 输出
print(getYesterday())




# if __name__ == '__main__':
#     filepath = "F:\WorkSpace\PycharmProjects\Python_things"
#     print_dir(filepath)
