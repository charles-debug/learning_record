# 1.自定义异常  继承exception  定义魔法方法__init__ 和 __str__(设置异常描述信息)
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        # 用户输入的密码长度
        self.length = length
        # 系统要求最短长度
        self.min_len = min_len

    def __str__(self):
        return f'您输入的密码长度为{self.length},系统要求的最短密码长度为{self.min_len}'

# 2.抛出异常   尝试执行，如果用户输入的长度小于3则抛出异常
def main():
    try:
        password = input('请输入密码:')
        if len(password) < 3:
            raise ShortInputError(len(password), 3)    # 关键字raise  抛出异常的关键字

    except Exception as result:
        print(result)
    else:
        print('密码输入正确')

main()



# 3.捕获异常