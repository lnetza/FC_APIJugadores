from fastapi import FastAPI
from typing import List
from model import Jugadores
from data import niveles,equipos

app = FastAPI()



@app.post("/jugadores/")
async def pagos(jugadores: List[Jugadores]):
    
    
    for item in jugadores:
        print(item)

             
    return {"Jugadores": jugadores}