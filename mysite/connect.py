import mysql.connector

conn = mysql.connector.connect(
  host="ibrahim00.mysql.pythonanywhere-services.com",
  user="ibrahim00",
  password="sqldatabase",
  database="ibrahim00$mysite"
)

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM score")

results = mycursor.fetchall()

for rows in results:
  print(rows)