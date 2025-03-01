from fastapi import FastAPI
from app.api.users.router import users_router
from app.api.addresses.router import addresses_router
from app.items import items_router
from app.db.database import engine
from app.db import models

app = FastAPI(title='My App')

fruits = [{'id': 1, 'name': 'banana'}, {'id': 2, 'name': 'apple'}]


@app.get('/hello')
def hello_world():
    return {'message': 'Hello World'}


# Поиск по query параметру
@app.get('/fruits')
async def get_fruit_by_name(fruit_name: str):
    for fruit in fruits:
        if fruit['name'] == fruit_name:
            return fruit

    return None


# Поиск по path параметру
@app.get('/fruits/{fruit_id}')
def get_fruit(fruit_id: int):
    for fruit in fruits:
        if fruit['id'] == fruit_id:
            return fruit

    return None


app.include_router(items_router, tags=['Items'])
app.include_router(users_router, tags=['Users'])
app.include_router(addresses_router, tags=['Addresses'])


# Эта часть кода применяет миграции после старта приложения, так как используется БД находится в оперативной памяти
@app.on_event('startup')
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
