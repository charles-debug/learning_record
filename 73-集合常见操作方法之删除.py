s1 = {10, 20, 30, 40, 50}

# 1.remove()  --删除指定数据，不存在时会报错
# s1.remove(10)
# print(s1)

# s1.remove(10)
# print(s1) # KeyError: 10

# 2. discard()  --删除指定数据，不存在也不报错
# s1.discard(10)
# print(s1)
# 再次删除10
# s1.discard(10)
# print(s1)  # {40, 50, 20, 30}

#3. pop()  --随机删除数据，并返回这个值
del_num = s1.pop()
print(del_num)  # 40
print(s1)  # {10, 50, 20, 30}
