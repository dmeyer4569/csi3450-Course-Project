from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from db.sqlscripts import delete_scripts as ds
import os

delete_router = APIRouter()


@delete_router.delete("/delete_manufacturer/{manufacturer_id}", tags=["Delete"])
async def delete_manufacturer(manufacturer_id: int, db: AsyncSession = Depends(get_db)):
    # get manufacturer (logo)
    result = await db.execute(ds.get_manufacturer_logo, {"manufacturerID": manufacturer_id})
    row = result.fetchone()
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Manufacturer not found")

    logo_id = row[0]

    # delete the manufacturer (cars should cascade)
    await db.execute(ds.delete_manufacturer, {"manufacturerID": manufacturer_id})
    await db.commit()

    # if there was a logo image, clean up if it's no longer referenced
    if logo_id:
        # check whether any manufacturers still reference the logo
        m_ref = await db.execute(ds.count_manufacturer_logo_refs, {"imageID": logo_id})
        m_count = m_ref.scalar_one()
        c_ref = await db.execute(ds.count_car_image_refs, {"imageID": logo_id})
        c_count = c_ref.scalar_one()

        if m_count == 0 and c_count == 0:
            # fetch image path
            img_res = await db.execute(ds.get_image_by_id, {"imageID": logo_id})
            img_row = img_res.fetchone()
            if img_row:
                file_path = img_row[2] if len(img_row) > 2 else None
                await db.execute(ds.delete_image, {"imageID": logo_id})
                await db.commit()
                if file_path:
                    abs_path = os.path.join(os.getcwd(), file_path)
                    try:
                        if os.path.exists(abs_path):
                            os.remove(abs_path)
                    except Exception:
                        pass

    return {"message": "Manufacturer deleted"}


@delete_router.delete("/delete_car/{car_id}", tags=["Delete"])
async def delete_car(car_id: int, db: AsyncSession = Depends(get_db)):
    # get images associated with the car (so we can cleanup orphaned images)
    imgs_res = await db.execute(ds.get_images_for_car, {"carID": car_id})
    images = imgs_res.fetchall()

    # delete the car (car_images should cascade)
    await db.execute(ds.delete_car, {"carID": car_id})
    await db.commit()

    # for each image that was associated with the deleted car, delete if unreferenced
    for img in images:
        image_id = img[0]
        file_path = img[1]

        c_ref = await db.execute(ds.count_car_image_refs, {"imageID": image_id})
        c_count = c_ref.scalar_one()
        m_ref = await db.execute(ds.count_manufacturer_logo_refs, {"imageID": image_id})
        m_count = m_ref.scalar_one()

        if c_count == 0 and m_count == 0:
            await db.execute(ds.delete_image, {"imageID": image_id})
            await db.commit()
            if file_path:
                abs_path = os.path.join(os.getcwd(), file_path)
                try:
                    if os.path.exists(abs_path):
                        os.remove(abs_path)
                except Exception:
                    pass

    return {"message": "Car deleted"}


@delete_router.delete("/delete_image/{image_id}", tags=["Delete"])
async def delete_image(image_id: int, db: AsyncSession = Depends(get_db)):
    # fetch image to get the file path
    img_res = await db.execute(ds.get_image_by_id, {"imageID": image_id})
    img_row = img_res.fetchone()
    if not img_row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")

    file_path = img_row[2] if len(img_row) > 2 else None

    # delete image (car_images referencing it will be removed via ON DELETE CASCADE)
    await db.execute(ds.delete_image, {"imageID": image_id})
    await db.commit()

    # remove file from disk if present
    if file_path:
        abs_path = os.path.join(os.getcwd(), file_path)
        try:
            if os.path.exists(abs_path):
                os.remove(abs_path)
        except Exception:
            pass

    return {"message": "Image deleted"}
