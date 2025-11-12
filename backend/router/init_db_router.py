from fastapi import Depends, APIRouter, HTTPException, Path, status
from database.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlscripts import init_db_scripts as initDB
from sqlscripts import init_db_mtm_scripts as initDB_mtm

init_router = APIRouter()

@init_router.post("/spawn_db_tables", tags=["Initialize"])
async def initialize_movie(db: AsyncSession = Depends(get_db)):
    await db.execute(initDB.create_movie_table)
    await db.execute(initDB.create_producer_table)
    await db.execute(initDB.create_actor_table)
    await db.execute(initDB.create_actress_table)
    await db.execute(initDB.create_person_table)
    await db.execute(initDB.create_writer_table)
    await db.execute(initDB.create_director_table)

    # mtm tables
    await db.execute(initDB_mtm.create_movie_producer_table)
    await db.execute(initDB_mtm.create_movie_actor_table)
    await db.execute(initDB_mtm.create_movie_actress_table)
    await db.execute(initDB_mtm.create_movie_writer_table)
    await db.execute(initDB_mtm.create_movie_director_table)

    await db.commit()

    raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Tables created successfully.")