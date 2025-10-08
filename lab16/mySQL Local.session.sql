-- Create your own database (if not already created)
CREATE DATABASE IF NOT EXISTS mydb;

-- Switch to it
USE mydb;
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);
INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('Amit', 'Sharma', 'HR', 45000, '2020-05-20'),
('Priya', 'Patel', 'Finance', 60000, '2021-02-10'),
('Ravi', 'Kumar', 'IT', 55000, '2019-08-14'),
('Neha', 'Reddy', 'Marketing', 48000, '2022-01-05'),
('Arjun', 'Singh', 'IT', 62000, '2020-09-12');

SELECT * FROM employees;
SELECT first_name, last_name, department FROM employees;
SELECT DISTINCT department FROM employees;
SELECT * FROM employees WHERE salary > 50000;
SELECT * 
FROM Employees
WHERE Department = 'IT';

SELECT * 
FROM Employees
WHERE Hire_date > '2020-12-31';

SELECT * 
FROM Employees
ORDER BY Salary ASC;

SELECT * 
FROM Employees
ORDER BY Salary DESC
LIMIT 3;

SELECT COUNT(*) AS TotalEmployees
FROM Employees;

SELECT AVG(Salary) AS AverageSalary
FROM Employees;

SELECT MAX(Salary) AS HighestSalary, 
       MIN(Salary) AS LowestSalary
FROM Employees;

SELECT Department, SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY Department;

SELECT Department, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 1;

SELECT Department, AVG(Salary) AS AverageSalary
FROM Employees
GROUP BY Department;

SELECT YEAR(Hire_date) AS HireYear, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY YEAR(Hire_date);

-- Drop the Department table if it exists
DROP TABLE IF EXISTS department;

CREATE TABLE Department (
    dept_id INT,
    dept_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO Department (dept_id, dept_name, location) VALUES
(1, 'HR', 'Hyderabad'),
(2, 'Finance', 'Mumbai'),
(3, 'IT', 'Bangalore'),
(4, 'Marketing', 'Chennai'),
(5, 'Operations', 'Delhi');

SELECT e.first_name, e.last_name, e.department, d.location
FROM Employees e
LEFT JOIN Department d ON e.department = d.dept_name;

SELECT e.first_name, e.last_name
FROM Employees e
JOIN Department d ON e.department = d.dept_name
WHERE d.location = 'Bangalore';

SELECT e.first_name, e.last_name, e.department, d.location
FROM Employees e
LEFT JOIN Department d ON e.department = d.dept_name;

SELECT d.dept_name
FROM Department d
LEFT JOIN Employees e ON e.department = d.dept_name
WHERE e.department IS NULL;

SELECT e.department, COUNT(*) AS employee_count
FROM Employees e
GROUP BY e.department;

SELECT first_name, last_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);

SELECT e.department, AVG(e.salary) AS avg_salary
FROM Employees e
GROUP BY e.department
ORDER BY avg_salary DESC
LIMIT 1;

SELECT first_name, last_name, hire_date
FROM Employees
ORDER BY hire_date DESC
LIMIT 1;

SELECT first_name, last_name, salary
FROM Employees
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees
    WHERE salary < (SELECT MAX(salary) FROM Employees)
);

UPDATE Employees
SET salary = salary * 1.10
WHERE department = 'IT';

UPDATE Employees
SET department = 'Marketing'
WHERE first_name = 'Ravi';

UPDATE Employees
SET department = 'Marketing'
WHERE first_name = 'Ravi';

DELETE FROM Employees
WHERE salary < 40000;

ALTER TABLE Employees
ADD COLUMN email VARCHAR(100);

UPDATE Employees
SET email = CONCAT(LOWER(first_name), '.', LOWER(last_name), '@company.com');

SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 2;

SELECT d.location, COUNT(e.first_name) AS employee_count
FROM Employees e
JOIN Department d ON e.department = d.dept_name
GROUP BY d.location;

SELECT COUNT(*) AS employee_count, SUM(salary) AS total_salary
FROM Employees;

SELECT first_name, last_name
FROM Employees
WHERE first_name LIKE 'A%';

SELECT first_name, last_name
FROM Employees
WHERE last_name LIKE '%a';

SELECT first_name, last_name, hire_date
FROM Employees
WHERE YEAR(hire_date) = 2020;

SELECT first_name, last_name, DATEDIFF(CURDATE(), hire_date) AS days_since_hired
FROM Employees;

SELECT UPPER(CONCAT(first_name, ' ', last_name)) AS full_name
FROM Employees;

SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM Employees;

SELECT first_name, last_name, salary
FROM Employees
WHERE salary BETWEEN 45000 AND 60000;

CREATE VIEW High_Salary_Employees AS
SELECT first_name, last_name, salary, department
FROM Employees
WHERE salary > 55000;

SELECT * FROM High_Salary_Employees;

ALTER TABLE Employees
MODIFY department VARCHAR(50) NOT NULL;

DROP VIEW IF EXISTS High_Salary_Employees;

RENAME TABLE Employees TO Staff;

CREATE TABLE Employees_backup AS
SELECT * FROM Employees;

TRUNCATE TABLE Employees;

DROP TABLE IF EXISTS Employees_backup;

CREATE INDEX idx_last_name ON Employees(last_name);

DROP INDEX idx_last_name ON Employees;
