select count(eid), state
from employee
group by state
having count(eid) >= 1
order by count(eid) asc;

select count(eid), state
from employee
group by state
having count(eid) >= 2;