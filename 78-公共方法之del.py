str1 = 'abcdefg'
list1 = [10,20,30,40, 50]
t1 = (10,20,30,40, 50)
s1 = {10,20,30,40, 50}
dict1 = {'name': 'TOM', 'age': 18}

# del 目标 或del (目标)

# 可删除序列和指定目标

""" 
del str1
print(str1)
del(str1)
print(str1) 
"""
""" 
del list1
del t1
del s1
del dict1

del(list1)
del(t1)
del(s1)
del(dict1) 
"""

# 字符串和元组是不可变类型，不可删除
# del list1[0]
# print(list1)
del t1[0]
print(t1)