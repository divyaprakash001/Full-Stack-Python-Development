select sum(eid) from employee;
select sum(eid) from employee where eid <= 10;
select sum(eid) from employee as tsum where eid <= 10;
select sum(eid*10) from employee  where eid <= 10;
-- select sum(eid * eid) from employee left join employee on employee.eid = employee.eid;  -- need some clarification
