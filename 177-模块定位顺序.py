# 1.模块不要与已有模块重名
# import random
# s = random.randint(1,9)
# print(s)
# 若重名时，会优先调用当前目录下的模块

# 2.当时用from xx import 导入模块功能的时候，如果功能名字重复，使用的是后定义或后倒入的同名功能
# from time import sleep


# 定义函数sleep
#def sleep():
#   print('这是新定义的sleep')
#sleep(2)


def sleep():
    print('这是新定义的sleep')
from time import sleep


sleep(2)
