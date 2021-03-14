from data import niveles

def goles_por_equipo(golesPorEquipo,golesMinimoPorEquipo):
    return (golesPorEquipo/golesMinimoPorEquipo)*100

def goles_individuales(goles,minimo):
    return 0 if goles<0 else (goles/minimo)*100

def alcance_total(porcentajeIndividual,porcentajePorEquipo):
    return (porcentajeIndividual+porcentajePorEquipo)/2

def calcular_bono(bono,alcanceTotal):
    return (alcanceTotal/100)*bono

def calcular_sueldo_completo(sueldoFijo,totalBono):
    return round(sueldoFijo+totalBono,2)

def suma_goles_equipo(data):
    sumaGolesPorEquipo=0
    for item in data:
        sumaGolesPorEquipo +=item['goles']
    return sumaGolesPorEquipo

def suma_goles_minimo_equipo(data):
    sumaGolesMinimoEquipo=0
    for item in data:
        nivel=item['nivel']
        minimo=niveles[nivel]
        sumaGolesMinimoEquipo +=minimo
    return sumaGolesMinimoEquipo

