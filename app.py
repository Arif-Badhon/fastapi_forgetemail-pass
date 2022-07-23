# from datetime import date
import re
from fastapi import FastAPI, HTTPException
import fastapi_mail
from database import user_collection, reset_code_collection
from model import *
import uuid



def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]

app =FastAPI()




@app.get("/test")
def test_function():
    return {
        "Text": "Working"
    }

@app.get("/test_data")
def test_data(email):
    return serializeList(user_collection.find({'email': email}))

@app.post("/forget-password")
def forget_password(request: ForgetPassword):
    #check if the user exist
    user = user_collection.find_one({"email": request.email})
    if not user:
        raise HTTPException(status_code=484, detail="user not found")
    
    #create reset code
    ResetCode = {
        "code": str(uuid.uuid1()),
        "email": request.email
    }
    #ResetCode.endtime = date.today().strftime('%d-%b-%Y')
    reset_code_collection.insert_one(dict(ResetCode))
    return ResetCode
