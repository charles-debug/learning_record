"""
break 当某些条件成立，退出整个循环
情景：
共有五个苹果，吃苹果的动作是循环的，吃完三个后，不吃了，则退出循环
"""

i=1

while i<=5:
    if i ==4:
        print('不吃了，吃饱了')
        break # break 以后的代码不执行，print()不可以放在break后面
    print(f'吃了{i}个苹果')
    i += 1
