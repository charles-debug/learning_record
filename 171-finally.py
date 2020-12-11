try:
    f = open('test105.txt','r')
except Exception as result:
    f = open('test105.txt','w')
finally:
    f.close()