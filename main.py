from fastapi import FastAPI
from random import randint

app = FastAPI()


@app.get("/")
async def root():
    return 2


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/random")
async def random():
    return randint(1,1000)