from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from settings import settings

engine = create_async_engine(settings.DATABASE_URI, echo=False)

async_session = async_sessionmaker(bind=engine, autocommit=False, autoflush=False, class_=AsyncSession)


async def get_session():
    async with async_session() as session:
        try:
            yield session
        except SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.close()
