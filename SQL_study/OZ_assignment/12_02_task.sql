
-- INSERT INTO employees (employees_name, employees_position, employees_salary) VALUES
--  ('혜린', 'PM', 90000)
--  ('은우', 'Frontend', 80000),
-- 	('가을', 'Backend', 92000),
-- 	('지수', 'Frontend', 78000),
-- 	('민혁', 'Frontend', 96000),
-- 	('하온', 'Backend', 130000

-- SELECT * FROM employees;

-- SELECT employees_name, employees_salary FROM employees WHERE employees_position = 'Frontend' AND employees_salary <= 90000;

-- SET SQL_SAFE_UPDATES = 0;

-- UPDATE employees SET employees_salary = employees_salary * 1.10 WHERE employees_position = 'PM';

-- UPDATE employees SET employees_salary = employees_salary * 1.05 WHERE employees_position = 'Backend';

-- SELECT employees_position, AVG(employees_salary) AS average_employees_salary FROM employees GROUP BY employees_position;
    