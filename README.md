# user_login_credentials_check
Python program accessing MYSQL database to check user login credentials.
Python program that creates a database and an appropriate table, enters 4 user login credential information (hard coded) into the table with hashed password. There are three python files:
i)db_creation.py creates the database and required table. 
ii)The main.py takes in user input of user id and password, hashes it and checks against the database containing the user id and hashed passwords. It returns if login attempt was successful or not.
iii)db_deletion.py drops the databse created for this program.
