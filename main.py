from fastapi import FastAPI
from data.data import User, Point, Status_type
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
    return [Point(id=point[0], name=point[1], description=point[2], location=point[3], type=point[4], photo=point[5], reward=point[6], status=point[7]) for point in base.get_points()]

@app.get("/points/{point_id}")
async def get_point(point_id) -> Point:
    point = base.get_point(point_id)
    return Point(id=point[0], name=point[1], description=point[2], location=point[3], type=point[4], photo=point[5], reward=point[6], status=point[7])


@app.post("/add_point/")
def add_point(point: Point):
    try:
        base.add_point(point.name, point.description, point.location, point.type, point.photo, point.reward)
        return {"message": "Point added successfully"}
    except:
        return {"message": "An error occurred while adding the point"}

@app.post("/delete_point/")
def delete_point(point: Point):
    try:
        base.delete_point(point.id)
        return {"message": "Point deleted successfully"}
    except:
        return {"message": "An error occurred while deleting the point"}

@app.post("/update_point_status/")
def update_point_status(point: Point, status: Status_type):
    try:
        base.update_point_status(point.id, status)
        return {"message": "Point status updated successfully"}
    except:
        return {"message": "An error occurred while updating the point status"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    #print(base.get_user(3))
    #base.update_point_status(4, 'В процессе')
    #...