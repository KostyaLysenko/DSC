
select * from employees;
select first_name, last_name, salary, salary*0.15 from employees;
select sum(salary) from employees;
select max(salary), min(salary) from employees;
select avg(salary), count(first_name) from employees;