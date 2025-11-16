"""
Make sure to run init_db first as that creates the tables. This will return an error otherwise
"""

from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from db.sqlscripts import fill_db_scripts as fillDB
from db.sqlscripts.data import manufacturers, cars, images

insert_data_router = APIRouter()


@insert_data_router.post("/insert_data", tags=["Initialize"])
async def initialize_data(db: AsyncSession = Depends(get_db)):


    # insert imgs
    for img in images:
        await db.execute(fillDB.insert_into_images, img)

    # insert manufact
    for m in manufacturers:
        await db.execute(fillDB.insert_into_manufacturer, m)

    # insert vroom vrooms
    for c in cars:
        await db.execute(fillDB.insert_into_car, c)

    await db.commit()
    raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Seed data inserted successfully.")
