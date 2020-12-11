# 定义类：私有类属性 类方法获取类属性
class Dog():
    __tooth = 10


# 定义类方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth

# 创建对象，调用类方法
wangcai = Dog()
result = wangcai.get_tooth()
print(result)