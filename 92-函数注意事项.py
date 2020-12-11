# 先使用函数，在判断注意事项
# 需求：一个函数，打印hello world
# info_print()  会报错

def info_print():
    print('hello world')

# 调用函数
info_print()
""" 
结论：
1.函数必须先定义，再调用，否则会报错
2.如果没有调用函数，函数里的代码就不会执行
3.函数执行流程：
当调用函数时，解释器回到定义函数的地方，执行下方缩进的代码。当这些代码执行完成，回到调用函数的地方，继续向下执行
定义函数的时候，函数体内部的缩进的代码并没有执行
"""