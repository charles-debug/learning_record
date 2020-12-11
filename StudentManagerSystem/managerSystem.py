from student import *

class StudentManager(object):
    def __init__(self):
        # 存储学员数据    ----列表
        self.student_list = []


    # 一、程序入口函数，启动程序后执行的函数
    # 1.加载文件里面的学生数据
    def run(self):
        self.load_student()
        
        while True:
            # 2.显示功能菜单
            self.show_menu()
            # 3.用户输入目标功能序号
            men_num = int(input('请输入要选择的功能序号：'))
            # 4.根据用户输入的不同的序号执行不同的功能
            if men_num == 1:
                #添加学员
                self.add_student()

            elif men_num == 2:
                # 删除学员
                self.del_student()

            elif men_num == 3:
                # 更改学员
                self.modify_student()

            elif men_num == 4:
                #查询学员
                self.search_student()

            elif men_num == 5:
                # 显示所有学员信息
                self.show_student()

            elif men_num == 6:
                # 保存学员信息
                self.save_student()

            elif men_num == 7:
                # 退出系统
                break

    # 二、系统功能函数
    # 2.1 显示功能菜单
    @staticmethod
    def show_menu():
        print('功能如下')
        print('1.增加学员')
        print('2.删除学员')
        print('3.更改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.退出系统')
        
    # 2.2 添加学员
    def add_student(self):
        # 1.用户输入姓名性别手机号码   ----先导入student类 在student.py文件里
        name = input('请输入姓名：')
        gender = input('请输入性别：')
        tel = input('请输入手机号码：')
        # 2.创建对象
        student = Student(name,gender,tel)
        # 3.将该对象添加到学院列表
        self.student_list.append(student)    #  吧对象添加进列表
        print(self.student_list)
        print(student)

    # 2.3 删除学员
    def del_student(self):
        # 1.用户输入学员姓名
        del_name = input('请输入要删除的学员姓名：')
        # 2.遍历列表，存在删除，不存在报错
        for i in self.student_list:

            if del_name == i.name:
            # i 是对象直接查看其name 这个属性值
                self.student_list.remove(i)
                break
        
        else:
            print('查无此人')

        print(self.student_list)

    # 2.4 更改学员信息
    def modify_student(self):
        # 1.用户输入学院姓名
        modify_name = input('请输入学员姓名：')
        # 2.遍历列表，存在修改，不存在提示
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('请输入姓名：')
                i.gender = input('请输入性别：')
                i.tel = input('请输入手机号')
                print(f'修改成功！学员的姓名：{i.name},性别：{i.gender},手机号：{i.tel}')
                break

        else:
            print('查无此人!')

    # 2.5 查询学员  
    def search_student(self):
        # 1.输入学员姓名
        search_name = input('请输入要搜索的学员姓名：')
        # 2.遍历列表，存在打印信息
        for i in self.student_list:
            if search_name == i.name:
                print(f'姓名是：{i.name},性别是：{i.gender},手机号是：{i.tel}')
                break
        else:
            print('查无此人！')


    # 2.6 显示所有学员信息
    def show_student(self):
        # 1. 打印表头
        print('姓名\t性别\t手机号')
        # 2.打印学员信息
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')
    # 2.7 保存学员信息
    def save_student(self):
        # 1.打开文件
        f = open('student.data','w')
        # 2.文件数据写入
        # 2.1 学员对象转换成字典
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        # 2.2 文件写入，字符串数据
        f.write(str(new_list))
        print('保存完成')
        # 3.关闭文件
        f.close()

    # 2.8 加载学员信息
    def load_student(self):
        # 1.打开文件：尝试以r打开，文件不存在以w 打开
        try:
            f = open('student.data','r')

        except:
            f = open('student.data','w')
        
        else:
            # 2.读取数据，文件读取出的数据是字符串  需还原成列表：[{}]  ->   [学员对象]
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'], i[gender], i[tel]) for i in new_list]
        finally:
            # 3.关闭文件
            f.close()