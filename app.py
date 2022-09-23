from typing import Union
import uvicorn
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/auth")
def read_item():
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    return {"Hello": username, "Password": password}


if __name__ == "__main__":
    uvicorn.run(app, host = '0.0.0.0',port=8080)