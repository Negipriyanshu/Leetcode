# Write your MySQL query statement below
WITH count_email AS( 
SELECT email , COUNT(email) as duplicate FROM Person
GROUP BY email)

SELECT email FROM count_email
WHERE  duplicate > 1; 