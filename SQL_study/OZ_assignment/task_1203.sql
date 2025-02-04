-- (1) customers 테이블에 새 고객 추가
-- INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, state, postalCode, country)

-- VALUES (1001, '홍길동', '홍', '길동', '010-1234-5678', '서울시 강남구 테헤란로 123', '서울', '서울', '12345', '대한민국');

-- (2) products 테이블에 새 제품 추가
-- INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
-- VALUES ('P   
-- ROD1001', '스마트폰', 'Smart Electronics', '1:1', '삼성전자', '최신 스마트폰', 100, 500000, 700000);

-- (3) employees 테이블에 새 직원 추가
-- INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
-- VALUES (1001, '김', '철수', 'x1234', 'kim@example.com', '1', 201, '영업사원');

-- (4) offices 테이블에 새 사무실 추가
-- INSERT INTO offices (officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory)
-- VALUES ('OF1001', '부산', '051-123-4567', '부산광역시 해운대구 마린시티 123', NULL, '부산', '대한민국', '61234', 'AP');

-- (5) orders 테이블에 새 주문 추가
-- INSERT INTO orders (orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber)
-- VALUES (1001, '2023-11-23', '2023-11-30', '2023-11-25', 'Shipped', '빠른 배송 요청', 1001);

-- (6) orderdetails 테이블에 주문 상세 정보 추가
-- INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach)
-- VALUES (1001, 'PROD1001', 2, 700000);

-- (7) payments 테이블에 지불 정보 추가
-- INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount)
-- VALUES (1001, 'CHECK1001', '2023-11-25', 1400000);

-- (8) productlines 테이블에 제품 라인 추가
-- INSERT INTO productlines (productLine, textDescription, HTMLDescription, image)
-- VALUES ('Fashion Accessories', '패션 액세서리', '<p>최신 패션 액세서리</p>', 'fashion_accessories.jpg');

-- (9) customers 테이블에 다른 지역의 고객 추가
-- INSERT INTO customers (customerNumber, customerName, ...)
-- VALUES (1002, 'John Doe', ...);  -- 미국 고객 추가

-- (10) products 테이블에 다른 카테고리의 제품 추가
-- INSERT INTO products (productCode, productName, ...)
-- VALUES ('PROD1002', '노트북', ...);  -- 컴퓨터 카테고리 제품 추가

-- (중급)
-- (1) INSERT INTO customers (customerName, contactName, address, city, country) 
-- VALUES 
--     ('홍길동', '홍길동', '서울시 강남구', '서울', '대한민국'),
--     ('김철수', '김철수', '부산시 해운대구', '부산', '대한민국'),
--     ('박영희', '박영희', '대전시 유성구', '대전', '대한민국');

-- (2) INSERT INTO products (productCode, productName, productLine, quantityInStock, buyPrice, price)
-- VALUES
--     ('PROD1001', '스마트폰', 'Electronics', 100, 500, 800),
--     ('PROD1002', '노트북', 'Electronics', 50, 800, 1200),
--     ('PROD1003', '태블릿', 'Electronics', 80, 300, 500);

-- (3) INSERT INTO employees (firstName, lastName, email, ...) 
-- VALUES
--     ('홍', '길동', 'hong@example.com', ...),
--     ('김', '철수', 'kim@example.com', ...),
--     ('박', '영희', 'park@example.com', ...);

-- (4) INSERT INTO orde-- rs (customerNumber, orderDate, ...) VALUES (1001, '2023-11-23', ...);
-- INSERT INTO orderdetails (orderNumber, productCode, quantity) VALUES (1001, 'PROD1001', 2), (1001, 'PROD1002', 3);

-- (5) INSERT INTO payments (customerNumber, paymentDate, amount) VALUES 
--     (1001, '2023-12-01', 1000),
--     (1002, '2023-12-01', 500);

-- (6) INSERT INTO customers (customerName, ...) VALUES ('홍길동', ...);
-- SET @newCustomerID = LAST_INSERT_ID(); -- 마지막으로 추가된 고객 ID 가져오기
-- INSERT INTO orders (customerNumber, ...) VALUES (@newCustomerID, ...);

-- (7) INSERT INTO employees (firstName, lastName, jobTitle, ...) VALUES ('홍', '길동', 'Sales Rep', ...);

-- (8) INSERT INTO products (productCode, productName, quantityInStock, ...) VALUES ('PROD1004', '신제품', 100, ...);

-- (9) INSERT INTO offices (officeCode, city, ...) VALUES ('US01', 'New York', ...);
-- INSERT INTO employees (officeCode, ...) VALUES ('US01', ...);

-- (10)INSERT INTO productlines (productLine, textDescription) VALUES ('NewProductLine', '신제품 라인');
-- INSERT INTO products (productCode, productName, productLine, ...) VALUES 
--     ('PROD2001', '신제품1', 'NewProductLine', ...),
--     ('PROD2002', '신제품2', 'NewProductLine', ...);
