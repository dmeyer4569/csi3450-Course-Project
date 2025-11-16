"""
fills the db with data
generic data I used gpt to create this... ain't no way u catchin me typing this out myself lmao
"""

images = [
    {"imageID": 1, "FileName": "ford_logo.png", "FilePath": "images/ford_logo.png", "Description": "Ford logo"},
    {"imageID": 2, "FileName": "toyota_logo.png", "FilePath": "images/toyota_logo.png", "Description": "Toyota logo"},
    {"imageID": 3, "FileName": "honda_logo.png", "FilePath": "images/honda_logo.png", "Description": "Honda logo"},
    {"imageID": 4, "FileName": "bmw_logo.png", "FilePath": "images/bmw_logo.png", "Description": "BMW logo"},
    {"imageID": 5, "FileName": "tesla_logo.png", "FilePath": "images/tesla_logo.png", "Description": "Tesla logo"},
]

manufacturers = [
    {
        "manufacturerID": 1,
        "manufacturerName": "Ford Motor Company",
        "established": "1903-06-16",
        "headquarters": "Dearborn, Michigan, USA",
        "description": "American multinational automaker producing cars, trucks, and SUVs.",
        "logoID": 1,
    },
    {
        "manufacturerID": 2,
        "manufacturerName": "Toyota Motor Corporation",
        "established": "1937-08-28",
        "headquarters": "Toyota City, Japan",
        "description": "Japanese automaker known for reliability and hybrid technology.",
        "logoID": 2,
    },
    {
        "manufacturerID": 3,
        "manufacturerName": "Honda Motor Co., Ltd.",
        "established": "1948-09-24",
        "headquarters": "Minato, Tokyo, Japan",
        "description": "Japanese manufacturer of cars, motorcycles, and power equipment.",
        "logoID": 3,
    },
    {
        "manufacturerID": 4,
        "manufacturerName": "Bayerische Motoren Werke AG (BMW)",
        "established": "1916-03-07",
        "headquarters": "Munich, Germany",
        "description": "German luxury vehicle and motorcycle manufacturer.",
        "logoID": 4,
    },
    {
        "manufacturerID": 5,
        "manufacturerName": "Tesla, Inc.",
        "established": "2003-07-01",
        "headquarters": "Palo Alto, California, USA",
        "description": "Electric vehicle and clean energy company.",
        "logoID": 5,
    },
]

# ~3 cars per manufacturer (15 total)
cars = [
    {"carID": 1, "model": "F-150", "year": 2023, "baseMSRP": 34995, "manufacturerID": 1},
    {"carID": 2, "model": "Mustang", "year": 2024, "baseMSRP": 28995, "manufacturerID": 1},
    {"carID": 3, "model": "Explorer", "year": 2022, "baseMSRP": 33995, "manufacturerID": 1},

    {"carID": 4, "model": "Camry", "year": 2023, "baseMSRP": 25995, "manufacturerID": 2},
    {"carID": 5, "model": "Corolla", "year": 2024, "baseMSRP": 21425, "manufacturerID": 2},
    {"carID": 6, "model": "RAV4", "year": 2023, "baseMSRP": 27750, "manufacturerID": 2},

    {"carID": 7, "model": "Civic", "year": 2024, "baseMSRP": 22650, "manufacturerID": 3},
    {"carID": 8, "model": "Accord", "year": 2023, "baseMSRP": 27950, "manufacturerID": 3},
    {"carID": 9, "model": "CR-V", "year": 2024, "baseMSRP": 29350, "manufacturerID": 3},

    {"carID": 10, "model": "3 Series", "year": 2024, "baseMSRP": 41900, "manufacturerID": 4},
    {"carID": 11, "model": "X5", "year": 2023, "baseMSRP": 60900, "manufacturerID": 4},
    {"carID": 12, "model": "i4", "year": 2024, "baseMSRP": 51600, "manufacturerID": 4},

    {"carID": 13, "model": "Model S", "year": 2024, "baseMSRP": 79990, "manufacturerID": 5},
    {"carID": 14, "model": "Model 3", "year": 2024, "baseMSRP": 39990, "manufacturerID": 5},
    {"carID": 15, "model": "Model Y", "year": 2024, "baseMSRP": 49990, "manufacturerID": 5},
]
# images for cars, not the actual car images rn.. to be changed
car_images = [
    {"carID": 1, "imageID": 1, "role":"logo"},
    {"carID": 2, "imageID": 1, "role":"logo"},
    {"carID": 3, "imageID": 1, "role":"logo"},
    
    {"carID": 4, "imageID": 2, "role":"logo"},
    {"carID": 5, "imageID": 2, "role":"logo"},
    {"carID": 6, "imageID": 2, "role":"logo"},

    {"carID": 7, "imageID": 3, "role":"logo"},
    {"carID": 8, "imageID": 3, "role":"logo"},
    {"carID": 9, "imageID": 3, "role":"logo"},

    {"carID": 10, "imageID": 4, "role":"logo"},
    {"carID": 11, "imageID": 4, "role":"logo"},
    {"carID": 12, "imageID": 4, "role":"logo"},

    {"carID": 13, "imageID": 5, "role":"logo"},
    {"carID": 14, "imageID": 5, "role":"logo"},
    {"carID": 15, "imageID": 5, "role":"logo"},

]
__all__ = ["images", "manufacturers", "cars"]
