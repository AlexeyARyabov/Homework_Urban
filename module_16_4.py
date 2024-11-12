from typing import Annotated, List
from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel
import uvicorn


app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/users")
async def all_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')]
                       , age: Annotated[int, Path(ge=18, le=120, description='Enter age')])-> User:
    if not users:
        new_id = 1
    else:
        new_id = len(users) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}')
async  def update_user(user_id: Annotated[int, Path(ge=1)]
                       , username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')]
                       , age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> User:
    try:
        if users[user_id - 1]:
            users[user_id - 1] = User(id=user_id, username=username, age=age)
            return users[user_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def deleted_user(user_id: Annotated[int, Path(ge=1)]) -> User:
    try:
        print('step1')
        if users[user_id - 1].id == user_id:
            print('step2')
            return users.pop(user_id - 1)
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

