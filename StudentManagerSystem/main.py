from managerSystem import *

# 1.导入系统管理模块

# 2.启动管理系统
# 保证是当前文件运行才启动管理系统，if 判断----创建对象并调用run方法
if __name__ == "__main__":
    student_manager = StudentManager()
    student_manager.run()