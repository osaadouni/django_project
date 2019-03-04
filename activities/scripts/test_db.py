import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                             database='old_timereg_db',
                             user='root',
                             password='UPT6over!')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", db_Info)
       
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to - ", record)

        sql = "SELECT * FROM activity"
        cursor.execute(sql)
        records = cursor.fetchall()
        print("Total number of rows in activities is - ", cursor.rowcount)
        print("Printing each row's column values i.e. activity record")
        for row in records:
            print(row)
        

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    # closing database connection
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
