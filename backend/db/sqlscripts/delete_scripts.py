"""
sql queries for mainly delete_router.py
"""

from sqlalchemy import text


delete_manufacturer = text(
    """
    DELETE FROM manufacturers
    WHERE manufacturerID = :manufacturerID
    """
)


delete_car = text(
    """
    DELETE FROM cars
    WHERE carID = :carID
    """
)


delete_image = text(
    """
    DELETE FROM images
    WHERE imageID = :imageID
    """
)


get_manufacturer_logo = text(
    """
    SELECT logoID FROM manufacturers WHERE manufacturerID = :manufacturerID
    """
)


get_image_by_id = text(
    """
    SELECT * FROM images WHERE imageID = :imageID
    """
)


get_images_for_car = text(
    """
    SELECT i.imageID, i.FilePath
    FROM images i
    JOIN car_images ci ON ci.imageID = i.imageID
    WHERE ci.carID = :carID
    """
)


count_car_image_refs = text(
    """
    SELECT COUNT(*) FROM car_images WHERE imageID = :imageID
    """
)


count_manufacturer_logo_refs = text(
    """
    SELECT COUNT(*) FROM manufacturers WHERE logoID = :imageID
    """
)
