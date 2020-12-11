
name_list = ['TOM', 'Lily', 'ROSE']

# 1.del 目标   --可以是数据也可以是列表
# del name_list
# del(name_list)
# print(name_list)  # 会报错 NameError: name 'name_list' is not defined
# 可以删除指定下标的数据
# del(name_list[1])  # ['TOM', 'ROSE']
# print(name_list)

#2.pop(下标)  --删除制定下标的数据，如果不指定，那么默认删除最后一个数据
# del_name = name_list.pop()   # ['TOM', 'Lily']
del_name = name_list.pop(1)   # Lily
print(del_name)
# print(name_list)

# 3.remove(数据)

# name_list.remove('Lily')  # ['TOM', 'ROSE']
# print(name_list)

#4.clear()  --清空列表
name_list.clear()  #  []
print(name_list)
