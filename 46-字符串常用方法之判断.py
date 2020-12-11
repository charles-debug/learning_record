mystr = "hello world and itcast and itheima and Python"
# 1. startswith()
#print(mystr.startswith('hello'))
#print(mystr.startswith('hel'))
#print(mystr.startswith('hels'))

#2.endswith
#print(mystr.endswith('Python'))


#3.isalpha()  --都是字母
print(mystr.isalpha())

#4.isdigit()  --都是数字
print(mystr.isdigit())
mystr1 = '123456'
print(mystr1.isdigit())

# 5. isalnum() --都是数字或字母或组合
print(mystr.isalnum())  # mystr中含有空格
print(mystr1.isalnum())
mystr2 = 'abc123'
print(mystr2.isalnum())

# 6.isspace  --空白
print(mystr.isspace())
mystr3='     '
print(mystr3.isspace())
