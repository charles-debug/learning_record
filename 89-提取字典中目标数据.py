#  需求:查找销售数量大于200的数据
# 获取所有的键值对，并判断大于200

counts = {'MBP':268, 'HP':125, 'DELL':201, 'lenovo': 199, 'acer':99}

# print(counts.items())

dict = {key:value for key,value in counts.items() if value >=200}
print(dict)

