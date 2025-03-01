from fastapi import APIRouter, Depends
from app.api.users.handlers import create_user, get_user, get_user_addresses, get_users

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.users.schemas import UserDTO
from app.db.database import get_session

users_router = APIRouter(prefix='/users')

@users_router.get('')
async def get_users_api(db_session: AsyncSession = Depends(get_session)):
    return await get_users(db_session)


@users_router.get('/short', response_model=list[UserDTO])
async def get_short_users_api(db_session: AsyncSession = Depends(get_session)):
    return await get_users(db_session)


@users_router.get('/{user_id}')
async def get_user_api(user_id: int, db_session: AsyncSession = Depends(get_session)):
    return await get_user(db_session, user_id)


@users_router.post('')
async def create_user_api(name: str, fullname: str, db_session: AsyncSession = Depends(get_session)):
    return await create_user(db_session, name, fullname)


@users_router.get('/{user_id}/addresses')
async def get_user_addresses_api(user_id: int, db_session: AsyncSession = Depends(get_session)):
    return await get_user_addresses(db_session, user_id)
