from fastapi import FastAPI
from typing import List
from model import Jugadores
from data import niveles,equipos
from helpers import goles_por_equipo,goles_individuales,calcular_bono,calcular_sueldo_completo,alcance_total,suma_goles_equipo,suma_goles_minimo_equipo

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()



@app.post("/jugadores/")
async def pagos(jugadores: List[Jugadores]):
    
    json_data = jsonable_encoder(jugadores)
    
    totalGolesEquipo=suma_goles_equipo(json_data)
    totalGolesMinimoPorEquipo=suma_goles_minimo_equipo(json_data)

    for item in json_data:
        nivel=item['nivel']
        minimo=niveles[nivel]
        bono=item['bono']
        sueldoFijo=item['sueldo']
        individual=goles_individuales(item['goles'],minimo)
        golesPorEquipo=goles_por_equipo(totalGolesEquipo,totalGolesMinimoPorEquipo)
        alcanceTotal=alcance_total(individual,golesPorEquipo)
        totalBono=calcular_bono(bono,alcanceTotal)
        sueldoTotal=calcular_sueldo_completo(sueldoFijo,totalBono)
        item['sueldo_completo']=sueldoTotal
        item.update({"goles_minimos": minimo})
        item.pop("nivel")
        
        

    return JSONResponse(content={"Jugadores":json_data})