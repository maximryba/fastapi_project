from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column



DATABASE_URL = "postgresql+asyncpg://postgres:root@localhost:5432/postgres"

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)



new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]

    description: Mapped[str | None]

async def create_tables():
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Model.metadata.create_all)
        except Exception as e:
            print(f"Ошибка подключения: {e}")
