import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='0000', 
    database='db_test',  
    charset='utf8mb4'      
)

try:
    with connection.cursor() as cursor:
        sql = """
        INSERT INTO users (first_name, last_name, email, password, address, contact, gender, is_active, is_staff)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = ('8ki', 'joa', '8kijoa@aespa.com', '123456', 'seoul gangnam, sinsa station', '010-7777-7777', 1, True, False)
        cursor.execute(sql, data)
        connection.commit()
finally:
    connection.close()

try:
    with connection.cursor() as cursor:
        sql = """
        UPDATE users
        SET address = %s
        WHERE id = %s
        """
        data = ('seoul gangnamgu, gangnam station', 21)
        cursor.execute(sql, data)
        connection.commit()
finally:
    connection.close()
try:
    with connection.cursor() as cursor:
        sales_records_sql = """
        INSERT INTO sales_records (user_id, store_id, is_refund, created_at)
        VALUES (%s, %s, %s, %s), 
               (%s, %s, %s, %s), 
               (%s, %s, %s, %s)
        """
        sales_records_data = (
            21, 1, True, '2024-12-06 11:00:00',
            21, 1, True, '2024-12-06 11:00:01',
            21, 1, True, '2024-12-06 11:00:02'   
        )
        cursor.execute(sales_records_sql, sales_records_data)
        
        sales_items_sql = """
        INSERT INTO sales_items (sales_record_id, product_id, quantity, created_at)
        VALUES (%s, %s, %s, %s), 
               (%s, %s, %s, %s), 
               (%s, %s, %s, %s)
        """
        sales_items_data = (
            2, 2, 3, '2024-12-06 11:00:00',
            3, 3, 2, '2024-12-06 11:00:01',
            4, 5, 5, '2024-12-06 11:00:02'
        )
        cursor.execute(sales_items_sql, sales_items_data)
        connection.commit()
finally:
    connection.close()

try:
    with connection.cursor() as cursor:
        insert_sql = """
        INSERT INTO sales_records (user_id, store_id, is_refund, created_at)
        VALUES (%s, %s, %s, %s), 
               (%s, %s, %s, %s), 
               (%s, %s, %s, %s)
        """
        insert_data = (
            3, 1, True, '2024-12-06 11:00:29',
            6, 7, True, '2024-12-06 11:00:20',
            9, 2, True, '2024-12-06 11:00:31'
        )
        select_sql = "SELECT * FROM sales_records"
        cursor.execute(select_sql)
        
        rows = cursor.fetchall()
        for row in rows:
            print(row)

try:
    with connection.cursor() as cursor:
        
        insert_sql = """
        INSERT INTO stocks (raw_material_id, pre_quantity, quantity, change_type, store_id, create_at)
        VALUES
        (%s, %s, %s, %s, %s, %s),  
        (%s, %s, %s, %s, %s, %s),
        (%s, %s, %s, %s, %s, %s)
        """
        insert_data = (
            4, 50, 40, '2', 4, '2024-12-06 11:34:00',
            1, 100, 120, '3', 7, '2024-12-06 11:29:00', 
            2, 90, 80, '1', 7, '2024-12-06 11:31:00'
        )
        cursor.execute(insert_sql, insert_data)
        connection.commit()

        select_sql = """
        SELECT *
        FROM stocks
        ORDER BY create_at DESC
        LIMIT 1
        """
        cursor.execute(select_sql)

        latest_record = cursor.fetchone()
        print("최근 사용 이력:", latest_record)

finally:
    connection.close()

try:
    with connection.cursor() as cursor:
        
        select_sql = """
        SELECT products.name, sales_items.quantity, products.price, 
               sales_items.quantity * products.price AS total_price 
        FROM users
        JOIN sales_records ON sales_records.user_id = users.id
        JOIN sales_items ON sales_items.sales_record_id = sales_records.id
        JOIN products ON products.id = sales_items.product_id
        WHERE users.first_name = %s AND users.last_name = %s
        ORDER BY products.price DESC
        """
        user_name = ('8ki', 'joa')

        cursor.execute(select_sql, user_name)
finally:
    connection.close()