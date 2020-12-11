# 需求：尝试打开test.txt（r）文档，如果不存在以只写的方式打开
""" 
try:
    可能会报错的代码
except:
    如果出现报错执行的代码
"""

try:
    f = open('test00.txt','r')
except:
    f = open('test00.txt','w')