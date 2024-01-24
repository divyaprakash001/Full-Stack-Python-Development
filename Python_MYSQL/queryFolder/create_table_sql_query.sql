create table persons(
	pid int,
    fname varchar(20),
    lname varchar(20),
    city varchar(100),
    address varchar(200),
    primary key(pid)
);

show tables;
select * from persons;
select * from anotherperson;
insert into anotherperson values(12,'ddjs','3232ewe');

-- table using another table
create table anotherperson as 
select pid, fname
from persons; 

drop table anotherperson;  -- delete the table
truncate table anotherperson;  -- clear all data from table

alter table anotherperson
add email varchar(222);  -- add another column into the existing table

alter table anotherperson
drop column email; -- delete column from existing table

alter table anotherperson
rename column email to emailOfPer; 
