"""
Initialize the db and add the tables if needed, I recommend manually deleting the db between tests
Up to you tho
"""

from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from db.sqlscripts import init_db_scripts as initDB

init_router = APIRouter()


@init_router.post("/spawn_db_tables", tags=["Initialize"])
async def initialize_db(db: AsyncSession = Depends(get_db)):
    # Create images first (manufacturers reference images.logoID)
    await db.execute(initDB.create_images_table)
    await db.execute(initDB.create_manufacturers_table)
    await db.execute(initDB.create_cars_table)

    await db.commit()

    raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Tables created successfully.")
