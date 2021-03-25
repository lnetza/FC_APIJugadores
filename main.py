from fastapi import FastAPI
from typing import List
from model import *
from data import niveles
from helpers import *
import json
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI(title="Resuelve FC")


@app.post("/jugadores/")
async def pagos(jugadores: Jugadores):
    
    data = jsonable_encoder(jugadores.jugadores)

    totalGolesEquipo=goles_equipo(data)
    sueldo=sueldo_completo(data,totalGolesEquipo)
    
    return sueldo