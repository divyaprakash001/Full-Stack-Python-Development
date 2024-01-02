select * from employee where state like 'j%';
select * from employee where state like 'bi___';  -- _ wildcard anything in place of it
select * from employee where state like '%h%';  -- % wildcard  means contain h in state
select * from employee where state like 'Bi%';  -- % wildcard  means start with Bi in state
select * from employee where state like '%h%' or state like 'u%'; 
select * from employee where state like '%sh';  -- %sh means ends with sh
select * from employee where state like 'b%r';  -- %sh means start with b and ends with r
select * from employee where state like '%kh%';  -- %sh means start with b and ends with r
--  combine wildcard
select * from employee where state like 'jh_%';
-- without wildcard
select * from employee where state like 'bihar'; 


