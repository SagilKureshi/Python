import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="dbStudent"
)

cur = con.cursor()

sql = """UPDATE tblStudInfo
         SET student_name=%s, stream=%s, remarks=%s
         WHERE student_id=%s"""

data = ("Amit", "BCA", "Excellent Student", 1)

cur.execute(sql, data)
con.commit()

print("Student information updated successfully.")

con.close()