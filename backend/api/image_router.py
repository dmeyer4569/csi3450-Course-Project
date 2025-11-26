"""
I'll have anything images related handled by this router
makes it nice and pretty + keeps me from going insane -ish
"""

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from pathlib import Path
from database.session import get_db
from db.sqlscripts.data import images
from db.sqlscripts import select_db_scripts as sel_db
import os

image_router = APIRouter()


@image_router.get("/get_image/{image_id}", tags=["Images"])
async def get_image(image_id: int):

    

    img = next((i for i in images if i.get("imageID") == image_id), None)
    if not img:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")

    filename = img.get("FileName") or Path(img.get("FilePath")).name
    static_dir = Path(__file__).resolve().parent.parent / "images"
    file_path = static_dir / filename

    print(file_path)

    if not file_path.exists():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Image file not found: {filename}")

    return FileResponse(path=str(file_path), media_type="image/png", filename=filename)

@image_router.get("/get_car_image/{car_id}", tags=["Images"])
async def get_car_image(car_id: int, db: AsyncSession = Depends(get_db)):
    # get images form db
    result = await db.execute(sel_db.get_car_images, {"carID": car_id})
    images = result.fetchall()
    # return http except if no images found
    if not result:
        raise HTTPException(status_code=404, detail="No images found for this car")
    print(images)

    response_data = []

    for img in images:
        img_id, name, path, description, *_ = img  
        abs_path = os.path.join(os.getcwd(), path)  # Make path absolute
        if not os.path.exists(abs_path):
            print(abs_path)
            continue  # skip this image
        
        # Extract relative path from 'images' onwards
        relative_path = path[path.find('images'):] if 'images' in path else path
        response_data.append({
            "id": img_id,
            "name": name,
            "description": description,
            "image_path": relative_path
        })

    if not response_data:
        raise HTTPException(status_code=404, detail="No valid image files found")

    # return images as relative paths
    return JSONResponse(content=response_data)