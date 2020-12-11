"""
准备数据
格式化输出数据
"""
name = 'TOM'
age = 18
weight = 75.5
stu_id = 1

# 1. 今年我的年龄是x岁
print('今年我的年龄是%d岁'%age)

# 2. 我的名字是x
print('我的名字是%s'%name)

# 3. 我的体重是x公斤
print('我的体重是%.2f公斤'%weight)

# 4. 我的学号是x
print('我的学号是%d'%stu_id)

# 4.1 我的学号是x
print('我的学号是%03d'%stu_id)


# 5. 我的名字是x, 今年x岁了
print('我的名字是%s, 今年%d岁了'%(name,age))

# 5.1 我的名字是x, 今年x岁了
print('我的名字是%s, 明年%d岁了'%(name,age+1))

# 6. 我的名字是x, 今年x岁了， 体重x公斤，学号是x
print('我的名字是%s, 今年%d岁了， 体重%.2f公斤，学号是%06d' % (name, age, weight, stu_id))

