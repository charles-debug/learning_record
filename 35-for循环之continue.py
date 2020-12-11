str1 = 'itheima'
for i in str1:
   # 当某些条件成立时，退出循环 break ----条件： i 取值为e0
    if i == 'e':
        print('不打印e')
        continue
    print(i)