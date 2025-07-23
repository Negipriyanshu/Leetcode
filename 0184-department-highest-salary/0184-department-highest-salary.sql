# Write your MySQL query statement below
select 
d.name as Department ,e.name as Employee ,e.salary as Salary
From Employee e 
JOIN Department d 
ON e.departmentId = d.id
where (e.salary,e.departmentId) IN 
(
SELECT max(salary),departmentId from Employee
group by departmentId
)


