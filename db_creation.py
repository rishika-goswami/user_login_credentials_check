import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="sysTeM@67WeK")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE user_login_credentials")

mydb = mysql.connector.connect(host="localhost", user="root", password="sysTeM@67WeK", database="user_login_credentials")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE user_detail (user_id INT NOT NULL, user_name TINYTEXT, password VARCHAR(150), PRIMARY KEY(user_id))")
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")