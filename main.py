'''
Siguiendo los documentos de 'fast api' trata de crearte lo siguiente:
Entra a github.com, create una cuenta //  LISTO
En la página de GitHub, en tu perfil, create un "repositorio" nombralo "eigentask"
Hacerte un clon de ese repositorio en tu compu, y ahí create un servidor de fastapi básico,
con dos rutas. //
Una ruta que sea "/" a secas, y devuelva un JSON que sea {"hello": "world"} LISTO
Otra ruta que sea "/random" y que devuelva un número aleatorio LISTO
-- hay muchas cosas ahí que capaz no conoces, googlealas, son bastante básicas en el laburo de
programación y hay mucho texto online para hacerlo
-- la razón de la nomenclatura es que sea como una entrevista para entrar a eigen, y que tengas
código público tuyo, que muestre que al menos sabes algo
-- la página de documentación de fast api':
https://fastapi.tiangolo.com/tutorial/first-steps/
'''

from fastapi import FastAPI
from random import randint

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/random")
async def random():
    return randint(1,1000)
