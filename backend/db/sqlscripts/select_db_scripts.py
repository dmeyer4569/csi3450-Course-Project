"""
Probably will have the following : 
    1. List all cars created by a manufacturer
    2. List all manufacturers
    3. List all cars
    4. List a specific car with all its images
    5. Find the most expensive car
    6. Find the oldest car manufacturer
    7. tbd as i go 
"""

from sqlalchemy import text

# select data from db 

# cars by manufacturer
get_manufact_cars = text(
    """
    SELECT c.carID, c.model, c.year, c.baseMSRP, c.manufacturerID, m.manufacturerName
    FROM cars c
    LEFT JOIN manufacturers m ON m.manufacturerID = c.manufacturerID
    WHERE (:manufacturer_id IS NULL OR c.manufacturerID = :manufacturer_id)
    AND (:manufacturer_name IS NULL OR m.manufacturerName LIKE '%' || :manufacturer_name || '%')
    ORDER BY c.year DESC, c.model
    LIMIT :limit OFFSET :offset;
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
    SELECT * 
    FROM cars
    LIMIT :limit OFFSET :offset;
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