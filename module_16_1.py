from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def welcome() -> str:
    return 'Главная страница'

@app.get("/user/admin")
async def admin_page() -> str:
    return 'Вы вошли как администратор'

@app.get("/user/{user_id}")
async def users_number(user_id: int) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user")
async def users_info(username: str, age: int) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
