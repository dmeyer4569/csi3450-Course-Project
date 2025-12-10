import os 
from fastapi import Depends, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from db.sqlscripts import crazysqlscripter as crazy_sql
from db.sqlscripts import select_db_scripts as seldb

select_sort_router = APIRouter()

@select_sort_router.get("/get_manufacturers/{manufacturer_id}", tags=["Select"])
async def get_manufacturers(manufacturer_id: int, order: int = 0, db: AsyncSession = Depends(get_db)):

    # default 0 = descending c.year, 1 = ascending c.year, 2 = descending c.baseMSRP, 3 = ascending c.baseMSRP

    query_script = crazy_sql.custom_car_from_manu_script(order)

    raw_result = await db.execute(query_script, {"manufacturerID": manufacturer_id})

    cars = raw_result.mappings().all()
    raw_result_manu = await db.execute(seldb.get_manufacturers, {"manufacturerID": manufacturer_id})
    manufacturer = raw_result_manu.mappings().first()
    return_data = []
    manufacturer_dict = dict(manufacturer)
    logo_path = manufacturer_dict["FilePath"]
    for car in cars:
        car_data = dict(car) # make the mapping a dict 
        image_path = None

        # verify image actually exists and extract relative path
        file_path = car_data.get("FilePath")
        print(file_path)


        car_data.pop("imageID", None)
        car_data.pop("manufacturerID", None)
        car_data.pop("FileName", None)

        car_data["manufacturer_logo_path"] = logo_path
        return_data.append(car_data)

    return JSONResponse(content=return_data)