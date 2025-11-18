"""
insert into table queries, I don't think there will be anything else added here
"""

from sqlalchemy import text

insert_into_manufacturer = text(
    """
    INSERT INTO manufacturers (manufacturerName, established, headquarters, description, logoID)
    VALUES (:manufacturerName, :established, :headquarters, :description, :logoID)
    """
)

insert_into_car = text(
    """
    INSERT INTO cars (model, year, baseMSRP, manufacturerID)
    VALUES (:model, :year, :baseMSRP, :manufacturerID)
    """
)

insert_into_images = text(
    """
    INSERT INTO images (FileName, FilePath, Description)
    VALUES (:FileName, :FilePath, :Description)
    """
)

insert_into_car_images = text(
    """
    INSERT INTO car_images (carID, imageID, role)
    VALUES (:carID, :imageID, :role);
    """
)
