# 1.定义类，定义静态方法
class Dog(object):
    
    @staticmethod
    def print_info():
        print('这是一个静态方法')


# 2.创建对象
wangcai = Dog()
# 3.调用静态方法：类和对象

wangcai.print_info()
Dog.print_info()