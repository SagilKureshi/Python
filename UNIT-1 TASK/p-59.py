import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cur = con.cursor()

sql = "UPDATE students SET name=%s, course=%s WHERE id=%s"
data = ("Amit", "BCA", 1)

cur.execute(sql, data)
con.commit()

print("Record updated successfully.")

con.close()