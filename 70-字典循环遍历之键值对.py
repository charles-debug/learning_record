dict1 = {'name':'TOM', 'age':20, 'gender': '男'}

 # for item in dict1.items():
   #  print(item)

""" 
输出结果：

('name', 'TOM')
('age', 20)
('gender', '男')
 """

 # 拆包
for key, value in dict1.items():
    print(key)
    print(value)