"""
insert into table queries, I don't think there will be anything else added here
"""

from sqlalchemy import text

insert_into_manufacturer = text(
    """
    INSERT INTO manufacturers (manufacturerID, manufacturerName, established, headquarters, description, logoID)
    VALUES (:manufacturerID, :manufacturerName, :established, :headquarters, :description, :logoID)
    """
)

insert_into_car = text(
    """
    INSERT INTO cars (carID, model, year, baseMSRP, manufacturerID)
    VALUES (:carID, :model, :year, :baseMSRP, :manufacturerID)
    """
)

insert_into_images = text(
    """
    INSERT INTO images (imageID, FileName, FilePath, Description)
    VALUES (:imageID, :FileName, :FilePath, :Description)
    """
)
