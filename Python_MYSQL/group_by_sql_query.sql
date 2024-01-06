select count(eid), state
from employee
group by state;

-- group by with join clause 
select courses.cname, count(employee.eid) as
noOfEmployee from employee
right join courses on employee.cid = courses.cid
group by courses.cname;