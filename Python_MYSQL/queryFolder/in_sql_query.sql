select * from employee where state in ('bihar','madhya pradesh');
select * from employee where state not in ('bihar','madhya pradesh');
select * from employee where eid in (select eid from employee where eid > 10);
select * from employee where eid not in (select eid from employee where eid > 10);