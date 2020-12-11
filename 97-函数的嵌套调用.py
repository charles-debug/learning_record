# 定义两个函数，函数B在函数A 里调用


# B 函数
def testB():
    print('B函数的开始--------')
    print('这是B函数的代码部分')
    print('B函数的结束--------')
# A 函数

def testA():
    print('A函数的开始-------')
    testB()
    print('A函数的结束-------')

testA()