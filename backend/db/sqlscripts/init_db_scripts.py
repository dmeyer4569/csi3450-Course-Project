"""
Create the tables.. will not change unless I hit enlightenment and find more shit to add
"""


from sqlalchemy import text

# create tables for manufact, cars, and images

create_manufacturers_table = text(
    """
    CREATE TABLE IF NOT EXISTS manufacturers (
        manufacturerID INTEGER PRIMARY KEY AUTOINCREMENT,
        manufacturerName VARCHAR(100) NOT NULL,
        established DATE,
        headquarters VARCHAR(255),
        description TEXT,
        logoID INTEGER,
        FOREIGN KEY (logoID) REFERENCES images(imageID)
    )
    """
)

create_cars_table = text(
    """
    CREATE TABLE IF NOT EXISTS cars (
        carID INTEGER PRIMARY KEY AUTOINCREMENT,
        model VARCHAR(100) NOT NULL,
        year INTEGER,
        baseMSRP INTEGER,
        manufacturerID INTEGER,
        FOREIGN KEY (manufacturerID) REFERENCES manufacturers(manufacturerID) ON DELETE CASCADE
    )
    """
)

create_images_table = text(
    """
    CREATE TABLE IF NOT EXISTS images (
        imageID INTEGER PRIMARY KEY AUTOINCREMENT,
        FileName VARCHAR(255) NOT NULL,
        FilePath VARCHAR(1024) NOT NULL,
        Description TEXT,
        UploadDate DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
)


# mtm between cars and images
create_car_images_table = text(
    """
    CREATE TABLE IF NOT EXISTS car_images (
        carImageID INTEGER PRIMARY KEY AUTOINCREMENT,
        carID INTEGER NOT NULL,
        imageID INTEGER NOT NULL,
        role VARCHAR(50),
        addedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (carID) REFERENCES cars(carID) ON DELETE CASCADE,
        FOREIGN KEY (imageID) REFERENCES images(imageID) ON DELETE CASCADE,
        UNIQUE(carID, imageID)
    )
    """
)
