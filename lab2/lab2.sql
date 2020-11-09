--（1）查询每门课程及其被选情况（输出所有课程中每门课的课程号、课程名称、选修该课程的学生学号及成绩(如果没有学生选择该课，则相应的学生学号及成绩为空值）。
select course.cno,course.cname,sc.sno,sc.grade
from course left outer join sc on(course.cno = sc.cno);
--（2）查询与“张立”同岁的学生的学号、姓名和年龄。（要求使用至少 3 种方法求解）
select sno,sname,sage
from student
where sage = (select sage
from student
where sname='张立');

select sno,sname,sage
from student
where sage in (select sage
from student
where sname='张立');

select s1.sno,s1.sname,s1.sage
from student s1,student s2
where s1.sage = s2.sage and s2.name='张立';
--（3）查询选修了 3 号课程而且成绩为良好（80~89 分）的所有学生的学号和姓名。
select sc.sno,student.sname
from sc,student
where cno = '3' and 80 <= grade <= 90 and student.sno = sc.sno;
--（4）查询学生 200215122 选修的课程号、课程名（思考：如何查询学生 200215122 选修的课程号、课程名及成绩？）
select course.cname,course.cno,grade
from course,sc
where sc.sno='200215122' and sc.cno = course.cno;
--（5）找出每个学生低于他所选修课程平均成绩 5 分以上的课程号。（输出学号和课程号）
select cno, sno
from sc x
where grade + 5 < (select avg(grade)
from sc y
where y.sno = x.sno); 
--（6）查询比所有男生年龄都小的女生的学号、姓名和年龄。
select sno,sname,sage
from student x
where x.ssex='女' and x.sage < all(select sage
from student
where ssex='男'
);
--（7）查询所有选修了 2 号课程的学生姓名及所在系。
select sname,sdept
from student,sc
where sc.cno='2' and student.sno = sc.sno;
--（8）使用 update 语句把成绩为良的学生的年龄增加 2 岁，并查询出来。
update student
set sage = sage-2
where sno in(select sno
from sc
where 80 <= grade <= 90
);
select student.*
from student,sc
where 80 <= grade <=89 and student.sno = sc.sno;
--（9）使用 insert 语句增加两门课程：C 语言和人工智能，并查询出来
insert into course(cno,cname,cpno,ccredit)
values(8,'C语言',null,null);
insert into course(cno,cname,cpno,ccredit)
values(9,'人工智能',null,null);--不要把分号写成中文的就行
select courese.*
from course;
--（10）使用 delete 语句把人工智能课程删除，并查询出来。
delete from course
where cno=8 or cno=9;
select courese.*
from course;