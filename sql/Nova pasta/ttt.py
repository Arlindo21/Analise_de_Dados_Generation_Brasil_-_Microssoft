import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="4524",
    database="sales_db"
)

print("Conectado com sucesso!")