from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return { 'hello': 'world' }

@app.get('/persons/{person_id}')
def readItem(
        person_id: int, 
        age: Union[int, None] = None, 
        nation: Union[str, None] = None
    ):
    return { 
        "person_id": person_id, 
        "age": age, 
        "nation": nation 
    }

@app.get('/helth-check')
def getString():
    return "200 success"