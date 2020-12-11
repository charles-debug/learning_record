# help(len)  help函数的作用就是查看函数的说明文档

def sum_num(a,b):
    """ 求和函数 """
    return a + b


help(sum_num)


# 说明文档的高级使用
def sum_num1(a,b):
    """
    求和函数sum_num
    param a:
    param b:
    return:
    """
    return a + b

help(sum_num1)