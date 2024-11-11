from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def all_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')]
                      , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='23')])-> str:
    current_id = str(int(max(users, key=int))+1)
    info_user = f"Имя: {username}, возраст: {age}"
    users[current_id] = info_user
    return f'User {current_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async  def update_user(user_id: str, username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')]
                       , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='23')]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete('/user/{user_id}')
async def deleted_user(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"
