list1 = [10, 20, 30, 40, 50]
s1 = {100, 200, 300, 400, 500}
t1 = ('a', 'b', 'c', 'd', 'e')

#list()  --转换成列表
# print(list(t1))  ['a', 'b', 'c', 'd', 'e']

# print(list(s1))  [100, 200, 300, 400, 500]
#tuple() --转换成元组
print(tuple(list1))
print(tuple(s1))

#set() --转换成集合 
print(set(list1))
print(set(t1))