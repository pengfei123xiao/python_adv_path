# spam模块，与Python文件在同路径下
print('from the spam.py')
money = 0


def read1():
    print('spam模块.read1：', money)


def read2():
    print('spam模块.read2')
    read1()


def change():
    global money
    money = 1  # 在模块中修改
