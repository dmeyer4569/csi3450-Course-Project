from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker



# sqlalchemy engine
def get_engine(testing: bool = False):
    if testing:
        engine = create_async_engine("sqlite+aiosqlite:///testing.sqlite", echo=True)
    # will add prod/ final db later.. probably mariaDB :p
    # If i don't get too lazy lmao... 
    
    return engine

engine = get_engine(testing=True) # change True here too... Probably should make a global variable but eh

# async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# fastapi dependency endpoint, we truly love fastapi <3
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        
        yield session