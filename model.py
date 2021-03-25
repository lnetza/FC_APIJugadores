from pydantic import BaseModel, HttpUrl
from typing import Optional
from typing import List, Optional, Set

class Jugador(BaseModel):
    nombre: str
    nivel: str
    goles: int
    sueldo: float
    bono: float
    sueldo_completo: Optional[float] = None
    equipo: str 

class Jugadores(BaseModel):
    jugadores: List[Jugador]


