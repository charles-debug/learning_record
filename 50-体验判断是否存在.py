"""  
需求：注册邮箱 ，用户输入一个账号名，判断账号名是否存在，若存在提示用户，不存在提示用户可以注册
步骤：
1. 用户输入一个账号名
2. 判断  if...else

"""

name_list = ['TOM', 'Lily', 'ROSE']

name = input('请输入你的邮箱账号名：')

if name in name_list:
    print(f'您输入的名字是{name}, 该用户名已存在')

else:
    print(f'您输入的名字是{name},你可以继续注册')