select min(ename) from employee;
select max(ename) from employee;
select min(ename) from employee where state= 'jharkhand';
select max(ename) from employee where state='jharkhand';
select min(eid) as minid from employee;  -- alias as column name