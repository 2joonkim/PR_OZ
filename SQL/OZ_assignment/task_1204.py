import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '0000',
    db = 'airbnb',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    # 문제 1 
    # sql = "INSERT INTO Products(productName, price, stockQuantity) VALUES (%s, %s, %s)"
    # cursor.execute(sql, ('Python Book', 1000, 10) )
    # connection.commit()

    # 문제 2
    # cursor.execute("SELECT * FROM Products")
    # for book in cursor.fetchall():
    #     print(book)
    
    # 문제 3
    # sql = 'UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID= %s '
    # cursor.execute(sql, (1, 1))
    # connection.commit()

    # 문제 4
    # sql = "SELECT customerID, sum(totalAmount) FROM Orders GROUP BY customerID"
    # cursor.execute(sql)
    # datas = cursor.fetchall()
    # print(datas)

    # 문제 5
    # sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
    # cursor.execute(sql, ('update@update.com', 1))
    # connection.commit()
    #
    # 문제 6
    # sql = "DELETE FROM Orders WHERE orderID = %s"
    # cursor.execute(sql, (15))
    # connection.commit()

    # 문제 7 
    # sql = "SELECT * FROM Products WHERE productName LIKE %s"
    # cursor.execute(sql, ('%Book%'))
    # datas = cursor.fetchall()
    # for data in datas:
    #     print(data['productNAME'])
    
    # 문제 8
    # sql = "SELECT * FROM Orders WHERE customerID = %s"
    # cursor.execute(sql, (1))
    # datas = cursor.fetchall()

    # for data in datas:
    #     print(data)

    # 문제 9 
    sql = """
        SELECT customerID, COUNT(*) as orderCount 
        FROM Orders 
        GROUP BY customerID 
        ORDER BY orderCount DESC 
        LIMIT 1
        """
    cursor.execute(sql)
    top_customer = cursor.fetchone()
    print(f"Top Customer ID: {top_customer[0]}, Orders: {top_customer[1]}")

cursor.close