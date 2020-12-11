t1 = ('aa', 'bb', 'cc', 'bb')

# 1.按下标查找数据
print(t1[0])   # aa
# 2.index() --查找数据返回下标
print(t1.index('aa'))
# print(t1.index('aaa'))  # 不存在会报错
# 3.count()
print(t1.count('aa'))  # 1
print(t1.count('bb'))  # 出现2次
# 4.len()
print(len(t1))  # 4