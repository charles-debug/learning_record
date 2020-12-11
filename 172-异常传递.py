# 以只读的方式打开test.txt文档，如异常则给出提示
# 以行的性读取文档内容，如出现的意外的情况时，捕捉异常
import time
try:
    f = open('test.txt')
    try:
        while True:
            con = f.readline()
            #　如读取完成退出循环
            if len(con) == 0:
                break
            time.sleep(3)
            print(con)
    except:
        # 如此刻按下了ctrl+c
        print('程序被意外中止')

except:
    print('文档无法打开')