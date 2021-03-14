from pydantic import BaseModel
from typing import Optional


class Jugadores(BaseModel):
    nombre: str
    nivel: str
    goles: int
    sueldo: float
    bono: float
    sueldo_completo: Optional[float] = None
    equipo: str 