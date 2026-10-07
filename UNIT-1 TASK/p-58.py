import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cur = con.cursor()

sql = "INSERT INTO students (id, name, course) VALUES (%s, %s, %s)"
data = (1, "Rahul", "BCA")

cur.execute(sql, data)
con.commit()

print("Record inserted successfully.")

con.close()