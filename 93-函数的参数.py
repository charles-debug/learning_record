# 1 固定参数 1，2做加法

def add_num():
    result = 1+2
    print(result)

add_num()

# 2 不使用真实数据，而是使用形参a和b

def add_num1(a,b):
    result = a + b
    print(result)

add_num1(10,20)

# add_num1(100)  会报错，因为有两个形参