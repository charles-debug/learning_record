a=1
b=2
c=3

# and 与 都真才真

print(a<b and b<c)  # true
print(a>b and b<c)  # false

# or 或 一真则真， 都假才假

print(a<b or b<c)
print(a<b or b<c)
print(a>b or b>c)

# not 非 取反

print(not False)
print(not c>b)


# 逻辑运算符书写规范
 # 一般要加上()
print((a<b) and (b<c))

# 数字的逻辑运算符
print(0 and 1)  # and 运算符一个为0则结果返回0，若均不为0，则返回最后一个非0数字
print(1 and 2)
print(2 and 1)
print(0 or 0)  # or 运算符都为0则返回值为0，其中一个不为0，则返回第一个非0数字
print(0 or 1)
print(1 or 2)