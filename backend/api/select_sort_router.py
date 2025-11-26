import os 
from fastapi import Depends, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from db.sqlscripts import crazysqlscripter as crazy_sql

select_sort_router = APIRouter()

@select_sort_router.get("/get_manufacturers/{manufacturer_id}", tags=["Select"])
async def get_manufacturers(manufacturer_id: int, limit: int = 5, offset: int = 0, order: int = 0, db: AsyncSession = Depends(get_db)):

    # default 0 = descending c.year, 1 = ascending c.year, 2 = descending c.baseMSRP, 3 = ascending c.baseMSRP

    query_script = crazy_sql.custom_car_from_manu_script(order)

    raw_result = await db.execute(query_script, {"manufacturerID": manufacturer_id, "limit": limit, "offset": offset})
    cars = raw_result.mappings().all()

    return_data = []

    for car in cars:
        car_data = dict(car) # make the mapping a dict 
        image_path = None

        # verify image actually exists and extract relative path
        file_path = car_data.get("FilePath")
        print(file_path)
        if file_path:
            abs_path = os.path.join(os.getcwd(), file_path)
            print(abs_path)
            if os.path.exists(abs_path):
                # Extract relative path from 'images' onwards
                image_path = file_path[file_path.find('images'):] if 'images' in file_path else file_path

        car_data["car_image_path"] = image_path
        car_data.pop("FilePath", None)
        car_data.pop("imageID", None)
        car_data.pop("manufacturerID", None)
        car_data.pop("FileName", None)


        return_data.append(car_data)

    return JSONResponse(content=return_data)