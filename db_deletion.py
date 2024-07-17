import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="sysTeM@67WeK")

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE user_login_credentials")