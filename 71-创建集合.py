#  1.创建有数据的集合  {}或set()
s1 = {10, 20, 30, 40, 50}
print(s1)   #{40, 10, 50, 20, 30}

s2 = {10, 20, 10, 40, 20}
print(s2)  #{40, 10, 20}

s3 = set('abcdefg')
print(s3)    #{'c', 'b', 'a', 'e', 'd', 'f', 'g'}

# 2.创建无数据的集合

s4 = set()
print(s4)  # set()
print(type(s4))  #(class set)

s5 = {}
print(type(s5))  # class dict