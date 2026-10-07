import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cur = con.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS dbStudent")
cur.execute("USE dbStudent")

cur.execute("""
CREATE TABLE IF NOT EXISTS tblStudInfo (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    stream VARCHAR(30),
    college_name VARCHAR(100),
    contact_number VARCHAR(15),
    remarks VARCHAR(100)
)
""")

sql = """INSERT INTO tblStudInfo
(student_id, student_name, stream, college_name, contact_number, remarks)
VALUES (%s, %s, %s, %s, %s, %s)"""

data = (1, "Rahul", "BCA", "ABC College", "9876543210", "Good Student")

cur.execute(sql, data)
con.commit()

print("Database, table and student record created successfully.")

con.close()