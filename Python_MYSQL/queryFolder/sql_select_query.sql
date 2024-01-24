show databases;
use divya;
show tables;
select * from employee;
select ename,post from employee;
select distinct  ename from employee;
select  count(ename) from employee;
select  count(distinct ename) from employee;
select * from employee where ename='Rubika';
select * from employee where eid != 3; -- not equal
select * from employee where eid <> 3; -- not equal
select * from employee where eid between 3 and 5;
select * from employee where address like 'patna%';
select * from employee where post like 'analyst%';
select * from employee where address in ('patna','boring road patna','anaith');
select * from employee where address in ('patna','boring road patna','anaith') order by address;
select * from employee where address in ('patna','boring road patna','anaith') order by state;
select * from employee where address in ('patna','boring road patna','anaith') order by state asc;
select * from employee where address in ('patna','boring road patna','anaith') order by state desc;
select * from employee where address in ('patna','boring road patna','anaith') order by state, ename;  -- order by multiple column
select * from employee where address in ('patna','boring road patna','anaith') order by state asc, ename desc;
select * from employee where state='bihar' and address='boring road patna';
select * from employee where state='jharkhand' and address='ranchi';
select * from employee where state='jharkhand' or address='ranchi';
select * from employee where state='jharkhand' and address like 'ranchi%';
select * from employee where state='jharkhand' or address like 'ranchi%';
select * from employee where state='jharkhand' and address like 'ranchi%' and gender='male';
select * from employee where state='jharkhand' and (address like 'ranchi%' or address like 'anaith%');
select * from employee where state='jharkhand' and address like 'ranchi%' or address like 'anaith%';
select * from employee where state='jharkhand' or state='bihar';
select * from employee where not state='jharkhand';
select * from employee where state not like 'jharkhand%';
select * from employee where eid not between 1 and 5;
select * from employee where state not in ('jharkhand','bihar');
select * from employee where not eid > 10;