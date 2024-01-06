use divya;
show tables;
select * from employee;
select * from user;
select * from courses;
-- ALTER TABLE employee ADD cid int; -- to add new column on employee table 
-- inner join 
select employee.eid, employee.ename, employee.post, employee.gender,employee.state, employee.address , user.phone from employee inner join user on employee.eid = user.userId;

-- inner join employee with courses 
select employee.eid, employee.ename, employee.post, employee.gender,employee.state, employee.address ,
courses.cname,courses.cdesc, courses.cfee from employee inner join courses on employee.cid = courses.cid;

-- inner join and join show same result  
select employee.eid, employee.ename, employee.post, employee.gender,employee.state, employee.address ,
courses.cname,courses.cdesc, courses.cfee from employee join courses on employee.cid = courses.cid;

-- inner join three tables 
select employee.eid, employee.ename, employee.post, employee.gender,employee.state, employee.address , user.phone,
courses.cname,courses.cdesc, courses.cfee 
from ((employee
inner join user on employee.eid = user.userId)
inner join courses on employee.cid = courses.cid);

-- left join -- if right table have unmatch value , show full left and right even unmatched column
select employee.eid, employee.ename, courses.cname
from employee
left join courses on employee.cid = courses.cid;

-- right join
select courses.cid, courses.cname, employee.eid, employee.ename
from courses
right join employee
on courses.cid = employee.cid;

-- full outer join  or full join  --> returns all records when there is a match in left and right table
select employee.eid, employee.ename, courses.cname
from employee
full join courses on
employee.cid = courses.cid;

-- self join  --need more clarification

