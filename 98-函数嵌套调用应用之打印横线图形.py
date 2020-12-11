# 打印一条横线

def print_line():
    print('-'*20)

# print_line()

# 打印多个横线
# 非循环嵌套
def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1

print_lines(5)

