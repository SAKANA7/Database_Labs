from crudsys import *


def menu():
    print(" Welcome to Student Management System ! ")
    print("        Designed by ***********         ")
    print("1. student_create   2. student_retrieve ")
    print("3. student_update   4. student_delete   ")
    print("5. course_create    6. course_retrieve  ")
    print("7. course_update    8. course_delete    ")
    print("9. sc_create        10. sc_retrieve     ")
    print("11. sc_update       12. sc_delete       ")
    print("13. stastic_bydept  14. rank_bydept     ")
    print("15. info_bysno                          ")



def func_select(func, cursor, db):
    if int(func) < 1 or int(func) > 15:
        func = input("输入了错误的功能号")
        return
    elif func == '1':
        stu_create(cursor, db)
    elif func == '2':
        stu_retrieve(cursor, db)
    elif func == '3':
        stu_update(cursor, db)
    elif func == '4':
        stu_delete(cursor, db)
    elif func == '5':
        course_create(cursor, db)
    elif func == '6':
        course_retrieve(cursor, db)
    elif func == '7':
        course_update(cursor, db)
    elif func == '8':
        course_delete(cursor, db)
    elif func == '9':
        sc_create(cursor, db)
    elif func == '10':
        sc_retrieve(cursor, db)
    elif func == '11':
        sc_update(cursor, db)
    elif func == '12':
        sc_delete(cursor, db)
    elif func == '13':
        stastic_sc_bydept(cursor, db)
    elif func == '14':
        rank_bydept(cursor, db)
    elif func == '15':
        info_bysno(cursor, db)


def get_all():
    # 隐匿了个人信息
    db = pymysql.connect("***", "**", "***", "***")
    cursor = db.cursor()
    yes_or_no = 'n'
    while yes_or_no != 'y':
        menu()
        func = input("请选择功能:")
        func_select(func, cursor, db)
        yes_or_no = input("是否退出(y/n):")
    db.close()


get_all()

