dict1 = {'name':'TOM', 'age':20, 'gender': '男'}

# del 删除字典或指定的键值对

# del dict1
# del(dictl)
# print(dict1)

# 删除name 键值对
# del dict1['name']  #{'age': 20, 'gender': '男'}
# del(dict1['name'])  # {'age': 20, 'gender': '男'}
# print(dict1)  

# 2.clear()  清空字典，删除所有键值对

dict1.clear()  # {}
print(dict1)
