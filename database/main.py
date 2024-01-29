import mysql.connector

conn= mysql.connector.connect(
    host='localhost',
    password='mysql',
    user='root',
    database= 'portfolio'
)

cursor= conn.cursor()

"""cursor.execute('CREATE DATABASE portfolio')

cursor.execute("USE portfolio")"""

user_details="""
CREATE TABLE  user_details(
id int auto_increment primary key,
name varchar(20),
email varchar(50),
address varchar(20),
ph_no varchar(20)
)


"""




cursor.execute(user_details)