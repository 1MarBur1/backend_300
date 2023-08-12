from fastapi import FastAPI
from data.data import User, Point
from data.database import Database
from config import Config, load_config
from utils import get_user_points_level, get_user_appeals_level, get_user_cleaning_days_level, get_user_swaps
import uvicorn

config: Config = load_config()
base = Database(config.db.database)
app = FastAPI()

@app.get('/users/{user_id}')
async def get_user(user_id) -> User:
    user = base.get_user(user_id)
    level_points, residue_points = get_user_points_level(user[3])
    level_appeals, residue_appeals = get_user_appeals_level(user[4])
    level_cleaning_days, residue_cleaning_days = get_user_cleaning_days_level(user[5])
    level_swaps, residue_swaps = get_user_swaps(user[5])
    return User(id=user[0], name=user[1], ex=user[2], level_points=level_points, residue_points=residue_points,
                level_appeals=level_appeals, residue_appeals=residue_appeals,level_cleaning_days=level_cleaning_days,
                residue_cleaning_days=residue_cleaning_days, level_swaps=level_swaps, residue_swaps=residue_swaps)

@app.get('/points') #работает
async def get_points() -> list[Point]:
    return [Point(id=point[0], name=point[1], description=point[2], location=point[3], type=point[4], photo=point[5], reward=point[6]) for point in base.get_points()]

@app.post("/add_point/")
def add_point(point: Point):
    try:
        base.add_point(point.name, point.description, point.location, point.type, point.photo, point.reward)
        return {"message": "Point added successfully"}
    except:
        return {"message": "An error occurred while adding the point"}

@app.get("/points/{point_id}")
async def get_point(point_id) -> Point:
    point = base.get_point(point_id)
    return Point(id=point[0], name=point[1], description=point[2], location=point[3], type=point[4], photo=point[5], reward=point[6])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    #print(base.get_user(3))
    #base.add_point('прикол! насрали голуби)))', 'прям на стекло... только вчера окна вымыла!!! твари!', '45.64258, 87.53168', 'Разлив нефти', 'https://static.tildacdn.com/tild6665-6130-4161-b766-366665316330/6.jpeg', 15)
    #...