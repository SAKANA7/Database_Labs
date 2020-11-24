--(1) 创建 CS 系的视图 CS_View
create view CS_View
as
select sno, sname, ssex, sage, scholarship
from student
where sdept = 'CS';
--(2) 在视图 CS_View 上查询 CS 系选修了 1 号课程的学生
select CS_View.sno, sname, ssex, sage, scholarship
from CS_View, sc
where CS_View.sno = sc.sno and sc.cno = '1';
--(3) 创建 IS 系成绩大于 80 的学生的视图 IS_View
create view IS_View
as
select distinct student.sno, sname, ssex, sage, scholarship
from student, sc
where student.sno = sc.sno and grade > 80 and sdept = 'IS';
--(4) 在视图 IS_View 查询 IS 系成绩大于 80 的学生
select distinct IS_view.*
from IS_View, sc
where IS_View.sno = sc.sno and grade > 80;
--(5) 删除视图 IS_View
drop view is_view;
--(6) 利用可视化窗口创建 2 个不同的用户 U1 和 U2,利用系统管理员给 U1 授予 Student 表的
--查询和更新的权限，给 U2 对 SC 表授予插入的权限。
-- 然后用 U1 登录，分别:
-- 1）查询学生表的信息；
select student.*
from student;
-- 2）把所有学生的年龄增加 1 岁，然后查询；
update student
set sage = sage + 1;
select student.*
from student;
-- 3）删除 IS 系的学生；(提示不具备删除权限)
delete
from student
where sdept = 'IS';
select student.*
from student;
-- 4）查询 CS 系的选课信息。(提示不具备查询sc权限)
select sc.*
from student, sc
where student.sno = sc.sno and sdept = 'CS';
-- 用 U2 登录，分别:
-- 1）在 SC 表中插入 1 条记录（‘200215122’，‘1’，75）；
insert
into sc
values('200215122', '1', 75);
-- 2）查询 SC 表的信息;
select sc.*
from sc;
-- 3）查询视图 CS_View 的信息。
select cs_view.*
from cs_view;
-- (7) 用系统管理员登录，收回 U1 的所有权限
-- 我在navicat上删掉了
-- (8) 用 U1 登录，查询学生表的信息(连命令列界面都进不去了)
select student.*
from student;
-- (9) 用系统管理员登录
-- 登陆了
-- (10) 对 SC 表建立一个更新触发器，当更新了 SC 表的成绩时，如果更新后的成绩大于等于
-- 95，则检查该成绩的学生是否有奖学金，如果奖学金是“否”，则修改为“是”。如果修改后的
-- 成绩小于 95，则检查该学生的其他成绩是不是有大于 95 的，如果都没有，且修改前的成绩
-- 是大于 95 时，则把其奖学金修改为”否”。然后进行成绩修改，并进行验证是否触发器正确
-- 执行。1）首先把某个学生成绩修改为 98，查询其奖学金。2）再把刚才的成绩修改为 80，
-- 再查询其奖学金。

delimiter $$
CREATE TRIGGER upd_check AFTER UPDATE ON sc
FOR EACH ROW
BEGIN
declare c int;
set c=(select MAX(grade) from sc where sc.sno = NEW.sno);
IF NEW.grade>=95 THEN
update student set scholarship='是' where sno=NEW.sno;
ELSEIF OLD.grade>=95 THEN
update student set scholarship='否' where sno=NEW.sno AND c<95;
END IF;
END$$
delimiter ;

update sc
set grade = 96
where sno = 200215121 and cno = 1;

update sc
set grade = 92
where sno = 200215121 and cno = 1;




--（11）删除刚定义的触发器
drop trigger scho_dtct;
--（12）定义一个存储过程计算 CS 系的课程的平均成绩和最高成绩，在查询分析器或查询编
--辑器中执行存储过程，查看结果。
DELIMITER $$ CREATE PROCEDURE calc_grd() BEGIN
SELECT Cno,
    AVG(Grade),
    MAX(Grade)
FROM SC
WHERE Sno IN (
        SELECT Sno
        FROM Student
        WHERE Sdept = 'CS'
    )
GROUP BY Cno;
END $$;
--（13）定义一个带学号为参数的查看某个学号的所有课程的成绩，查询结果要包含学生姓
--名。进行验证。
DELIMITER $$
CREATE PROCEDURE query_grd(IN no_in char(9))
BEGIN
    SELECT Student.Sname, SC.Cno, SC.Grade
    FROM Student, SC
    WHERE Student.Sno = no_in AND SC.Sno = no_in;
END$$
DELIMITER ;
set @no_in = '200215121';
CALL query_grd(@no_in);
--（14）把上一题改成函数。再进行验证。
-- 未能实现，参考的同学的
create table temp
 (Sno char(9),
Sname char(20),
Cno char(4),
Grade smallint
 );
delimiter $$
create function fun_score(inputsno  char(9))returns int
DETERMINISTIC
begin
declare x int default 0;
declare done int default false;
declare v_Sno CHAR(9);
declare v_Sname char(20);
declare v_Cno char(4);
declare v_Grade smallint;
declare tmp_cursor cursor for select student.Sno,Sname,Cno,Grade
from student,sc
where student.Sno=sc.Sno AND student.Sno=inputsno;
declare continue HANDLER for not found set done = true;
open tmp_cursor;
real_loop:loop
	fetch tmp_cursor into  v_Sno,v_Sname,v_Cno,v_Grade;
	if done
	then leave real_loop;
    end if;
	insert into temp(Sno,Sname,Cno,Grade) values(v_Sno,v_Sname,v_Cno,v_Grade);
end loop;
close tmp_cursor;
return x;
end;$$
select fun_score('200215121');
select *
from temp;
--（15）在 SC 表上定义一个完整性约束，要求成绩再 0-100 之间。定义约束前，先把某个学
--生的成绩修改成 120，进行查询，再修改回来。定义约束后，再把该学生成绩修改为 120，
--然后进行查询。
ALTER TABLE SC
ADD CONSTRAINT CK_GRADE check(Grade BETWEEN 0 AND 100);