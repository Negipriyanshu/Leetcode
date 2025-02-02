# Write your MySQL query statement below
SELECT max(salary) as SecondHighestSalary FROM Employee WHERE salary < (select MAX(salary) from Employee);