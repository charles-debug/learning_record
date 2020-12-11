dict1 = {'name':'TOM', 'age':20, 'gender': '男'}

# 1.[key]
# print(dict1['name'])  #TOM
# print(dict1['id'])  # 会报错

# 2. 函数
# 2.1 get(key, 默认值)
print(dict1.get('name'))   # TOM
print(dict1.get('names', 'Lily'))   # Lily
print(dict1.get('names'))    # None
#2.2 keys()  #查找字典中所有的键（key） 返回一个可迭代的对象
print(dict1.keys()) # dict_keys(['name', 'age', 'gender'])
# 2.3 values() # 查找字典中所有的value（值） 返回一个可迭代的对象
print(dict1.values())  # dict_values(['TOM', 20, '男'])
# 2.4 items()   # 查找字典中的所有键值对，并以元组的形式返回  返回一个可迭代的对象
print(dict1.items())  # dict_items([('name', 'TOM'), ('age', 20), ('gender', '男')])