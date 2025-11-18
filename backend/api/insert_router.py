"""
insert data into the db from the 
"""
import base64
import os
from datetime import datetime
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from db.sqlscripts import fill_db_scripts as fillDB

insert_router = APIRouter()

@insert_router.post("/insert_manufacturer", tags=["Initialize"])
async def insert_manufacturer(manufacturerName : str, 
                              established : str,
                              headquarters : str,
                              description : str,
                              logoBase64 : str,
                              fileName: str,
                              imgDescription: str,
                              db: AsyncSession = Depends(get_db)):
    # verify everything is provided, (if image is not provided utilize default logoID (0))
    if not all(manufacturerName, established, headquarters, description):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="All fields are required.")

    if not all(logoBase64, fileName, imgDescription):
        # insert manufacturer without logo
        await db.execute(fillDB.insert_into_manufacturer, {
            "manufacturerName": manufacturerName,
            "established": established,
            "headquarters": headquarters,
            "description": description,
            "logoID": 0
        })
        await db.commit()
        return {"message": "Manufacturer inserted without logo."}
    
    else: 

        # process image first
        img_data = base64.b64decode(logoBase64)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        safe_file_name = f"{timestamp}_{fileName}"
        file_path = os.path.join("images", safe_file_name)

        # ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as img_file:
            img_file.write(img_data)

        # insert image into images table
        result = await db.execute(fillDB.insert_into_images, {
            "FileName": safe_file_name,
            "FilePath": file_path,
            "Description": imgDescription
        })
        await db.commit()
        image_id = result.lastrowid

        # insert manufacturer with logoID

        await db.execute(fillDB.insert_into_manufacturer, {
            "manufacturerName": manufacturerName,
            "established": established,
            "headquarters": headquarters,
            "description": description,
            "logoID": image_id
        })
        await db.commit()
        return {"message": "Manufacturer inserted with logo."}