# 方法一
""" 
1.导入包    
包名.模块名

2.调用功能
包名.模块名.功能
 """
# 导入mypackage 包下的模块一，使用这个模块的info_print 函数
import mypackage.my_module1
mypackage.my_module1.info_print()

# 方法二：
#　注意设置 __init__.py里面的all 列表，添加的是允许导入的模块

""" 
from 包名 import *
模块名.目标
 """

from mypackage import *
my_module1.info_print()