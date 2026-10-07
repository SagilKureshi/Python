import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="dbStudent"
)

cur = con.cursor()

sql = "DELETE FROM tblStudInfo WHERE student_id=%s"
data = (1,)

cur.execute(sql, data)
con.commit()

print("Student information deleted successfully.")

con.close()