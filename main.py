from fastapi import FastAPI
from typing import List
from model import Jugadores
from data import niveles,equipos
from helpers import goles_por_equipo,goles_individuales,calcular_bono,calcular_sueldo_completo,alcance_total

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()



@app.post("/jugadores/")
async def pagos(jugadores: List[Jugadores]):
    
    
    json_data = jsonable_encoder(jugadores)
    totalGolesPorEquipo=0
    totalGolesMinimoPorEquipo=0
    
    for item in json_data:
        nivel=item['nivel']
        minimo=niveles[nivel]
        bono=item['bono']
        sueldoFijo=item['sueldo']
        totalGolesPorEquipo +=item['goles']
        totalGolesMinimoPorEquipo +=minimo
        individual=goles_individuales(item['goles'],minimo)
        golesPorEquipo=goles_por_equipo(totalGolesPorEquipo,totalGolesMinimoPorEquipo)
        alcanceTotal=alcance_total(individual,golesPorEquipo)
        totalBono=calcular_bono(bono,alcanceTotal)
        sueldoTotal=calcular_sueldo_completo(sueldoFijo,totalBono)
        item['sueldo_completo']=sueldoTotal
        item.update({"minimo": minimo})
        item.pop("nivel") 



    return JSONResponse(content={"Jugadores":json_data})