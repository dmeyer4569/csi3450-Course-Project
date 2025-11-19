"""
edit the data inside the db. I am not implementing cookies for auth
this is just to show off functionality
"""
import os
import uuid
# might not need above 2, copied from insert_router.py
from fastapi import Depends, APIRouter, Form, HTTPException, UploadFile, status, File
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from db.sqlscripts import edit_scripts as editDB
from typing import List

edit_router = APIRouter()

# I don't wanna implement images cuz more work lol... might add later
@edit_router.put("/edit_manufacturer", tags=["Edit"])
async def edit_manufacturer(
    manufacturerID: int,
    manufacturerName: str = None,
    established: str = None,
    headquarters: str = None,
    description: str = None,
    db: AsyncSession = Depends(get_db)
):
    if manufacturerID is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="manufacturerID is required to edit a manufacturer."
        )
    # make sure at least oen field is filled to edit 
    if all(param is None for param in [manufacturerName, established, headquarters, description]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one field to edit must be provided."
        )
    
    query = editDB.edit_manufacturer_script(manufacturerID, manufacturerName, established, headquarters, description)
    await db.execute(query, {
        "manufacturerID": manufacturerID,
        "manufacturerName": manufacturerName,
        "established": established,
        "headquarters": headquarters,
        "description": description,
    })
    await db.commit()

    return {"message": "Manufacturer edited successfully."}

    #same as eidt manufacturer but for cars
@edit_router.put("/edit_car", tags=["Edit"])
async def edit_car(
    carID: int,
    model: str = None,
    year: int = None,
    baseMSRP: float = None,
    manufacturerID: int = None,
    db: AsyncSession = Depends(get_db)
):
    if carID is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="carID is required to edit a car."
        )
    # make sure at least one field is filled to edit
    if all(param is None for param in [model, year, baseMSRP, manufacturerID]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one field to edit must be provided."
        )
    
    query = editDB.edit_car_script(model, year, baseMSRP, manufacturerID)
    await db.execute(query, {
        "carID": carID,
        "model": model,
        "year": year,
        "baseMSRP": baseMSRP,
        "manufacturerID": manufacturerID,
    })
    await db.commit()

    return {"message": "Car edited successfully."}  