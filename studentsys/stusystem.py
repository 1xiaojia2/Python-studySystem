import os

filename = 'student.txt'


# 菜单
def menu():
    print('学生信息管理系统'.center(66, '='))
    print('功能菜单'.center(68, '-'))
    print('\t\t\t\t1.录入学生信息')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.删除学生信息')
    print('\t\t\t\t4.修改学生信息')
    print('\t\t\t\t5.排序')
    print('\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t0.退出系统')
    print('-----------------------------------------------------------------------')


# 输入学生信息
def insert():
    student_list = []
    while 1:
        num = input('请输入学生ID（如1001）:')
        flag = True
        if os.path.exists(filename):
            with open(filename, 'r', encoding='UTF-8') as file:
                stu_lst = file.readlines()
            for item in stu_lst:
                d = dict(eval(item))
                if d['ID'] == num:
                    flag = False
                else:
                    continue
        if not flag:
            print('输入学号重复！请重新输入！')
            continue
        if not num:
            break
        name = input('请输入学生姓名:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入Python成绩:'))
            java = int(input('请输入Java成绩:'))
        except:
            print('输入无效，请重新输入!')
            continue
        # 将成绩存入字典
        student = {'ID': num, 'Name': name, 'English': english, 'Python': python, 'Java': java}
        # 将字典存入列表
        student_list.append(student)
        answer = input('是否继续添加?y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完毕!')


# 保存学生信息
def save(lst):
    try:
        stu = open(filename, 'a', encoding='UTF-8')
    except:
        stu = open(filename, 'w', encoding='UTF-8')
    for item in lst:
        stu.write(str(item) + '\n')
    stu.close()


# 查找学生信息
def search():
    while 1:
        choose = input('你要根据姓名(1)查找还是根据ID(2)查找(请输入选项):')
        if choose == '2':
            stu = input('请输入你要查找的学生ID:')
        elif choose == '1':
            stu = input('请输入你要查找的学生姓名:')
        else:
            print('请输入正确选项!')
            continue
        if stu != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='UTF-8') as file:
                    student = file.readlines()
            else:
                student = []
            Flag = 0
            if student:
                stu_lst = []
                for item in student:
                    d = dict(eval(item))
                    if choose == '2':
                        if d['ID'] == stu:
                            Flag += 1
                            stu_lst.append(d)
                        else:
                            continue
                    else:
                        if d['Name'] == stu:
                            Flag += 1
                            stu_lst.append(d)
                        else:
                            continue
                if not Flag:
                    print('没有找到此学生!')
            else:
                print('无学生信息!')
                return
            show_student(stu_lst)
        else:
            continue
        answer = str(input('您要继续查找吗？y/n'))
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break


# 显示学生信息
def show_student(lst):
    if not lst:
        print('没有查询到学生信息!')
        return
    format_title = '{:^6}\t{:^12}{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', "姓名", '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    format_data = '{:^6}\t{:^15}{:^8}\t{:^18}\t{:^5}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('ID'),
                                 item.get('Name'),
                                 item.get('English'),
                                 item.get('Python'),
                                 item.get('Java'),
                                 int(item.get('English')) + int(item.get('Python')) + int(item.get('Java'))
                                 ))


# 删除学生信息
def delete():
    while 1:
        stu = str(input('请输入要删除的学生ID:'))
        if stu != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='UTF-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w', encoding='UTF-8') as wfile:
                    for item in student_old:
                        d = dict(eval(item))
                        if d['ID'] != stu:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'你所输入ID为{stu}的学生信息已删除!')
                    else:
                        print('你所输入的学生ID不存在!')
            else:
                print('无学生信息!')
                return
        else:
            continue
        show()
        answer = str(input('还要继续删除吗？y/n'))
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break


# 修改学生信息
def modify():
    while 1:
        stu = input('请输入要修改学生的学号:')
        if stu:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='UTF-8') as file:
                    stu_lst = file.readlines()
            else:
                stu_lst = []
            flag = False
            if stu_lst:
                with open(filename, 'w', encoding='UTF-8') as wfile:
                    for item in stu_lst:
                        d = dict(eval(item))
                        if d['ID'] == stu:
                            flag = True
                            try:
                                a = input('修改后的名字为:')
                                if a:
                                    b = int(input('修改后的英语成绩为:'))
                                    c = int(input('修改后的Pyth成绩为:'))
                                    e = int(input('修改后的java成绩为:'))
                                else:
                                    print('输入错误!')
                                    wfile.write(str(d) + '\n')
                                    break
                            except BaseException:
                                print('输入信息有误，请重新输入!')
                                wfile.write(str(d) + '\n')
                                break
                            d['Name'] = a
                            d['English'] = b
                            d['Python'] = c
                            d['Java'] = e
                            print('修改成功！')
                        wfile.write(str(d) + '\n')
                    if not flag:
                        print(f'没有学号为{stu}的学生!')
            else:
                print('学生信息为空!')
                return
        else:
            modify()
        answer = str(input('还要继续修改吗？y/n'))
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break


# 排序
def sort():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='UTF-8') as file:
            stu_lst = file.readlines()
        stu = []
        for item in stu_lst:
            d = dict(eval(item))
            stu.append(d)
        asc_or_desc = input('请选择排序（0.升序 1.降序）:')
        if asc_or_desc == '0':
            asc_or_desc_bool = False
        elif asc_or_desc == '1':
            asc_or_desc_bool = True
        else:
            print('请输入正确选项!')
            return
        method = input('请选择排序方式（1. 按英语成绩 2.按Python成绩 3. 按Java成绩 0.按总成绩）:')
        if method == '1':
            stu.sort(key=lambda stu: int(stu['English']), reverse=asc_or_desc_bool)
        elif method == '2':
            stu.sort(key=lambda stu: int(stu['Python']), reverse=asc_or_desc_bool)
        elif method == '3':
            stu.sort(key=lambda stu: int(stu['Java']), reverse=asc_or_desc_bool)
        elif method == '0':
            stu.sort(key=lambda stu: int(stu['English']) + int(stu['Python']) + int(stu['Java']),
                     reverse=asc_or_desc_bool)
        else:
            print('请输入正确选项!')
            return
        show_student(stu)
    else:
        print('暂无学生信息!')


# 统计学生总人数
def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='UTF-8') as file:
            stu_lst = file.readlines()
            if stu_lst:
                print(f'一共{len(stu_lst)}个学生')
            else:
                print('没有学生信息!')
    else:
        print('没有学生信息!')

    return


# 显示所有学生信息
def show():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='UTF-8') as file:
            stu_lst = file.readlines()
    else:
        stu_lst = []
    if stu_lst:
        format_title = '{:^6}\t{:^12}{:^8}\t{:^10}\t{:^10}\t{:^8}'
        print(format_title.format('ID', "姓名", '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
        format_data = '{:^6}\t{:^15}{:^8}\t{:^18}\t{:^5}\t{:^8}'
        stu = []
        for item in stu_lst:
            d = dict(eval(item))
            stu.append(d)
        for item in stu:
            print(format_data.format(item.get('ID'),
                                     item.get('Name'),
                                     item.get('English'),
                                     item.get('Python'),
                                     item.get('Java'),
                                     int(item.get('English')) + int(item.get('Python')) + int(item.get('Java'))
                                     ))
    else:
        print('无学生信息!')
        return


if __name__ == '__main__':
    while 1:
        menu()
        try:
            option = input('请选择:')
        except BaseException:
            print('\n程序结束,感谢使用!')
            break
        if option == '0':
            answer = str(input('您确定要退出系统吗？y/n'))
            if answer == 'y' or answer == 'Y':
                print('退出系统成功!!!感谢您的使用!!!')
                break
            else:
                continue
        elif option == '1':
            insert()
        elif option == '2':
            search()
        elif option == '3':
            delete()
        elif option == '4':
            modify()
        elif option == '5':
            sort()
        elif option == '6':
            total()
        elif option == '7':
            show()
        else:
            print('输入选项不正确！请重新输入:')
            continue
