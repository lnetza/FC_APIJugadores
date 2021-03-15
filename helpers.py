from data import niveles
from operator import itemgetter
from itertools import groupby
from fastapi.responses import JSONResponse

def validar_goles(goles):
    return 0 if goles<0 else goles

def goles_equipo(data):
    data.sort(key=itemgetter('equipo'))

    totalGolesPorEquipo = {}

    for equipo, elements in groupby(data, key=itemgetter('equipo')):

        sumaGolesMinimoEquipo = 0
        sumaGolesEquipo = 0
        totalGoles = 0
        for i in elements:

            equipo = i['equipo']
            nivel = i['nivel']
            minimo = niveles[nivel]
            sumaGolesMinimoEquipo += minimo
            sumaGolesEquipo += i['goles']
            totalGoles = (sumaGolesEquipo/sumaGolesMinimoEquipo)*100

        totalGolesPorEquipo[equipo] = totalGoles

    return totalGolesPorEquipo


def sueldo_completo(data, totalGolesEquipo):
    golesIndividuales = 0

    for i in data:
        equipo = i['equipo']
        nivel = i['nivel']
        goles = validar_goles(i['goles'])
        bono = i['bono']
        sueldo = i['sueldo']
        minimo = niveles[nivel]
        golesIndividuales = round((((((goles/minimo*100)+(totalGolesEquipo[equipo]))/2)/100)*bono)+sueldo, 2)
        i['sueldo_completo'] = golesIndividuales
        i.update({"goles_minimos": minimo})
        i.pop("nivel")

    return JSONResponse(content={"Jugadores": data})
