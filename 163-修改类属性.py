class Dog(object):
    tooth = 10

wangcai = Dog()
xiaohei = Dog()

# 类修改   类.类属性 = 值
# Dog.tooth = 20

# print(Dog.tooth)  #20
# print(wangcai.tooth) # 20
# print(xiaohei.tooth)   # 20
# 对象修改类属性

wangcai.tooth = 15   # 只是相当于创建了一个实例属性

print(Dog.tooth)   # 10
print(wangcai.tooth)  # 15
print(xiaohei.tooth)  # 10
