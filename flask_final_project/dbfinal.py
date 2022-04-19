import sqlite3 as sql

conn = sql.connect('databasefinal.db')
print("Opened database successfully.")

conn.execute('CREATE TABLE products (productname TEXT,category TEXT,description TEXT,quantity NUMBER,checkdate DATETIME)')
print("Table created successfully.")
conn.close()