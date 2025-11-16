import os
from fastapi import Depends, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from db.sqlscripts import select_db_scripts as sel_db 
import base64

select_router = APIRouter()


# get all manufacturers
@select_router.get("/get_manufacturers", tags=["Select"])
async def get_manufacturers(limit: int = 5, offset: int = 0, db: AsyncSession = Depends(get_db)):
    # by default, if no offset or limit are provided will have a offset of 0, and limit of 5
    raw_result = await db.execute(sel_db.get_manufacturers, {"limit": limit, "offset": offset})
    manufacturers = raw_result.mappings().all()

    return manufacturers

# works similar to manufacturers, but for cars + return first image
@select_router.get("/get_cars", tags=["Select"])
async def get_cars(limit: int = 10, offset: int = 0, db: AsyncSession = Depends(get_db)):
    # smae like manufact, limit is 10 and offset 0 by default
    raw_result = await db.execute(sel_db.get_cars, {"limit": limit, "offset": offset})
    cars = raw_result.mappings().all()

    return_data = []

    for car in cars:
        car_data = dict(car) # make the mapping a dict 
        image_base64 = None

        # verify image actually exists
        image_path = car_data.get("FilePath")
        print(image_path)
        if image_path:
            abs_path = os.path.join(os.getcwd(), image_path)
            print(abs_path)
            if os.path.exists(abs_path):
                try:
                    with open(abs_path, "rb") as f:
                        image_base64 = base64.b64encode(f.read()).decode("utf-8")
                except Exception as e:
                    print(f"Error with image :( {abs_path}: {e}")

        car_data["car_image_base64"] = image_base64
        car_data.pop("FilePath", None)

        return_data.append(car_data)

    if not return_data:
        raise HTTPException(status_code=404, detail="No cars found :(")
    
    return JSONResponse(content=return_data)