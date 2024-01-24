-- union operator  -- select only distinct data means no duplicate data
select ename from employee
union
select userName from user;

-- union all  -- select all data
select ename from employee
union all
select userName from user;
 
-- SELECT City, Country FROM Customers
-- WHERE Country='Germany'
-- UNION
-- SELECT City, Country FROM Suppliers
-- WHERE Country='Germany'
-- ORDER BY City;

