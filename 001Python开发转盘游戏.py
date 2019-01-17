import tkinter
import threading
import time

root = tkinter.Tk()

# 设置窗口名字
root.title('香港男神')

# 设置窗口大小
root.minsize(300, 300)

# 按钮
btn1 = tkinter.Button(root, text='成龙', bg='red')
btn1.place(x=20, y=20, width=50, height=50)

btn2 = tkinter.Button(root, text='张国荣', bg='white')
btn2.place(x=90, y=20, width=50, height=50)

btn3 = tkinter.Button(root, text='郭富城', bg='white')
btn3.place(x=160, y=20, width=50, height=50)

btn4 = tkinter.Button(root, text='黎明', bg='white')
btn4.place(x=230, y=20, width=50, height=50)

btn5 = tkinter.Button(root, text='刘德华', bg='white')
btn5.place(x=230, y=90, width=50, height=50)

btn6 = tkinter.Button(root, text='梁朝伟', bg='white')
btn6.place(x=230, y=160, width=50, height=50)

btn7 = tkinter.Button(root, text='张学友', bg='white')
btn7.place(x=230, y=230, width=50, height=50)

btn8 = tkinter.Button(root, text='周润发', bg='white')
btn8.place(x=160, y=230, width=50, height=50)

btn9 = tkinter.Button(root, text='周星驰', bg='white')
btn9.place(x=90, y=230, width=50, height=50)

btn10 = tkinter.Button(root, text='谢霆锋', bg='white')
btn10.place(x=20, y=230, width=50, height=50)

btn11 = tkinter.Button(root, text='张家辉', bg='white')
btn11.place(x=20, y=160, width=50, height=50)

btn12 = tkinter.Button(root, text='古天乐', bg='white')
btn12.place(x=20, y=90, width=50, height=50)

# 按钮列表
herolist = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12]

# 开启的标志
isloop = False

# 停止的标志
isstop = False

# 停止时的ID
stopid = None

# 定义一个函数，实现循环功能
def round():

    # 设为全局变量，在此处做的改动可应用在其他函数中
    global isloop
    global stopid

    # 设置ID开始值
    i = 1

    # 已经在循环中
    if isloop is True:
        return

    if isinstance(stopid, int):
        i = stopid

    # 开始循环
    while True:

        # 睡眠
        time.sleep(0.03)

        # 设置每个按钮的背景色
        # 可以通过键值得方式设置按钮属性
        for e_btn in herolist:
            e_btn['bg'] = 'white'

        # 当前按钮背景色设置为红色
        herolist[i]['bg'] = 'red'

        i += 1
        print('当前i为', i)

        # 当i的值大于选项个数时，归零
        if i >= 12:
            i = 0

        # 当停止按钮被激活时，停止循环
        if isstop is True:
            isloop = False
            stopid = i
            break

# 定义停止函数，只是将停止标志设置为True
def my_stop():

    global isstop

    # 已经是停止状态时，不变
    if isstop is True:
        return

    isstop = True

# 定义开始函数
def newtask():

    global isloop
    global isstop

    isstop = False

    # 使用线程
    t = threading.Thread(target=round)

    t.start()

    # 开启循环标志
    isloop = True

# 设置开始按钮
btn_start = tkinter.Button(root, text='开始', command=newtask)
btn_start.place(x=90, y=125, width=50, height=50)

# 设置停止按钮
btn_stop = tkinter.Button(root, text='停止', command=my_stop)
btn_stop.place(x=160, y=125, width=50, height=50)

root.mainloop()
