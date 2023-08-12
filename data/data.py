from pydantic import BaseModel
from datetime import datetime, time
from enum import Enum


class Point_type(Enum):
    shit = 'Грязь и мусор'
    tires = 'Свалка шин'
    dumpsters = 'Переполненные контейнеры'
    petrol = 'Разлив нефти'
    blawn = 'Парковка на газонах'
    commerce = 'Несанкционированная торговля'
    improvement = 'Нарушение благоустройства'


class Point(BaseModel):
    id: int
    name: str
    description: str
    location: str
    type: Point_type
    photo: str
    reward: float


class User(BaseModel):
    id: int
    name: str
    ex: int