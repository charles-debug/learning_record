# 0-10之间的偶数数据

# range实现
list1 = [i for i in range(0,10,2)]
print(list1)

# 用for 循环加if语句实现

list2 = []
for i in range(10):
    if i % 2 == 0:
        list2.append(i)
print(list2)

# 带if的列表推导式

list3 = [i for i in range(10) if i%2==0]
print(list3)