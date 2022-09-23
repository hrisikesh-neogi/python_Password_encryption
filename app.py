from typing import Union
from urllib import request
import uvicorn
import os
import os
from utils import Generate_encryption_key



from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/auth/get_ev_key")
def read_ev_key():
    key = os.environ.get("KEY")
    return {"key: ", key}


@app.get("/auth/encrypt")
def encrypt_password(username: str, password: str):
    
    key = Generate_encryption_key()
    encrypted_password = key.encrypt(password.encode())
    return {'username': username, 'password': encrypted_password}

@app.get("/auth/decrypt")
def decrypt_password(password: str):
    key = Generate_encryption_key()
    decrypted_password = key.decrypt(password).decode()
    return {"password": decrypted_password}

    
    
    
    
    


if __name__ == "__main__":
    uvicorn.run(app, host = '0.0.0.0',port=8080)