"""
Cit Horas Disponibles v4, esquemas de pydantic
"""
from datetime import time

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class CitHoraDisponibleOut(BaseModel):
    """Esquema para entregar horas disponibles"""

    horas_minutos: time


class OneCitHoraDisponibleOut(CitHoraDisponibleOut, OneBaseOut):
    """Esquema para entregar un hora disponible"""
