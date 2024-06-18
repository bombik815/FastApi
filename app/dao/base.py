from sqlalchemy import select, insert

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id):
        async with  async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)  # select * from any_models
            result = await session.execute(query)  # вернет ответ на запрос выше
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with  async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)  # select * from any_models
            result = await session.execute(query)  # вернет ответ на запрос выше
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with  async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)  # select * from any_models
            result = await session.execute(query)  # вернет ответ на запрос выше
            return result.mappings().all()  # вернет список всех записей

    @classmethod
    async def add(cls, **data):
        async with  async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
