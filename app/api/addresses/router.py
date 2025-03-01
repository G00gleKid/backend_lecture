from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.addresses.handlers import create_address
from app.api.addresses.schemas import CreateAddressDTO
from app.db.database import get_session


addresses_router = APIRouter(prefix='/addresses')


@addresses_router.post('')
async def create_address_api(new_address: CreateAddressDTO, db_session: AsyncSession = Depends(get_session)):
    await create_address(db_session, **dict(new_address))
