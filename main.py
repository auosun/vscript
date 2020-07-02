from fastapi import FastAPI
# from pydantic import BaseModel
from userController import userController
import mysql

app = FastAPI()
uController = userController()

@app.get("/")
def read_root():
    return "一个简单的v2ray-api控制器"

@app.get("/create/all")
def create_all():
    return mysql.readconfig().get('error',str(uController.create_all_user()))

@app.get("/remove/all")
def remove_all():
    return mysql.readconfig().get('error',str(uController.remove_all_user()))

@app.get("/create/{email}")
def create_one(email:str=None):
    return mysql.readconfig().get('error',str(uController.create_one_user(email)))

@app.get("/remove/{email}")
def remove_one(email:str=None):
    return mysql.readconfig().get('error',str(uController.remove_one_user(email)))


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host='127.0.0.1',port=8000)


