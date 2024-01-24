-- select TOP 3 * from employee;  --mysql doesnot support this
select * from employee limit 3;  -- mysql query
select * from employee where state='bihar' limit 5;  -- mysql query
select * from employee where state='bihar' order by ename desc limit 5;  
-- select * from employee fetch first 3 rows only -- this is for oracle
-- select top 50 percent * from employee;  -- sql server and ms access
