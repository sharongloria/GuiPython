import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="company"
)

my_cursor = my_db.cursor()
# my_cursor.execute("CREATE DATABASE company")
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)
#my_cursor.execute("CREATE TABLE employees(name varchar(55), age int, email varchar(55), salary int)")
my_cursor.execute("ALTER TABLE employees ADD COLUMN id int auto_increment primary key")
