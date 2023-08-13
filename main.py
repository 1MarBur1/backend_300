from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data.data import User, Point, Status_type, Event
from data.database import Database
from bot.bot import bot
from config import Config, load_config
from utils import get_user_points_level, get_user_appeals_level, get_user_cleaning_days_level, get_user_swaps
import uvicorn

config: Config = load_config()
base = Database(config.db.database)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#юзеры

@app.get('/users/{user_id}')
async def get_user(user_id: int) -> User:
    user = base.get_user(user_id)
    level_points, residue_points = get_user_points_level(user[3])
    level_appeals, residue_appeals = get_user_appeals_level(user[4])
    level_cleaning_days, residue_cleaning_days = get_user_cleaning_days_level(user[5])
    level_swaps, residue_swaps = get_user_swaps(user[5])
    return User(id=user[0], name=user[1], ex=user[2], level_points=level_points, residue_points=residue_points,
                level_appeals=level_appeals, residue_appeals=residue_appeals, level_cleaning_days=level_cleaning_days,
                residue_cleaning_days=residue_cleaning_days, level_swaps=level_swaps, residue_swaps=residue_swaps)

@app.post("/users/{user_id}/send_message")
async def send_message(user_id: int, message: str):
    try:
        message = 'У Вас новый ответ на обращение\n'+message
        await bot.send_message(chat_id=user_id, text=message)
        return {"message": "Event deleted successfully"}
    except:
        return {"message": "An error occurred while deleting the event"}


#поинты

@app.get('/points')
async def get_points() -> list[Point]:
    return [Point(id=point[0], name=point[1], description=point[2], location=point[3], type=point[4], photo=point[5],
                  reward=point[6], status=point[7], creator_id=point[8]) for point in base.get_points()]


@app.get("/points/{point_id}")
async def get_point(point_id) -> Point:
    point = base.get_point(point_id)
    return Point(id=point[0], name=point[1], description=point[2], location=point[3], type=point[4], photo=point[5],
                 reward=point[6], status=point[7], creator_id=point[8])


# @app.post("/add_point/")
# async def add_point(point: Point):
#     # base.add_point(point.name, point.description, point.location, point.type, point.photo, point.reward, point.status,
#     #                point.creator_id)

    #base.add_point('name', 'dd', 'loc', 'Грязь и мусор', 'fjvnv', 5, 'Решено',12345)
   # #     return {"message": "Point added successfully"}
    # except:
    #     return {"message": "An error occurred while adding the point"}

@app.post("/add_point/")
async def add_point(name, description, location, typee, photo, reward, status, creator_id):
    base.add_point(name, description, location, typee, photo, reward, status, creator_id)
    return {"message": "Point deleted successfully"}


@app.post("/delete_point/")
async def delete_point(point: Point):
    try:
        base.delete_point(point.id)
        return {"message": "Point deleted successfully"}
    except:
        return {"message": "An error occurred while deleting the point"}


@app.post("/update_point_status/")
async def update_point_status(point: Point, status: Status_type):
    try:
        base.update_point_status(point.id, status)
        return {"message": "Point status updated successfully"}
    except:
        return {"message": "An error occurred while updating the point status"}


#ивенты
@app.get('/events')  # работает
async def get_events() -> list[Event]:
    return [Event(id=event[0], name=event[1], description=event[2], datetime=event[3], location=event[4], type=event[5],
                  photo=event[6], reward=event[7]) for event in base.get_events()]


@app.get("/events/{event_id}")
async def get_event(event_id: int) -> Event:
    event = base.get_event(event_id)
    return Event(id=event[0], name=event[1], description=event[2], datetime=event[3], location=event[4], type=event[5],
                 photo=event[6], reward=event[7])


@app.post("/add_event/")
async def add_event(event: Event):
    try:
        base.add_event(event.name, event.description, event.datetime, event.location, event.type, event.photo, event.reward)
        return {"message": "Event added successfully"}
    except:
        return {"message": "An error occurred while adding the event"}


@app.post("/delete_event/")
async def delete_event(event: Event):
    try:
        base.delete_event(event.id)
        return {"message": "Event deleted successfully"}
    except:
        return {"message": "An error occurred while deleting the event"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    #print(base.get_point(1))
    #base.add_point('name', 'dd', 'loc', 'Грязь и мусор', 'fjvnv', 5, 'Решено',12345)

