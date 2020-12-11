try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('捕获异常')