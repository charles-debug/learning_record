# 尝试捕获所有异常，打印num  捕获exception

try:
    print(1/0)
    # print(num)
except Exception as result:
    print(result)


    # 不需要人为指定异常类型