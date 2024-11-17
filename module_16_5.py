from typing import Annotated, List
from fastapi import FastAPI, Path, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import uvicorn

templates = Jinja2Templates(directory='templates')
app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/")
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request':request, 'users':users})

@app.get('/user/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request':request, 'user':users[user_id-1]})

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')]
                       , age: Annotated[int, Path(ge=18, le=120, description='Enter age')])-> User:
    if not users:
        new_id = 1
    else:
        max_id = 1
        for i in range(len(users)):
            if users[i].id > max_id:
                max_id = users[i].id
        new_id = max_id + 1
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
        for i in range(len(users)):
            if users[i].id == user_id:
                return users.pop(i)
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

