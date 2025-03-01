from pydantic import BaseModel


class CreateAddressDTO(BaseModel):
    email: str
    user_id: int
