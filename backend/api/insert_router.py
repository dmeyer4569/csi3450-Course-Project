"""
insert data into the db from the 
"""
import os
import uuid
from fastapi import Depends, APIRouter, Form, HTTPException, UploadFile, status, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database.session import get_db
from db.sqlscripts import fill_db_scripts as fillDB
from typing import List

insert_router = APIRouter()

@insert_router.post("/insert_manufacturer", tags=["Initialize"])
async def insert_manufacturer(
    manufacturerName: str,
    established: str,
    headquarters: str,
    description: str,
    image: UploadFile = File(None),  # optional
    fileName: str = Form(None),  # optional
    imgDescription: str = Form(None), #optional 
    db: AsyncSession = Depends(get_db)
):

    if not all([manufacturerName, established, headquarters, description]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Manufacturer fields required"
        )
    
    # default if image is none, utilize placeholder 
    if image is None:
        await db.execute(
            fillDB.insert_into_manufacturer,
            {
                "manufacturerName": manufacturerName,
                "established": established,
                "headquarters": headquarters,
                "description": description,
                "logoID": 0
            }
        )
        await db.commit()
        return {"message": "Manufacturer inserted without logo."}

    # if image was provided run the following

    # make sure fileName and imgDescription are provided
    if not all([fileName, imgDescription]):
        raise HTTPException(
            status_code=400,
            detail="fileName and imgDescription are required when uploading an image."
        )

    # save img directory
    upload_dir = "images/uploads"
    os.makedirs(upload_dir, exist_ok=True)

    #  give it a filename such that no img has the same name
    ext = os.path.splitext(image.filename)[1]
    safe_file_name = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(upload_dir, safe_file_name)

    # save the image
    contents = await image.read()
    with open(file_path, "wb") as f:
        f.write(contents)

    # add imageto db table
    result = await db.execute(
        fillDB.insert_into_images,
        {
            "FileName": fileName,
            "FilePath": file_path,
            "Description": imgDescription
        }
    )
    await db.commit()

    # get the id of the last inserted item
    image_id = result.lastrowid

    # insert manufacturer with logoID
    await db.execute(
        fillDB.insert_into_manufacturer,
        {
            "manufacturerName": manufacturerName,
            "established": established,
            "headquarters": headquarters,
            "description": description,
            "logoID": image_id
        }
    )
    await db.commit()

    return {"message": "Manufacturer inserted with logo."}

# same as above but for cars, also can take multiple images
@insert_router.post("/insert_car", tags=["Initialize"])
async def insert_car(
    model: str,
    year: int,
    baseMSRP: float,
    manufacturerID: int,
    images: List[UploadFile] = File(None),  # optional
    db: AsyncSession = Depends(get_db)
):
    if not all([model, year, baseMSRP, manufacturerID]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="All car fields are required")
    if not images:
        await db.execute(
            fillDB.insert_into_car,
            {
                "model": model,
                "year": year,
                "baseMSRP": baseMSRP,
                "manufacturerID": manufacturerID
            }
        )
        await db.commit()
    
    else: 
        upload_dir = "images/uploads"
        os.makedirs(upload_dir, exist_ok=True)

        for image in images:
            ext = os.path.splitext(image.filename)[1]
            safe_file_name = f"{uuid.uuid4().hex}{ext}"
            file_path = os.path.join(upload_dir, safe_file_name)

            contents = await image.read()
            with open(file_path, "wb") as f:
                f.write(contents)
            result = await db.execute(
                fillDB.insert_into_images,
                {
                    "FileName": image.filename,
                    "FilePath": file_path,
                    "Description": f"Image for {model}"
                }
            )
            await db.commit()
            image_id = result.lastrowid
            await db.execute(
                fillDB.insert_into_car,
                {
                    "model": model,
                    "year": year,
                    "baseMSRP": baseMSRP,
                    "manufacturerID": manufacturerID
                }
            )
            await db.commit()
            car_result = await db.execute(
                text("SELECT last_insert_rowid() as carID")
            )
            car_id = car_result.scalar_one()
            await db.execute(
                fillDB.insert_into_car_images,
                {
                    "carID": car_id,
                    "imageID": image_id,
                    "role": "gallery" # tbh, idk why tf I have role... but at this point just gonan keep it 
                }
            )
            await db.commit()

    return {"message": "Car inserted successfully."}