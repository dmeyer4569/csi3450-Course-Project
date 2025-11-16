"""
I'll have anything images related handled by this router
makes it nice and pretty + keeps me from going insane -ish
"""

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.responses import FileResponse
from pathlib import Path
from database.session import get_db
from db.sqlscripts.data import images

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

