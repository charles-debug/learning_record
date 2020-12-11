t1 = ('aa', 'bb', 'cc', 'dd')
# t1[0]='aaa'
# print(t1)

t2 = ('aa', 'bb', ['cc','dd'])
t2[2][0] = 'TOM'
print(t2)  #('aa', 'bb', ['TOM', 'dd'])

