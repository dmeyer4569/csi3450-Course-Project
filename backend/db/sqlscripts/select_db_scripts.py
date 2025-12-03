"""
Probably will have the following : 
    1. List all cars created by a manufacturer -> DONE
    2. List all manufacturers -> DONE
    3. List all cars -> DONE 
    4. List a specific car with all its images -> DONE
    5. Find the most expensive car -> Next
    6. Find the oldest car manufacturer -> Next, maybe combine with no 5
    7. tbd as i go 
"""

from sqlalchemy import text

# select data from db 

# cars by manufacturer
get_manufact_cars = text(
    """
    SELECT c.carID, c.model, c.year, c.baseMSRP, c.manufacturerID, m.manufacturerName, m.logoFilePath,
           i.imageID, i.FileName, i.FilePath, ci.role, ci.addedAt
    FROM cars c
    LEFT JOIN manufacturers m ON m.manufacturerID = c.manufacturerID
    LEFT JOIN car_images ci ON ci.carID = c.carID
    AND ci.carImageID = (
        SELECT ci2.carImageID
        FROM car_images ci2
        WHERE ci2.carID = c.carID
        ORDER BY ci2.addedAt ASC, ci2.carImageID ASC
        LIMIT 1
    )
    LEFT JOIN images i ON i.imageID = ci.imageID
    WHERE (:manufacturer_id IS NULL OR c.manufacturerID = :manufacturer_id)
    AND (:manufacturer_name IS NULL OR m.manufacturerName LIKE '%' || :manufacturer_name || '%')
    ORDER BY c.year DESC, c.model
    LIMIT 200 OFFSET 0;
    """
)

# get all manufacturers
get_manufacturers = text(
    """
    SELECT * 
    FROM manufacturers
    LIMIT :limit OFFSET :offset;
    """
)

# get all cars
get_cars = text(
    """
    SELECT
        c.*,
        i.imageID,
        i.FileName,
        i.FilePath,
        ci.role,
        m.manufacturerName,
        m.logoID,
        mi.FileName AS logoFileName,
        mi.FilePath AS logoFilePath
    FROM cars c
    LEFT JOIN car_images ci ON ci.carImageID = (
        SELECT ci2.carImageID
        FROM car_images ci2
        WHERE ci2.carID = c.carID
        ORDER BY ci2.addedAt ASC, ci2.carImageID ASC
        LIMIT 1
    )
    LEFT JOIN manufacturers m on m.manufacturerID = c.manufacturerID
    LEFT JOIN images i ON i.imageID = ci.imageID
    LEFT JOIN images mi ON mi.imageID = m.logoID
    LIMIT 200 OFFSET 0;
    """
)

# get images of a car, split it up cuz easier handling when multiple images are returned
get_car_images = text(
    """
    SELECT i.*, ci.role, ci.addedAt
    FROM images i
    JOIN car_images ci ON ci.imageID = i.imageID
    WHERE ci.carID = :carID
    """
)

# Get all cars of a manufacturer
get_cars_by_manufacturer = text(
    """
    SELECT c.*, ci.*, i.FilePath, i.FileName
    FROM cars c
    LEFT JOIN car_images ci 
    ON ci.carID = c.carID
    AND ci.carImageID = (
        SELECT ci2.carImageID
        FROM car_images ci2
        WHERE ci2.carID = c.carID
        ORDER BY ci2.addedAt ASC, ci2.carImageID ASC
        LIMIT 1
    )
    LEFT JOIN images i on i.imageID = ci.imageID
    WHERE c.manufacturerID = :manufacturerID
    ORDER BY c.year DESC, c.model
    LIMIT 200 OFFSET 0;
    """
)