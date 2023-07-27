import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Uic2023!'
)

cursor = database.cursor()
cursor.execute("CREATE DATABASE company")

print("Yay, database created.")

