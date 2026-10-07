import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cur = con.cursor()

sql = "DELETE FROM students WHERE id=%s"
data = (1,)

cur.execute(sql, data)
con.commit()

print("Record deleted successfully.")

con.close()