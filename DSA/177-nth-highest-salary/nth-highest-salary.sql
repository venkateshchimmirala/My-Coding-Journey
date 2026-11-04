CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
     select  salary  as 'getNthHighestSalary(N)'from (select salary,dense_rank() over(order by salary desc) as rnk from Employee)  as tmp where rnk=N limit 1

  );
END