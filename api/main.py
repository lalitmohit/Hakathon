from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn
from database import *
from models import *

app=FastAPI()

origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post('/registration')
def registration(request_body:User):
    # return request_body
    sql = "INSERT INTO customers (name, email,mobile_number,password,active) VALUES (%s, %s,%s,%s,%s)"
    val = (request_body.name,request_body.email,request_body.mobile_number,request_body.password,True)
    mycursor.execute(sql, val)
    mydb.commit()
    
    return {'data':f"registration details {request_body.name}"}
    
@app.post('/login')
def login(request_body:User1):
    mycursor.execute("SELECT email,password,active FROM customers")
    myresult = mycursor.fetchall()
    y=True
    for x in myresult:
        if x[0]==request_body.email and x[1]==request_body.password:

            y=False
            sql = "UPDATE customers SET active = %s WHERE email = %s"
            val = (True, x[0])
            mycursor.execute(sql, val)
            mydb.commit()
            return "successfully login"
    if y:
        return "wrong email or password"
        
@app.post('/logout')
def logout(request_body:User2):
    mycursor.execute("SELECT email,active FROM customers")
    myresult = mycursor.fetchall()
    y=True
    for x in myresult:
        if x[0]==request_body.email:
            y=False
            sql = "UPDATE customers SET active = %s WHERE email = %s"
            val = (False, x[0])
            mycursor.execute(sql, val)
            mydb.commit()
            return "successfully logout"
    if y:
        return "wrong email or password"
          
@app.get('/indexbse')
def indexbse():
    mycursor.execute("SELECT * FROM bse")
    myresult = mycursor.fetchall()
    lists=[]
    print(lists)
    for i in myresult:
        lists.append(i)
    lists=lists[1:]   
    return {'data':lists}

@app.get('/indexnse')
def indexnse():
    mycursor.execute("SELECT * FROM nse")
    myresult = mycursor.fetchall()
    lists=[]
    print(lists)
    for i in myresult:
        lists.append(i)
    return {'data':lists}

@app.get('/Reliance')
def indexnse():
    mycursor.execute("SELECT * FROM Reliance")
    myresult = mycursor.fetchall()
    lists=[]
    # print(lists)
    for i in myresult:
        lists.append(i)
    return {'data':lists}

@app.get('/Ashok_Leyland')
def indexnse():
    mycursor.execute("SELECT * FROM ashoka")
    myresult = mycursor.fetchall()
    lists=[]
    print(lists)
    for i in myresult:
        lists.append(i)
    return {'data':lists}

@app.get('/Cipla')
def indexnse():
    mycursor.execute("SELECT * FROM Cipla")
    myresult = mycursor.fetchall()
    lists=[]
    print(lists)
    for i in myresult:
        lists.append(i)
    return {'data':lists}

@app.get('/Tata_Steel')
def indexnse():
    mycursor.execute("SELECT * FROM tata")
    myresult = mycursor.fetchall()
    lists=[]
    print(lists)
    for i in myresult:
        lists.append(i)
    return {'data':lists}

@app.get('/Eicher_Motors')
def indexnse():
    mycursor.execute("SELECT * FROM eicher")
    myresult = mycursor.fetchall()
    lists=[]
    print(lists)
    for i in myresult:
        lists.append(i)
    return {'data':lists}


 
