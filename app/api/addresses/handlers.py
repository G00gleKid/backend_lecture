from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Address


async def create_address(db_session: AsyncSession, email: str, user_id: int):
    new_address = Address(
        email=email,
        user_id=user_id
    )

    db_session.add(new_address)

    await db_session.commit()
    await db_session.refresh(new_address)

    return new_address
