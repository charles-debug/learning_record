
name_list = ['TOM', 'Lily', 'ROSE']

#1.修改指定下标的数据

name_list[0] = 'aaa'   # ['aaa', 'Lily', 'ROSE']
print(name_list)



#2. 逆序 reverse（）

list1 = [1,3,2,5,4,6]
# list1.reverse()
# print(list1)

# 3. 排序 sort() 升序（默认）和降序   true 为降序， false为升序
# list1.sort()
list1.sort(reverse=True)  
print(list1)
