str1 = 'aa'
str2 = 'bb'

list1 = [1,2]
list2 = [10,20]

t1 = (1,2)
t2 = (10,20)

dict1 = {'name': 'Python'}
dict2 = {'age': 30}

# +:合并
print(str1 + str2)   #aabb
print(list1 + list2)#[1, 2, 10, 20]
print(t1 + t2)#(1, 2, 10, 20)

# print(dict1 + dict2)  不支持合并，会报错