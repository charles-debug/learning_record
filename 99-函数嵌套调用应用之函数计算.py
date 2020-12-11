# 三个数的求和

def sum_num(a, b, c):
    return a + b + c
    

result = sum_num(1,2,3)
# print(result)

# 三个数求平均值

def avg_num(a,b,c):
    # 先求和，在除于3
    sumResult = sum_num(a, b, c)   # 这里跟result调用一样的意思  就是return及其前面的代码是一个整体，后面可以对其使用
    return sumResult/3

avg = avg_num(1,2,3)
print(avg)
