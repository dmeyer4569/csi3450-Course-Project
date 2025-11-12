from fastapi import Depends, APIRouter, HTTPException, Path, status
from database.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlscripts import fill_db_scripts as fillDB
from sqlscripts.data import movie_data

insert_data_router = APIRouter()

@insert_data_router.post("/insert_data", tags=["Initialize"])
async def initialize_movie(db: AsyncSession = Depends(get_db)):

    for movie in movie_data.movies:
        await db.execute(fillDB.insert_into_movie, movie)

    await db.commit()
    raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Movies inserted successfully.")