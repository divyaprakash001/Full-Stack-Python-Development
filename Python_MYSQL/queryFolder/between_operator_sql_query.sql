select * from employee where eid between 5 and 10;
select * from employee where eid not between 5 and 10;
select * from employee where eid between 5 and 10 and state in ('bihar','jharkhand');
select * from employee where state between 'bihar' and 'jharkhand' order by ename desc;
-- SELECT * FROM orders WHERE orderdate BETWEEN #07/01/1996# and #07/31/1996#; -- select between dates
-- SELECT * FROM Orders WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31'; -- select between dates