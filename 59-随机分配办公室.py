"""  
需求：有三个办公室，八位老师随机分配到到三个办公室
步骤：
1.准备数据  
   1.1 八个老师数据
   1.2 三个办公室  --列表嵌套
2.分配老师办公室
随机分配 random
办公室列表追加名字

3.验证
打印办公室详细信息：办公室人数和人名
"""

import random
# 1.准备数据
teachers = ['A','B','C','D','E','F','G','H']
offices = [[], [], []]

# 2.分配老师到办公室    ----遍历老师列表数据   把老师随机加到三个办公室中的一个
for name in teachers:
    num = random.randint(0,2)
    offices[num].append(name)

# print(offices)
# 贴合生活，给办公室加编号
i=1
for office in offices:
    print(f'办公室{i}的人数是{len(office)}, 老师分别是：')

    for name in office:
        print(name)

    i+=1
