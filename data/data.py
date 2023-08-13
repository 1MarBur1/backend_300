from pydantic import BaseModel
from datetime import datetime, time
from enum import Enum


# from utils import parse_organization

class Point_type(Enum):
    shit = 'Грязь и мусор'
    tires = 'Свалка шин'
    dumpsters = 'Переполненные контейнеры'
    petrol = 'Разлив нефти'
    blawn = 'Парковка на газонах'
    commerce = 'Несанкционированная торговля'
    improvement = 'Нарушение благоустройства'


class Status_type(Enum):
    not_watched = 'Не просмотрено'
    process = 'В процессе'
    done = 'Решено'


class Point(BaseModel):
    id: int
    name: str
    description: str
    location: str
    type: Point_type
    photo: str
    reward: int
    status: Status_type
    creator_id: int
    # organization: str|None - будет добавлено позже при получении доступа к API реестровой карты

class Event_type(Enum):
    swap = 'Своп'
    cleaning_day = 'Субботник'
    lecture = 'Лекция'
    festivales = 'Фестивали'
    master_classes = 'Мастер-классы'
    kvesti = 'Квесты'
    actions = 'Экологические акции'
    other = 'Другое'


class Event(BaseModel):
    id: int
    name: str
    description: str
    datetime: datetime
    location: str
    type: Event_type
    photo: str
    reward: int


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
