select * from employees;
select count(FIRST_NAME) from employees;
select avg(salary), count(department_id) from employees where DEPARTMENT_ID='90';
select count(JOB_ID), JOB_ID from employees  group by employees.JOB_ID;
select first_name, last_name, department_id from employees;
select first_name, Last_name, JOB_ID, DEPARTMENT_NAME 
from departments 
inner join employees 
on departments.DEPARTMENT_ID = employees.DEPARTMENT_ID 
inner join locations 
on departments.LOCATION_ID=locations.LOCATION_ID 
where city='London';
