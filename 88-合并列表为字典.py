list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, '男']

dict1 = {list1[i]:list2[i] for i in range(len(list1))}  #  --(0,3)
print(dict1)

# 还是在使用for循环
# 如果两个列表的值不等，如list1 = ['name','age', 'gender', 'id'] 再使用len()会报错
# 应该选择使用列表数据短的那个