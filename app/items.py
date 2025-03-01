from fastapi import APIRouter

from app.schemas import Item, ShortItem

items_router = APIRouter(prefix='/items')

item = Item(name='Laptop', description='description', price=1000)



@items_router.post('')
def create_item(item: Item):
    return item


@items_router.get('', response_model=ShortItem)
def read_short_item():
    return item
