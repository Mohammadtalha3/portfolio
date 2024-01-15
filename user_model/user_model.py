import mysql.connector
import sys
from fastapi import Response
import string


class User_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(hostname='localhost', user='root',password='mysql',database='portfolio')
            self.con.autocommit=True
            self.mycursor=self.con.cursor(dictionary= True)

        except:
            print('connection to database is made')
            
        else:
            print('Your connection to database cannot  be made: ')

    
    def getall(self):
            return {'message':'This is api connection test'}
    
        



    

