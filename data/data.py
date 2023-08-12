from pydantic import BaseModel
from datetime import datetime, time
from enum import Enum
#from utils import parse_organization

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
    reward: int
    #organization: str|None


class User(BaseModel):
    id: int
    name: str
    ex: int

    level_points: int
    residue_points: int

    level_appeals: int
    residue_appeals: int

    level_cleaning_days: int
    residue_cleaning_days: int

    level_swaps: int
    residue_swaps: int