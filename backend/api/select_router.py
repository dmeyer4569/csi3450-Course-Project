import os
from fastapi import Depends, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from db.sqlscripts import select_db_scripts as sel_db

select_router = APIRouter()


# get all manufacturers
@select_router.get("/get_manufacturers", tags=["Select"])
async def get_manufacturers(db: AsyncSession = Depends(get_db)):
    # by default, if no offset or limit are provided will have a offset of 0, and limit of 5
    raw_result = await db.execute(sel_db.get_manufacturers)
    manufacturers = raw_result.mappings().all()

    return manufacturers

# works similar to manufacturers, but for cars + return first image
@select_router.get("/get_cars", tags=["Select"])
async def get_cars(db: AsyncSession = Depends(get_db)):
    # smae like manufact, limit is 10 and offset 0 by default
    raw_result = await db.execute(sel_db.get_cars)
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

        logo_path = None
        logo_file_path = car_data.get("logoFilePath")
        if logo_file_path:
            abs_logo_path = os.path.join(os.getcwd(), logo_file_path)
            if os.path.exists(abs_logo_path):
                logo_path = logo_file_path[logo_file_path.find('images'):] if 'images' in logo_file_path else logo_file_path
  
        car_data["manufacturer_logo_path"] = logo_path
        car_data.pop("logoFilePath", None)
        car_data.pop("logoFileName", None)
        car_data["car_image_path"] = image_path
        car_data.pop("FilePath", None)
        car_data.pop("imageID", None)
        car_data.pop("manufacturerID", None)
        car_data.pop("FileName", None)


        return_data.append(car_data)

    if not return_data:
        raise HTTPException(status_code=404, detail="No cars found :(")
    
    return JSONResponse(content=return_data)

# get a manufacturer with all their cars
@select_router.get("/get_manufacturer_cars/{manufacturer_id}", tags=["Select"])
async def get_manufacturer_cars(manufacturer_id: int, db: AsyncSession = Depends(get_db)):
    # get all cars by a manufacturer
    raw_result = await db.execute(sel_db.get_cars_by_manufacturer, {"manufacturerID": manufacturer_id})
    cars = raw_result.mappings().all()

    return_data = []

    if not cars:
        raise HTTPException(status_code=404, detail="No cars found for this manufacturer :(")

    for car in cars:
        car_data = dict(car) # make the mapping a dict 
        image_path = None

        # verify image actually exists and extract relative path
        file_path = car_data.get("FilePath")
        print(file_path)

        car_data.pop("imageID", None)
        car_data.pop("manufacturerID", None)
        car_data.pop("FileName", None)
        car_data.pop("carImageID", None)
        car_data.pop("addedAt", None)
        return_data.append(car_data)

    return return_data