from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import User


async def get_users(db_session: AsyncSession):
    return (await db_session.execute(select(User))).scalars().all()


async def get_user(db_session: AsyncSession, user_id: int):
    return await db_session.scalar(select(User).where(User.id == user_id))


async def create_user(db_session: AsyncSession, name: str, fullname: str):
    await db_session.execute(insert(User).values(name=name, fullname=fullname))

    await db_session.commit()


async def get_user_addresses(db_session: AsyncSession, user_id: int):
    user = await db_session.get(User, user_id) 

    return await user.awaitable_attrs.addresses
