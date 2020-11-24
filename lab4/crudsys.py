import pymysql


def stu_create(cursor, db):
    sql = "insert into student(sno, sname, ssex, sage, sdept, scholarship) values(%s, %s, %s, %s, %s, %s)"
    sno_in = input("请输入sno:")
    sname_in = input("请输入sname:")
    ssex_in = input("请输入ssex:")
    sage_in = input("请输入sage:")
    sdept_in = input("请输入sdept:")
    scholarship_in = input("请输入scholarship:")
    params = (sno_in, sname_in, ssex_in, sage_in, sdept_in, scholarship_in)
    try:
        cursor.execute(sql, params)
        db.commit()
    except:
        db.roolback()
        print("error")


def stu_retrieve(cursor, db):
    sql = "select * from student"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            sno_out = row[0]
            sname_out = row[1]
            ssex_out = row[2]
            sage_out = row[3]
            sdept_out = row[4]
            scholarship_out = row[5]
            print("sno = %s, sname = %s, ssex = %s, sage = %s, sdept = %s, scholarship = %s" % (
                sno_out, sname_out, ssex_out, sage_out, sdept_out, scholarship_out))
    except:
        print("Error: unable to fetch data")


def stu_update(cursor, db):
    sno_to_update = input("请输入需要修改信息学生的学号sno:")
    print("请按提示输入以下待修改信息:")
    # sno_in = input("请输入sno:")
    sname_in = input("请输入sname:")
    ssex_in = input("请输入ssex:")
    sage_in = input("请输入sage:")
    sdept_in = input("请输入sdept:")
    scholarship_in = input("请输入scholarship:")
    sql = """update student set sname = %s, ssex = %s, sage = %s, sdept = %s, scholarship = %s
             where sno = %s """
    params = (sname_in, ssex_in, sage_in, sdept_in, scholarship_in, sno_to_update)
    try:
        cursor.execute(sql, params)
        db.commit()
    except:
        db.rollback()
        print("error")


def stu_delete(cursor, db):
    sql1 = "delete from student where student.sno = %s"
    sql2 = "delete from sc where sc.sno = %s"
    sno_to_delete = input("请输入要删除信息的学生号:")
    try:
        cursor.execute(sql1, sno_to_delete)
        cursor.execute(sql2, sno_to_delete)
        db.commit()
    except:
        db.rollback()
        print("error")


def course_create(cursor, db):
    sql = "insert into course(cno, cname, cpno, ccredit) values(%s, %s, %s, %s)"
    cno_in = input("请输入cno:")
    cname_in = input("请输入cname:")
    cpno_in = input("请输入cpno:")
    ccredit_in = input("请输入ccredit:")
    if cpno_in == 'NULL' or cpno_in == 'null':
        cpno_in = None
    params = (cno_in, cname_in, cpno_in, ccredit_in)
    try:
        cursor.execute(sql, params)
        db.commit()
    except:
        db.roolback()
        print("error")


def course_retrieve(cursor, db):
    sql = "select * from course"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            cno_out = row[0]
            cname_out = row[1]
            cpno_out = row[2]
            ccredit_out = row[3]
            print("cno = %s, cname = %s, cpno = %s, ccredit = %s" % (
                cno_out, cname_out, cpno_out, ccredit_out))
    except:
        print("Error: unable to fetch data")


def course_update(cursor, db):
    cno_to_update = input("请输入需要修改信息课程的课程号cno:")
    print("请按提示输入以下待修改信息:")
    # cno_in = input("请输入cno:")
    cname_in = input("请输入cname:")
    cpno_in = input("请输入cpno:")
    ccredit_in = input("请输入ccredit:")
    if cpno_in == 'NULL' or cpno_in == 'null':
        cpno_in = None
    sql = """update course set cname = %s, cpno = %s, ccredit = %s
             where cno = %s """
    params = (cname_in, cpno_in, ccredit_in, cno_to_update)
    try:
        cursor.execute(sql, params)
        db.commit()
    except:
        db.rollback()
        print("error")


def course_delete(cursor, db):
    sql = "delete from course where course.cno = %s"
    cno_to_delete = input("请输入要删除课程的课程号:")
    try:
        cursor.execute(sql, cno_to_delete)
        db.commit()
    except:
        db.rollback()
        print("error")


def sc_create(cursor, db):
    sql = "insert into sc values(%s, %s, %s)"
    sno_in = input("请输入sno:")
    cno_in = input("请输入cno:")
    grade_in = input("请输入grade:")
    if grade_in == 'NULL' or grade_in == 'null':
        grade_in = None
    params = (sno_in, cno_in, grade_in)
    try:
        cursor.execute(sql, params)
        db.commit()
    except:
        db.roolback()
        print("error")


def sc_retrieve(cursor, db):
    sql = "select * from sc"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            sno_out = row[0]
            cno_out = row[1]
            grade_out = row[2]
            print("sno = %s, cno = %s, grade = %s" % (
                sno_out, cno_out, grade_out))
    except:
        print("Error: unable to fetch data")


def sc_update(cursor, db):
    sno_to_update = input("请输入需要修改学生的学号sno:")
    cno_to_update = input("请输入需要修改信息课程的课程号cno:")
    print("请按提示输入以下待修改信息:")
    # sno_in = input("请输入sno:")
    # cno_in = input("请输入cno:")
    grade_in = input("请输入grade:")
    if grade_in == 'NULL' or grade_in == 'null':
        grade_in = None
    sql = """update sc set grade = %s
             where sno = %s and cno = %s """
    params = (grade_in, sno_to_update, cno_to_update)
    try:
        cursor.execute(sql, params)
        db.commit()
    except:
        db.rollback()
        print("error")


def sc_delete(cursor, db):
    sql = "delete from sc where sno = %s and cno = %s"
    sno_to_delete = input("请输入要删除学生的学号:")
    cno_to_delete = input("请输入要删除课程的课程号:")
    try:
        cursor.execute(sql, (sno_to_delete, cno_to_delete))
        db.commit()
    except:
        db.rollback()
        print("error")


def stastic_sc_bydept(cursor, db):
    print("请按提示输入以下信息:")
    sdept_in = input("院系:")
    con_in = input("课程号:")

    # 总人数
    sql = "SELECT Count(*) FROM SC,Student WHERE Student.Sdept='%s' AND SC.Cno='%s' AND SC.Sno = Student.Sno "
    cursor.execute(sql, (sdept_in, con_in))
    # db.commit()
    results = cursor.fetchall()
    for row in results: all = row[0]

    # 平均成绩
    sql = "SELECT AVG(Grade) FROM SC,Student WHERE Student.Sdept='%s' AND SC.Cno='%s' AND SC.Sno = Student.Sno"
    cursor.execute(sql, (sdept_in, con_in))
    # db.commit()
    results = cursor.fetchall()
    for row in results: avg = row[0]

    # 最好成绩
    sql = "SELECT MAX(Grade) FROM SC,Student WHERE Student.Sdept='%s' AND SC.Cno='%s' AND SC.Sno = Student.Sno"
    cursor.execute(sql, (sdept_in, con_in))
    # db.commit()
    results = cursor.fetchall()
    for row in results: max = row[0]

    # 最差成绩
    sql = "SELECT MIN(Grade) FROM SC,Student WHERE Student.Sdept='%s' AND SC.Cno='%s' AND SC.Sno = Student.Sno"
    cursor.execute(sql, (sdept_in, con_in))
    # db.commit()
    results = cursor.fetchall()
    for row in results: min = row[0]

    # 优秀率
    sql = "SELECT Count(Grade) FROM SC,Student WHERE Student.Sdept='%s' AND SC.Cno='%s' AND SC.Grade >= 90 AND Student.Sno = SC.Sno "
    cursor.execute(sql, (sdept_in, con_in))
    # db.commit()
    results = cursor.fetchall()
    for row in results: good = row[0]

    # 不及格人数
    sql = "SELECT Count(Grade) FROM SC,Student WHERE Student.Sdept='%s' AND SC.Cno='%s' AND SC.Grade < 60 AND Student.Sno = SC.Sno "
    cursor.execute(sql, (sdept_in, con_in))
    # db.commit()
    results = cursor.fetchall()
    for row in results: failed = row[0]

    print("平均成绩：", avg)
    print("最好成绩：", max)
    print("最差成绩：", min)
    good = good / all
    print("优秀率：", good)
    print("不及格人数", failed)


def rank_bydept(cursor, db):
    print("请按提示输入以下信息:")
    sdept_in = input("院系:")
    cno_in = input("课程号:")
    sql = "SELECT Student.Sno,Student.Sname,Course.Cno,Course.Cname,SC.Grade FROM Student,Course,SC WHERE Student.Sdept = '%s' AND Course.Cno = '%s' AND Course.Cno = SC.Cno AND SC.Sno=Student.Sno ORDER BY SC.Grade DESC"
    cursor.execute(sql, (sdept_in, cno_in))
    results = cursor.fetchall()
    for row in results:
        print("学号：%s,姓名：%s,课程号：%s,课程名：%s,成绩：%s" % (row[0], row[1], row[2], row[3], row[4]))


def info_bysno(cursor, db):
    sno_in = input("请输入要查询学生的学号:")
    sql1 = "select * from student where sno = %s"
    sql2 = "select sc.cno, cname, grade from sc, course where course.cno = sc.cno and sno = %s"
    cursor.execute(sql1, sno_in)
    results = cursor.fetchall()
    print("学生信息为:")
    for row in results:
        sno_out = row[0]
        sname_out = row[1]
        ssex_out = row[2]
        sage_out = row[3]
        sdept_out = row[4]
        scholarship_out = row[5]
        print("sno = %s, sname = %s, ssex = %s, sage = %s, sdept = %s, scholarship = %s" % (
            sno_out, sname_out, ssex_out, sage_out, sdept_out, scholarship_out))
    cursor.execute(sql2, sno_in)
    results = cursor.fetchall()
    print("选课信息为:")
    for row in results:
        cno_out = row[0]
        cname_out = row[1]
        grade_out = row[2]
        print("cno = %s, cname = %s, grade = %s" % (cno_out, cname_out, grade_out))
