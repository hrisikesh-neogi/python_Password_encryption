from typing import Union
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/auth/{password}")
def read_item(password: str):
    return {"password": password}


if __name__ == "__main__":
    uvicorn.run(app, debug=True)