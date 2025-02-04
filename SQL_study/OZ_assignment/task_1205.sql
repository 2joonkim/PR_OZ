-- SELECT * FROM products

-- 문제 1 
-- INSERT INTO users(first_name, last_name, email, password, address, contact, gender, is_active, is_staff)
-- VALUES 
-- ('John', 'Doe', 'john.doe@example.com', 'password123', '123 Main St, Cityville', '010-1234-5678', 'Male', TRUE, FALSE),
-- ('Jane', 'Smith', 'jane.smith@example.com', 'password123', '456 Oak St, Townsville', '010-2345-6789', 'Female', TRUE, FALSE),
-- ('Michael', 'Johnson', 'michael.johnson@example.com', 'password123', '789 Pine St, Villagetown', '010-3456-7890', 'Male', TRUE, TRUE),
-- ('Emily', 'Davis', 'emily.davis@example.com', 'password123', '321 Birch St, Hamletburg', '010-4567-8901', 'Female', TRUE, FALSE),
-- ('David', 'Martinez', 'david.martinez@example.com', 'password123', '654 Cedar St, Crossroads', '010-5678-9012', 'Male', TRUE, FALSE),
-- ('Sophia', 'Brown', 'sophia.brown@example.com', 'password123', '987 Elm St, Greenfield', '010-6789-0123', 'Female', TRUE, TRUE),
-- ('James', 'Wilson', 'james.wilson@example.com', 'password123', '741 Maple St, Riverside', '010-7890-1234', 'Male', TRUE, FALSE),
-- ('Olivia', 'Taylor', 'olivia.taylor@example.com', 'password123', '852 Redwood St, Lakeside', '010-8901-2345', 'Female', TRUE, FALSE),
-- ('William', 'Anderson', 'william.anderson@example.com', 'password123', '963 Willow St, Seaview', '010-9012-3456', 'Male', TRUE, TRUE),
-- ('Ava', 'Thomas', 'ava.thomas@example.com', 'password123', '159 Cedar St, Hilltop', '010-0123-4567', 'Female', TRUE, FALSE);

-- 문제 2 
-- INSERT INTO stocks(raw_material_id, pre_quantity, quantity, change_type, store_id, create_at)
-- VALUES
-- (1, 100, 120, '1', 3, '2024-12-01 09:00:00'),  
-- (2, 80, 70, '2', 4, '2024-12-01 10:00:00'),  
-- (3, 50, 70, '3', 2, '2024-12-01 11:00:00'),  
-- (4, 40, 50, '1', 1, '2024-12-02 09:30:00'),  
-- (1, 120, 100, '2', 5, '2024-12-02 10:00:00'),  
-- (2, 70, 90, '4', 2, '2024-12-02 10:30:00'),  
-- (3, 70, 60, '1', 1, '2024-12-03 11:00:00'),  
-- (4, 50, 40, '2', 4, '2024-12-03 11:30:00'),  
-- (1, 100, 120, '3', 2, '2024-12-04 12:00:00'),
-- (2, 90, 80, '1', 1, '2024-12-04 13:00:00');

-- 문제 3
-- INSERT INTO sales_records(user_id, store_id, is_refund, created_at)
-- VALUES
-- ('2', '3', TRUE,'2024-12-04 00:00:00');

-- INSERT INTO sales_items(sales_record_id, product_id, quantity, created_at)
-- VALUES
-- ('1', '2', '30','2024-12-04 00:00:00');

-- 문제 4
-- INSERT INTO products(name, description, price)
-- VALUES
-- ('buldak bun', 'bun meet the bul-dak ramen!', 6.00);

-- 문제 5
-- SELECT * FROM stores
-- SELECT * FROM employees
-- SELECT * FROM users

-- INSERT INTO stores (name, address, contact, is_active)
-- VALUES
-- ("Karina's Bakery", '123 Main Street, Springfield', '555-678-9012',TRUE),
-- ('Ocean Breeze Cafe','456 Coastal Avenue, Miami Beach','555-234-5678',TRUE);

-- INSERT INTO employees(code, type, user_id, store_id, is_active)
-- VALUES
-- (5,1,'1',5,TRUE),
-- (7,2,'2',7,TRUE);

-- UPDATE users
-- SET is_staff = TRUE
-- WHERE id = 1;

-- UPDATE users
-- SET is_staff = TRUE
-- WHERE id = 2;









