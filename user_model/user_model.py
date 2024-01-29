import mysql.connector
import sys
from fastapi import Request
from starlette.responses import JSONResponse
import logging



class User_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host='localhost', user='root',password='mysql',database='portfolio')
            self.con.autocommit=True
            self.mycursor=self.con.cursor(dictionary= True)

        except:
            logging.error('connection to database  cannot be made')
            
        else:
            logging.info('Your connection to database  is made: ')  

    
    async def details_db(self,request: Request):
        form_data= await request.form()
        name= form_data.get('name')
        email= form_data.get('email')
        address= form_data.get('address')
        ph_no= form_data.get('ph_no')

        if name and email and address and ph_no:

            query="INSERT INTO user_details (name,email,address,ph_no) VALUES(%s,%s,%s,%s)"
            values= (name,email,address,ph_no)

            self.mycursor.execute(query,values)

            logging.info('Details successfully inserted nto database')
        else:
            logging.error({'error':'Could not insert data into database'})
    
    async def getall(self):

        query= "SELECT * FROM user_details"

        self.mycursor.execute(query)
        
        response=self.mycursor.fetchall()

        return response




        

        
    
        



    

