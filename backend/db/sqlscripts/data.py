"""
fills the db with data
generic data I used gpt to create this... ain't no way u catchin me typing this out myself lmao
"""

images = [
    {"FileName": "ford_logo.png", "FilePath": "images/ford_logo.png", "Description": "Ford logo"},
    {"FileName": "toyota_logo.png", "FilePath": "images/toyota_logo.png", "Description": "Toyota logo"},
    {"FileName": "honda_logo.png", "FilePath": "images/honda_logo.png", "Description": "Honda logo"},
    {"FileName": "bmw_logo.png", "FilePath": "images/bmw_logo.png", "Description": "BMW logo"},
    {"FileName": "tesla_logo.png", "FilePath": "images/tesla_logo.png", "Description": "Tesla logo"},
    {"FileName": "mercedes_logo.png", "FilePath": "images/mercedes_logo.png", "Description": "Mercedes Logo"},
]

manufacturers = [
    {
        "manufacturerName": "Ford Motor Company",
        "established": "1903-06-16",
        "headquarters": "Dearborn, Michigan, USA",
        "description": "American multinational automaker producing cars, trucks, and SUVs.",
        "logoID": 1,
    },
    {
        "manufacturerName": "Toyota Motor Corporation",
        "established": "1937-08-28",
        "headquarters": "Toyota City, Japan",
        "description": "Japanese automaker known for reliability and hybrid technology.",
        "logoID": 2,
    },
    {
        "manufacturerName": "Honda Motor Co., Ltd.",
        "established": "1948-09-24",
        "headquarters": "Minato, Tokyo, Japan",
        "description": "Japanese manufacturer of cars, motorcycles, and power equipment.",
        "logoID": 3,
    },
    {
        "manufacturerName": "Bayerische Motoren Werke AG (BMW)",
        "established": "1916-03-07",
        "headquarters": "Munich, Germany",
        "description": "German luxury vehicle and motorcycle manufacturer.",
        "logoID": 4,
    },
    {
        "manufacturerName": "Tesla, Inc.",
        "established": "2003-07-01",
        "headquarters": "Palo Alto, California, USA",
        "description": "Electric vehicle and clean energy company.",
        "logoID": 5,
    },
    {
        "manufacturerName": "Mercedes-Benz",
        "established": "1926-06-28",
        "headquarters": "Stuttgart, Germany",
        "description": "Luxury vehicles and automotive engineering company.",
        "logoID": 6
    },
    {
        "manufacturerName": "Audi AG",
        "established": "1909-07-16",
        "headquarters": "Ingolstadt, Germany",
        "description": "Premium automobile manufacturer known for advanced technology.",
        "logoID": 7
    },
    {
        "manufacturerName": "Ferrari S.p.A.",
        "established": "1939-09-13",
        "headquarters": "Maranello, Italy",
        "description": "High-performance sports car manufacturer.",
        "logoID": 8
    },
    {
        "manufacturerName": "Automobili Lamborghini S.p.A.",
        "established": "1963-10-30",
        "headquarters": "Sant'Agata Bolognese, Italy",
        "description": "Italian manufacturer of luxury supercars.",
        "logoID": 9
    },
    {

        "manufacturerName": "Volkswagen AG",
        "established": "1937-05-28",
        "headquarters": "Wolfsburg, Germany",
        "description": "Global automobile manufacturer producing a wide range of vehicles.",
        "logoID": 10
    },
    {

        "manufacturerName": "McLaren Automotive",
        "established": "1985-09-02",
        "headquarters": "Woking, Surrey, United Kingdom",
        "description": "British manufacturer of high-performance supercars.",
        "logoID": 11
    },
    {

        "manufacturerName": "Pagani Automobili S.p.A.",
        "established": "1992-01-01",
        "headquarters": "San Cesario sul Panaro, Italy",
        "description": "Italian manufacturer of exclusive hypercars.",
        "logoID": 12
    },
    {

        "manufacturerName": "Koenigsegg Automotive AB",
        "established": "1994-08-12",
        "headquarters": "Ängelholm, Sweden",
        "description": "Swedish manufacturer of high-performance hypercars.",
        "logoID": 13
    },
    {

        "manufacturerName": "Renault Group",
        "established": "1899-02-25",
        "headquarters": "Boulogne-Billancourt, France",
        "description": "French multinational automobile manufacturer.",
        "logoID": 14
    },
    {

        "manufacturerName": "Bugatti Automobiles S.A.S.",
        "established": "1909-01-01",
        "headquarters": "Molsheim, France",
        "description": "Luxury hypercar manufacturer known for extreme performance.",
        "logoID": 15
    }
]

# ~3 cars per manufacturer (15 total)
cars = [
    { "model": "F-150", "year": 2023, "baseMSRP": 34995, "manufacturerID": 1},
    { "model": "Mustang", "year": 2024, "baseMSRP": 28995, "manufacturerID": 1},
    { "model": "Explorer", "year": 2022, "baseMSRP": 33995, "manufacturerID": 1},

    { "model": "Camry", "year": 2023, "baseMSRP": 25995, "manufacturerID": 2},
    { "model": "Corolla", "year": 2024, "baseMSRP": 21425, "manufacturerID": 2},
    { "model": "RAV4", "year": 2023, "baseMSRP": 27750, "manufacturerID": 2},

    { "model": "Civic", "year": 2024, "baseMSRP": 22650, "manufacturerID": 3},
    { "model": "Accord", "year": 2023, "baseMSRP": 27950, "manufacturerID": 3},
    { "model": "CR-V", "year": 2024, "baseMSRP": 29350, "manufacturerID": 3},

    {"model": "3 Series", "year": 2024, "baseMSRP": 41900, "manufacturerID": 4},
    {"model": "X5", "year": 2023, "baseMSRP": 60900, "manufacturerID": 4},
    {"model": "i4", "year": 2024, "baseMSRP": 51600, "manufacturerID": 4},

    {"model": "Model S", "year": 2024, "baseMSRP": 79990, "manufacturerID": 5},
    {"model": "Model 3", "year": 2024, "baseMSRP": 39990, "manufacturerID": 5},
    {"model": "Model Y", "year": 2024, "baseMSRP": 49990, "manufacturerID": 5},

    {"model": "C-Class", "year": 2024, "baseMSRP": 43900, "manufacturerID": 6},
    {"model": "E-Class", "year": 2024, "baseMSRP": 57900, "manufacturerID": 6},
    {"model": "S-Class", "year": 2024, "baseMSRP": 114500, "manufacturerID": 6},
    {"model": "GLC", "year": 2024, "baseMSRP": 47450, "manufacturerID": 6},
    {"model": "GLE", "year": 2024, "baseMSRP": 62900, "manufacturerID": 6},

    {"model": "A4", "year": 2024, "baseMSRP": 41900, "manufacturerID": 7},
    {"model": "A6", "year": 2024, "baseMSRP": 57900, "manufacturerID": 7},
    {"model": "Q5", "year": 2024, "baseMSRP": 45500, "manufacturerID": 7},
    {"model": "Q7", "year": 2024, "baseMSRP": 59900, "manufacturerID": 7},
    {"model": "R8", "year": 2024, "baseMSRP": 161000, "manufacturerID": 7},

    {"model": "488 GTB", "year": 2024, "baseMSRP": 262000, "manufacturerID": 8},
    {"model": "F8 Tributo", "year": 2024, "baseMSRP": 283950, "manufacturerID": 8},
    {"model": "Roma", "year": 2024, "baseMSRP": 222620, "manufacturerID": 8},
    {"model": "SF90 Stradale", "year": 2024, "baseMSRP": 524815, "manufacturerID": 8},
    {"model": "812 Superfast", "year": 2024, "baseMSRP": 340000, "manufacturerID": 8},

    {"model": "Huracán", "year": 2024, "baseMSRP": 249865, "manufacturerID": 9},
    {"model": "Aventador", "year": 2024, "baseMSRP": 507353, "manufacturerID": 9},
    {"model": "Urus", "year": 2024, "baseMSRP": 237848, "manufacturerID": 9},
    {"model": "Revuelto", "year": 2024, "baseMSRP": 608358, "manufacturerID": 9},
    {"model": "Sian", "year": 2024, "baseMSRP": 3300000, "manufacturerID": 9},

    {"model": "Golf", "year": 2024, "baseMSRP": 24500, "manufacturerID": 10},
    {"model": "Passat", "year": 2024, "baseMSRP": 29900, "manufacturerID": 10},
    {"model": "Tiguan", "year": 2024, "baseMSRP": 28900, "manufacturerID": 10},
    {"model": "Atlas", "year": 2024, "baseMSRP": 36800, "manufacturerID": 10},
    {"model": "ID.4", "year": 2024, "baseMSRP": 39995, "manufacturerID": 10},

    {"model": "720S", "year": 2024, "baseMSRP": 310500, "manufacturerID": 11},
    {"model": "Artura", "year": 2024, "baseMSRP": 233000, "manufacturerID": 11},
    {"model": "765LT", "year": 2024, "baseMSRP": 382500, "manufacturerID": 11},
    {"model": "GT", "year": 2024, "baseMSRP": 210000, "manufacturerID": 11},
    {"model": "Senna", "year": 2024, "baseMSRP": 1000000, "manufacturerID": 11},

    {"model": "Huayra", "year": 2024, "baseMSRP": 3500000, "manufacturerID": 12},
    {"model": "Zonda R", "year": 2024, "baseMSRP": 1800000, "manufacturerID": 12},
    {"model": "Huayra BC", "year": 2024, "baseMSRP": 2800000, "manufacturerID": 12},
    {"model": "Utopia", "year": 2024, "baseMSRP": 2500000, "manufacturerID": 12},
    {"model": "Zonda Cinque", "year": 2024, "baseMSRP": 2300000, "manufacturerID": 12},

    {"model": "Jesko", "year": 2024, "baseMSRP": 3000000, "manufacturerID": 13},
    {"model": "Regera", "year": 2024, "baseMSRP": 1900000, "manufacturerID": 13},
    {"model": "Agera RS", "year": 2024, "baseMSRP": 2500000, "manufacturerID": 13},
    {"model": "Gemera", "year": 2024, "baseMSRP": 1700000, "manufacturerID": 13},
    {"model": "One:1", "year": 2024, "baseMSRP": 2800000, "manufacturerID": 13},

    {"model": "Clio", "year": 2024, "baseMSRP": 19000, "manufacturerID": 14},
    {"model": "Megane", "year": 2024, "baseMSRP": 24000, "manufacturerID": 14},
    {"model": "Captur", "year": 2024, "baseMSRP": 23000, "manufacturerID": 14},
    {"model": "Arkana", "year": 2024, "baseMSRP": 27000, "manufacturerID": 14},
    {"model": "Austral", "year": 2024, "baseMSRP": 30000, "manufacturerID": 14},

    {"model": "Chiron", "year": 2024, "baseMSRP": 3000000, "manufacturerID": 15},
    {"model": "Divo", "year": 2024, "baseMSRP": 5800000, "manufacturerID": 15},
    {"model": "Centodieci", "year": 2024, "baseMSRP": 9000000, "manufacturerID": 15},
    {"model": "Veyron Super Sport", "year": 2024, "baseMSRP": 2400000, "manufacturerID": 15},
    {"model": "Bolide", "year": 2024, "baseMSRP": 4700000, "manufacturerID": 15}

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

    {"carID": 16, "imageID": 6, "role":"logo"},

]
__all__ = ["images", "manufacturers", "cars"]
