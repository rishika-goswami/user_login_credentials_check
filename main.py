from passlib.hash import pbkdf2_sha256
import hashlib
'''import db_connection

#db_connection.test()

with open('db_connection.py', 'r') as file:
    code = file.read()
    exec(code)

#def test():'''

import mysql.connector as mysql
from mysql.connector import connect, Error

try:
    #db is the connection object
    db = mysql.connect(host = "localhost", user = "root", passwd = "sysTeM@67WeK", database = "user_login_credentials")

    print("Connection was successful!")
    print('The user ' + db.user + ' is connected to the ' + db.database + ' database.')

    # catch exception and print error message
except Error as err:
    print('Error message: ' + err.msg)

cursor = db.cursor()

#Hardcoated entry of user data and hashed password
hash1 = hashlib.sha256('donald@ressler549!'.encode()).hexdigest()
hash2 = hashlib.sha256('oliver@harrington$778'.encode()).hexdigest()
hash3 = hashlib.sha256('ronan@astor67%90'.encode()).hexdigest()
hash4 = hashlib.sha256('colton@donavan*44@87'.encode()).hexdigest()

sql = "INSERT INTO user_detail (user_id, user_name, password) VALUES (%s, %s, %s)"
val = [
    (11111, "DonaldRessler", hash1),
    (13326,"OliverHarrington",hash2),
    (23118, "RonanAstor", hash3),
    (83624, "ColtonDonavan", hash4)
    ]
cursor.executemany(sql, val)
db.commit()
print(cursor.rowcount, "record inserted.")


query = 'SELECT user_id, user_name, password FROM user_detail'
cursor.execute(query)
result = cursor.fetchall()

username=[]
for i in result:
    username.append(i[1])

password=[]
for i in result:
    password.append(i[2])

flag=1
user=input('Enter your username:')

#print("Valid username!")
pwd=input('Enter your password:')
# generate new salt, and hash a password
hashed_pwd = hashlib.sha256(pwd.encode()).hexdigest()

for i in password:
    if hashed_pwd==i:
        print("User logged in successfully!")
        flag=0
        break             

if(flag) or user not in username:
    print("Unsucessful login attempt.\nPlease try again!")
    

# close the cursor and database connection
cursor.close()
db.close()