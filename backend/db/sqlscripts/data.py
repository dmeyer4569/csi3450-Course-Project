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
    {"FileName": "A42024Black.jpg", "FilePath": "images/A42024Black.jpg", "Description": "A4 2024 Black"},
    {"FileName": "A42024Red.jpg", "FilePath": "images/A42024Red.jpg", "Description": "A4 2024 Red"},
    {"FileName": "A42024White.webp", "FilePath": "images/A42024White.webp", "Description": "A4 2024 White"},

    {"FileName": "A62024Front.avif", "FilePath": "images/A62024Front.avif", "Description": "A6 2024 Front"},
    {"FileName": "A62024Grey.avif", "FilePath": "images/A62024Grey.avif", "Description": "A6 2024 Grey"},
    {"FileName": "A62024White.webp", "FilePath": "images/A62024White.webp", "Description": "A6 2024 White"},

    {"FileName": "Q52024Blue.jpg", "FilePath": "images/Q52024Blue.jpg", "Description": "Q5 2024 Blue"},
    {"FileName": "Q52024Green.jpg", "FilePath": "images/Q52024Green.jpg", "Description": "Q5 2024 Green"},
    {"FileName": "Q52024White.jpg", "FilePath": "images/Q52024White.jpg", "Description": "Q5 2024 White"},

    {"FileName": "Q72024Black.jpg", "FilePath": "images/Q72024Black.jpg", "Description": "Q7 2024 Black"},
    {"FileName": "Q72024Grey.jpg", "FilePath": "images/Q72024Grey.jpg", "Description": "Q7 2024 Grey"},
    {"FileName": "Q72024White.jpg", "FilePath": "images/Q72024White.jpg", "Description": "Q7 2024 White"},

    {"FileName": "R82024Blue.jpg", "FilePath": "images/R82024Blue.jpg", "Description": "R8 2024 Blue"},
    {"FileName": "R82024Grey.jpg", "FilePath": "images/R82024Grey.jpg", "Description": "R8 2024 Grey"},
    {"FileName": "R82024White.jpg", "FilePath": "images/R82024White.jpg", "Description": "R8 2024 White"},

    {"FileName": "488GTBRed.jpg", "FilePath": "images/488GTBRed.jpg", "Description": "488 GTB 2024 Red"},
    {"FileName": "488GTBWhite.jpg", "FilePath": "images/488GTBWhite.jpg", "Description": "488 GTB 2024 White"},
    {"FileName": "488GTBYellow.jpg", "FilePath": "images/488GTBYellow.jpg", "Description": "488 GTB 2024 Yellow"},

    {"FileName": "F8TributoBlack.jpg", "FilePath": "images/F8TributoBlack.jpg", "Description": "F8 Tributo 2024 Black"},
    {"FileName": "F8TributoRed.jpg", "FilePath": "images/F8TributoRed.jpg", "Description": "F8 Tributo 2024 Red"},
    {"FileName": "F8TributoYellow.jpg", "FilePath": "images/F8TributoYellow.jpg", "Description": "F8 Tributo 2024 Yellow"},

    {"FileName": "Roma2024Grey.jpg", "FilePath": "images/Roma2024Grey.jpg", "Description": "Roma 2024 Grey"},
    {"FileName": "Roma2024Red.jpg", "FilePath": "images/Roma2024Red.jpg", "Description": "Roma 2024 Red"},
    {"FileName": "Roma2024White.jpg", "FilePath": "images/Roma2024White.jpg", "Description": "Roma 2024 White"},

    {"FileName": "Sf90stradale2024Black.jpg", "FilePath": "images/Sf90stradale2024Black.jpg", "Description": "SF90 Stradale 2024 Black"},
    {"FileName": "Sf90stradale2024Cream.jpg", "FilePath": "images/Sf90stradale2024Cream.jpg", "Description": "SF90 Stradale 2024 Cream"},
    {"FileName": "Sf90stradale2024Red.jpg", "FilePath": "images/Sf90stradale2024Red.jpg", "Description": "SF90 Stradale 2024 Red"},

    {"FileName": "B12Superfast2024Blue.jpg", "FilePath": "images/B12Superfast2024Blue.jpg", "Description": "812 Superfast 2024 Blue"},
    {"FileName": "B12Superfast2024Grey.jpg", "FilePath": "images/B12Superfast2024Grey.jpg", "Description": "812 Superfast 2024 Grey"},
    {"FileName": "B12Superfast2024Red.jpg", "FilePath": "images/B12Superfast2024Red.jpg", "Description": "812 Superfast 2024 Red"},

    {"FileName": "Huracán2024Red.jpg", "FilePath": "images/Huracán2024Red.jpg", "Description": "Huracán 2024 Red"},
    {"FileName": "Huracán2024White.jpg", "FilePath": "images/Huracán2024White.jpg", "Description": "Huracán 2024 White"},
    {"FileName": "Huracán2024Yellow.jpg", "FilePath": "images/Huracán2024Yellow.jpg", "Description": "Huracán 2024 Yellow"},

    {"FileName": "Aventador2024Blue.jpg", "FilePath": "images/Aventador2024Blue.jpg", "Description": "Aventador 2024 Blue"},
    {"FileName": "Aventador2024Orange.jpg", "FilePath": "images/Aventador2024Orange.jpg", "Description": "Aventador 2024 Orange"},
    {"FileName": "Aventador2024White.jpg", "FilePath": "images/Aventador2024White.jpg", "Description": "Aventador 2024 White"},

    {"FileName": "Urus2024Green.jpg", "FilePath": "images/Urus2024Green.jpg", "Description": "Urus 2024 Green"},
    {"FileName": "Urus2024Grey.jpg", "FilePath": "images/Urus2024Grey.jpg", "Description": "Urus 2024 Grey"},

    {"FileName": "Revuelto2024Grey.jpg", "FilePath": "images/Revuelto2024Grey.jpg", "Description": "Revuelto 2024 Grey"},
    {"FileName": "Revuelto2024Orange.jpg", "FilePath": "images/Revuelto2024Orange.jpg", "Description": "Revuelto 2024 Orange"},
    {"FileName": "Revuelto2024Purple.jpg", "FilePath": "images/Revuelto2024Purple.jpg", "Description": "Revuelto 2024 Purple"},

    {"FileName": "Sian2024Blue.webp", "FilePath": "images/Sian2024Blue.webp", "Description": "Sian 2024 Blue"},

    {"FileName": "Golf2024Black.jpg", "FilePath": "images/Golf2024Black.jpg", "Description": "Golf 2024 Black"},
    {"FileName": "Golf2024Blue.jpg", "FilePath": "images/Golf2024Blue.jpg", "Description": "Golf 2024 Blue"},
    {"FileName": "Golf2024White.jpg", "FilePath": "images/Golf2024White.jpg", "Description": "Golf 2024 White"},

    {"FileName": "Passat2024Blue.jpg", "FilePath": "images/Passat2024Blue.jpg", "Description": "Passat 2024 Blue"},
    {"FileName": "Passat2024Green.jpg", "FilePath": "images/Passat2024Green.jpg", "Description": "Passat 2024 Green"},
    {"FileName": "Passat2024White.jpg", "FilePath": "images/Passat2024White.jpg", "Description": "Passat 2024 White"},

    {"FileName": "Tiguan2024Orange.jpg", "FilePath": "images/Tiguan2024Orange.jpg", "Description": "Tiguan 2024 Orange"},
    {"FileName": "Tiguan2024Red.jpg", "FilePath": "images/Tiguan2024Red.jpg", "Description": "Tiguan 2024 Red"},
    {"FileName": "Tiguan2024White.jpg", "FilePath": "images/Tiguan2024White.jpg", "Description": "Tiguan 2024 White"},

    {"FileName": "Atlas2024Black.jpg", "FilePath": "images/Atlas2024Black.jpg", "Description": "Atlas 2024 Black"},
    {"FileName": "Atlas2024Grey.jpg", "FilePath": "images/Atlas2024Grey.jpg", "Description": "Atlas 2024 Grey"},
    {"FileName": "Atlas2024Red.jpg", "FilePath": "images/Atlas2024Red.jpg", "Description": "Atlas 2024 Red"},

    {"FileName": "ID.42024Blue.jpg", "FilePath": "images/ID.42024Blue.jpg", "Description": "ID.4 2024 Blue"},
    {"FileName": "ID.42024Grey.jpg", "FilePath": "images/ID.42024Grey.jpg", "Description": "ID.4 2024 Grey"},
    {"FileName": "ID.42024Red.jpg", "FilePath": "images/ID.42024Red.jpg", "Description": "ID.4 2024 Red"},

    {"FileName": "720S2024Black.jpg", "FilePath": "images/720S2024Black.jpg", "Description": "720S 2024 Black"},
    {"FileName": "720S2024Blue.jpg", "FilePath": "images/720S2024Blue.jpg", "Description": "720S 2024 Blue"},
    {"FileName": "720S2024Orange.jpg", "FilePath": "images/720S2024Orange.jpg", "Description": "720S 2024 Orange"},

    {"FileName": "Artura2024Green.jpg", "FilePath": "images/Artura2024Green.jpg", "Description": "Artura 2024 Green"},
    {"FileName": "Artura2024Orange.jpg", "FilePath": "images/Artura2024Orange.jpg", "Description": "Artura 2024 Orange"},
    {"FileName": "Artura2024Red.jpg", "FilePath": "images/Artura2024Red.jpg", "Description": "Artura 2024 Red"},

    {"FileName": "765LT2024Blue.jpg", "FilePath": "images/765LT2024Blue.jpg", "Description": "765LT 2024 Blue"},
    {"FileName": "765LT2024Green.jpg", "FilePath": "images/765LT2024Green.jpg", "Description": "765LT 2024 Green"},
    {"FileName": "765LT2024Orange.jpg", "FilePath": "images/765LT2024Orange.jpg", "Description": "765LT 2024 Orange"},

    {"FileName": "GT2024Blue.jpg", "FilePath": "images/GT2024Blue.jpg", "Description": "GT 2024 Blue"},
    {"FileName": "GT2024Grey.jpg", "FilePath": "images/GT2024Grey.jpg", "Description": "GT 2024 Grey"},
    {"FileName": "GT2024Red.jpg", "FilePath": "images/GT2024Red.jpg", "Description": "GT 2024 Red"},

    {"FileName": "Senna2024Blue.jpg", "FilePath": "images/Senna2024Blue.jpg", "Description": "Senna 2024 Blue"},
    {"FileName": "Senna2024Grey.jpg", "FilePath": "images/Senna2024Grey.jpg", "Description": "Senna 2024 Grey"},
    {"FileName": "Senna2024Orange.jpg", "FilePath": "images/Senna2024Orange.jpg", "Description": "Senna 2024 Orange"}

    
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

    #Aidens images
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
    #End Aiden Images
    
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

    {"carID": 21, "imageID": 6, "role": "gallery"},
    {"carID": 21, "imageID": 7, "role": "gallery"},
    {"carID": 21, "imageID": 8, "role": "gallery"},

    # A6 (carID 22) → images 9, 10, 11
    {"carID": 22, "imageID": 9, "role": "gallery"},
    {"carID": 22, "imageID": 10, "role": "gallery"},
    {"carID": 22, "imageID": 11, "role": "gallery"},

    # Q5 (carID 23) → images 12, 13, 14
    {"carID": 23, "imageID": 12, "role": "gallery"},
    {"carID": 23, "imageID": 13, "role": "gallery"},
    {"carID": 23, "imageID": 14, "role": "gallery"},

    # Q7 (carID 24) → images 15, 16, 17
    {"carID": 24, "imageID": 15, "role": "gallery"},
    {"carID": 24, "imageID": 16, "role": "gallery"},
    {"carID": 24, "imageID": 17, "role": "gallery"},

    # R8 (carID 25) → images 18, 19, 20
    {"carID": 25, "imageID": 18, "role": "gallery"},
    {"carID": 25, "imageID": 19, "role": "gallery"},
    {"carID": 25, "imageID": 20, "role": "gallery"},

    # 488 GTB (carID 26) → images 21, 22, 23
    {"carID": 26, "imageID": 21, "role": "gallery"},
    {"carID": 26, "imageID": 22, "role": "gallery"},
    {"carID": 26, "imageID": 23, "role": "gallery"},

    # F8 Tributo (carID 27) → images 24, 25, 26
    {"carID": 27, "imageID": 24, "role": "gallery"},
    {"carID": 27, "imageID": 25, "role": "gallery"},
    {"carID": 27, "imageID": 26, "role": "gallery"},

    # Roma (carID 28) → images 27, 28, 29
    {"carID": 28, "imageID": 27, "role": "gallery"},
    {"carID": 28, "imageID": 28, "role": "gallery"},
    {"carID": 28, "imageID": 29, "role": "gallery"},

    # SF90 Stradale (carID 29) → images 30, 31, 32
    {"carID": 29, "imageID": 30, "role": "gallery"},
    {"carID": 29, "imageID": 31, "role": "gallery"},
    {"carID": 29, "imageID": 32, "role": "gallery"},

    # 812 Superfast (carID 30) → images 33, 34, 35
    {"carID": 30, "imageID": 33, "role": "gallery"},
    {"carID": 30, "imageID": 34, "role": "gallery"},
    {"carID": 30, "imageID": 35, "role": "gallery"},

    # Huracán (carID 31) → images 36, 37, 38
    {"carID": 31, "imageID": 36, "role": "gallery"},
    {"carID": 31, "imageID": 37, "role": "gallery"},
    {"carID": 31, "imageID": 38, "role": "gallery"},

    # Aventador (carID 32) → images 39, 40, 41
    {"carID": 32, "imageID": 39, "role": "gallery"},
    {"carID": 32, "imageID": 40, "role": "gallery"},
    {"carID": 32, "imageID": 41, "role": "gallery"},

    # Urus (carID 33) → images 42, 43
    {"carID": 33, "imageID": 42, "role": "gallery"},
    {"carID": 33, "imageID": 43, "role": "gallery"},

    # Revuelto (carID 34) → images 44, 45, 46
    {"carID": 34, "imageID": 44, "role": "gallery"},
    {"carID": 34, "imageID": 45, "role": "gallery"},
    {"carID": 34, "imageID": 46, "role": "gallery"},

    # Sian (carID 35) → image 47
    {"carID": 35, "imageID": 47, "role": "gallery"},

    # Golf (carID 36) → images 48, 49, 50
    {"carID": 36, "imageID": 48, "role": "gallery"},
    {"carID": 36, "imageID": 49, "role": "gallery"},
    {"carID": 36, "imageID": 50, "role": "gallery"},

    # Passat (carID 37) → images 51, 52, 53
    {"carID": 37, "imageID": 51, "role": "gallery"},
    {"carID": 37, "imageID": 52, "role": "gallery"},
    {"carID": 37, "imageID": 53, "role": "gallery"},

    # Tiguan (carID 38) → images 54, 55, 56
    {"carID": 38, "imageID": 54, "role": "gallery"},
    {"carID": 38, "imageID": 55, "role": "gallery"},
    {"carID": 38, "imageID": 56, "role": "gallery"},

    # Atlas (carID 39) → images 57, 58, 59
    {"carID": 39, "imageID": 57, "role": "gallery"},
    {"carID": 39, "imageID": 58, "role": "gallery"},
    {"carID": 39, "imageID": 59, "role": "gallery"},

    # ID.4 (carID 40) → images 60, 61, 62
    {"carID": 40, "imageID": 60, "role": "gallery"},
    {"carID": 40, "imageID": 61, "role": "gallery"},
    {"carID": 40, "imageID": 62, "role": "gallery"},

    # 720S (carID 41) → images 63, 64, 65
    {"carID": 41, "imageID": 63, "role": "gallery"},
    {"carID": 41, "imageID": 64, "role": "gallery"},
    {"carID": 41, "imageID": 65, "role": "gallery"},

    # Artura (carID 42) → images 66, 67, 68
    {"carID": 42, "imageID": 66, "role": "gallery"},
    {"carID": 42, "imageID": 67, "role": "gallery"},
    {"carID": 42, "imageID": 68, "role": "gallery"},

    # 765LT (carID 43) → images 69, 70, 71
    {"carID": 43, "imageID": 69, "role": "gallery"},
    {"carID": 43, "imageID": 70, "role": "gallery"},
    {"carID": 43, "imageID": 71, "role": "gallery"},

    # GT (carID 44) → images 72, 73, 74
    {"carID": 44, "imageID": 72, "role": "gallery"},
    {"carID": 44, "imageID": 73, "role": "gallery"},
    {"carID": 44, "imageID": 74, "role": "gallery"},

    # Senna (carID 45) → images 75, 76, 77
    {"carID": 45, "imageID": 75, "role": "gallery"},
    {"carID": 45, "imageID": 76, "role": "gallery"},
    {"carID": 45, "imageID": 77, "role": "gallery"},

]
__all__ = ["images", "manufacturers", "cars"]
