select avg(eid) from employee;
select avg(eid) from employee where eid <= 10;
select avg(eid) as asvg from employee where eid <= 10;
select * from employee where eid > (select avg(eid) from employee where eid <= 10);
