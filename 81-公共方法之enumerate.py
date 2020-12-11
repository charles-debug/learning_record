list1 = ['a', 'b', 'c', 'd','e']

# enumerate(遍历对象， start = )
# enumerate返回的数据数元组，元组的第一个数据是迭代对象数的下标，第二个对象是迭代的数据
for i in enumerate(list1):
    print(i)

for i in enumerate(list1, start=1):  # 表示下标数据从1开始
    print(i)