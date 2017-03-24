SELECT CASE WHEN COUNT(1)>0 THEN a.salary ELSE null END AS SecondHighestSalary
FROM
(SELECT salary
FROM Employee
WHERE salary < ANY (SELECT salary FROM Employee)
ORDER BY salary DESC
)a
LIMIT 1
;
