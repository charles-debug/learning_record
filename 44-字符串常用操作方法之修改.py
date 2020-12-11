mystr = "hello world and itcast and itheima and Python"


# 1.replace()
# replace() 把'and' 替换成 'he'
#new_str = mystr.replace('and', 'he')
#new_str = mystr.replace('and', 'he',1) # 表示替换一个and

# 如果替换次数超过该子串出现的最大值，则表示替换所有
#new_str = mystr.replace('and', 'he', 10)
#print(mystr)
#print(new_str)

# 调用replace函数后发下原字符串并未得到改，修改后的数据是replace调用后的返回值
# ** 字符串是不可变类型的数据

# 2. split()--分割，返回一个列表，会丢失分割符
# list1 = mystr.split('and')
#list1 = mystr.split('and',2)
#print(list1)

#3.join --字符串拼接，将序列内的字符串拼接成一个大字符串
# 语法： 字符或子串.join(序列)
mylist = ['aa','bb','cc']
# aa...bb...cc
new_str = "...".join(mylist)
print(new_str)

