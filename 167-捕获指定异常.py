# 需求：打印输出num, 捕获指定异常NameError，如果捕获到这个异常类型则打印，否则不执行

try:
    print(num)
    # print(1/0)   #  ZeroDivisionError: division by zero 
except NameError:
    print('有错误')