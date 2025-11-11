from fastapi import Depends, APIRouter, HTTPException, Path, status
from database.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlscripts import init_db_scripts as initDB

init_router = APIRouter()

@init_router.post("/spawn_db_tables", tags=["Initialize"])
async def initialize_movie(db: AsyncSession = Depends(get_db)):
    await db.execute(initDB.create_movie_table)
    await db.execute(initDB.create_producer_table)
    await db.commit()