s1 = {10,20}

# 1. add()  适用于追加单个数据

s1.add(100)
print(s1)  # {100, 10, 20}

# 集合具有去重功能已有要添加的数据时，不执行任何操作
s1.add(100)
print(s1)  # {100, 10, 20}

# 2. update()  适用于追加序列

s1.update([10,20,40,50])
print(s1)   # {100, 40, 10, 50, 20}