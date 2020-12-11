mystr = "hello world and itcast and itheima and Python"

#1. find()
print(mystr.find('and')) # 12  and 开始的下标位置
print(mystr.find('and',15,30)) # 23   在(15，30)范围内查找and
print(mystr.find('ands')) # -1 表明ands不存在
 
#2.index()
print(mystr.index('and')) # 12
print(mystr.index('and',15,30)) #23
# print(mystr.index('ands'))  # ands 不再字符串中，使用index方法会报错

#3.count()  统计出现的次数
print(mystr.count('and',15,30))  #1
print(mystr.count('and'))  #3
print(mystr.count('ands')) # 0


#4.rfind()从右侧开始查找
print(mystr.rfind('and'))  # 35
print(mystr.rfind('ands'))  # -1

#5.rindex
print(mystr.rindex('and')) # 35
print(mystr.rindex('ands'))  # 报错
