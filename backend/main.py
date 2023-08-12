from fastapi import FastAPI
from data.data import User, Point
from data.database import Database
from config import Config, load_config
from utils import get_user_status
import uvicorn

config: Config = load_config()

base = Database(config.db.database)
app = FastAPI()

@app.get('/users/{user_id}')
async def get_user(user_id):
    user = base.get_user(user_id)
    return {'id': user[0],
            "name": user[1],
            'ex': user[2],
            'status': get_user_status(user[2])
            }

@app.get('/points') #работает
async def get_points():
    return [{'id': point[0], 'name': point[1], 'description': point[3], 'location': point[4], 'link': point[5], 'reward': point[6]} for point in base.get_points()]

@app.post("/add_point/")
def add_point(point: Point):
    try:
        base.add_point(point.name, point.description, point.location, point.type, point.photo, point.reward)
        return {"message": "Point added successfully"}
    except:
        return {"message": "An error occurred while adding the point"}

if __name__ == "__main__":
    #uvicorn.run(app, host="0.0.0.0", port=8000)
    #print(base.get_user(3))
    #base.add_point('прикол! насрали голуби)))', 'прям на стекло... только вчера окна вымыла!!! твари!', '45.64258, 87.53168', 'Разлив нефти', 'https://static.tildacdn.com/tild6665-6130-4161-b766-366665316330/6.jpeg', 15)
    ...