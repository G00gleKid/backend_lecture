from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: int

class ShortItem(BaseModel):
    name: str
    price: int
