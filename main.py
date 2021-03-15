from fastapi import FastAPI
from typing import List
from model import Jugadores
from data import niveles
from helpers import *

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.post("/jugadores/")
async def pagos(jugadores: List[Jugadores]):
    
    data = jsonable_encoder(jugadores)
    
    totalGolesEquipo=goles_equipo(data)
    sueldo=sueldo_completo(data,totalGolesEquipo)
    
    return sueldo
