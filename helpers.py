
def goles_por_equipo(golesPorEquipo,golesMinimoPorEquipo):
    return (golesPorEquipo/golesMinimoPorEquipo)*100

def goles_individuales(goles,minimo):
    return 0 if goles<0 else (goles/minimo)*100

def alcance_total(porcentajeIndividual,porcentajePorEquipo):
    return ((porcentajeIndividual+porcentajePorEquipo)/2)/100

def calcular_bono(bono,alcanceTotal):
    return bono * alcanceTotal

def calcular_sueldo_completo(sueldoFijo,totalBono):
    return round(sueldoFijo+totalBono,2)