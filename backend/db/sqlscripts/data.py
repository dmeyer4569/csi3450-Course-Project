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
    {"FileName": "audi_logo.png", "FilePath": "images/audi_logo.png", "Description": "Audi Logo"},
    {"FileName": "ferrari_logo.png", "FilePath": "images/ferrari_logo.png", "Description": "Ferrari Logo"},
    {"FileName": "lamborghini_logo.png", "FilePath": "images/lamborghini_logo.png", "Description": "Lamborghini Logo"},
    {"FileName": "vw_logo.png", "FilePath": "images/vw_logo.png", "Description": "VW Logo"},
    {"FileName": "mclaren_logo.png", "FilePath": "images/mclaren_logo.png", "Description": "McLaren Logo"},
    {"FileName": "pagani_logo.png", "FilePath": "images/pagani_logo.png", "Description": "Pagani Logo"},
    {"FileName": "koenigsegg_logo.png", "FilePath": "images/koenigsegg_logo.png", "Description": "Koenigsegg Logo"},
    {"FileName": "renault_logo.png", "FilePath": "images/renault_logo.png", "Description": "Renault Logo"},
    {"FileName": "bugatti_logo.png", "FilePath": "images/bugatti_logo.png", "Description": "Bugatti Logo"},


    #images
    {"FileName": "F-150.png", "FilePath": "images/F-150.png", "Description": "Ford F-150"},
    {"FileName": "F-150(2).jpg", "FilePath": "images/F-150(2).jpg", "Description": "Ford F-150 side view"},
    {"FileName": "F-150(3).jpg", "FilePath": "images/F-150(3).jpg", "Description": "Ford F-150 rear view"},

    {"FileName": "Mustang(1).jpg", "FilePath": "images/Mustang(1).jpg", "Description": "Ford Mustang front view"},
    {"FileName": "Mustang(2).jpg", "FilePath": "images/Mustang(2).jpg", "Description": "Ford Mustang side view"},
    {"FileName": "Mustang(3).jpg", "FilePath": "images/Mustang(3).jpg", "Description": "Ford Mustang rear view"},

    {"FileName": "Explorer(1).jpg", "FilePath": "images/Explorer(1).jpg", "Description": "Ford Explorer front view"},
    {"FileName": "Explorer(2).jpg", "FilePath": "images/Explorer(2).jpg", "Description": "Ford Explorer side view"},
    {"FileName": "Explorer(3).jpg", "FilePath": "images/Explorer(3).jpg", "Description": "Ford Explorer second front view"},

    {"FileName": "Camry(1).jpg", "FilePath": "images/Camry(1).jpg", "Description": "Toyota Camry front view"},
    {"FileName": "Camry(2).jpg", "FilePath": "images/Camry(2).jpg", "Description": "Toyota Camry side view"},
    {"FileName": "Camry(3).jpg", "FilePath": "images/Camry(3).jpg", "Description": "Toyota Camry second front view"},

    {"FileName": "Corolla(1).jpg", "FilePath": "images/Corolla(1).jpg", "Description": "Toyota Corolla front view"},
    {"FileName": "Corolla(2).jpg", "FilePath": "images/Corolla(2).jpg", "Description": "Toyota Corolla back view"},

    {"FileName": "RAV4(1).jpg", "FilePath": "images/RAV4(1).jpg", "Description": "Toyota RAV4 front view"},
    {"FileName": "RAV4(2).jpg", "FilePath": "images/RAV4(2).jpg", "Description": "Toyota RAV4 side view"},
    {"FileName": "RAV4(3).jpg", "FilePath": "images/RAV4(3).jpg", "Description": "Toyota RAV4 rear view"},

    {"FileName": "Civic(1).jpg", "FilePath": "images/Civic(1).jpg", "Description": "Honda Civic front view"},
    {"FileName": "Civic(2).jpg", "FilePath": "images/Civic(2).jpg", "Description": "Honda Civic side view"},
    {"FileName": "Civic(3).jpg", "FilePath": "images/Civic(3).jpg", "Description": "Honda Civic rear view"},

    {"FileName": "Accord(1).jpg", "FilePath": "images/Accord(1).jpg", "Description": "Honda Accord front view"},
    {"FileName": "Accord(2).jpg", "FilePath": "images/Accord(2).jpg", "Description": "Honda Accord side view"},
    {"FileName": "Accord(3).jpg", "FilePath": "images/Accord(3).jpg", "Description": "Honda Accord rear view"},

    {"FileName": "CR-V(1).jpg", "FilePath": "images/CR-V(1).jpg", "Description": "Honda CR-V front view"},
    {"FileName": "CR-V(2).jpg", "FilePath": "images/CR-V(2).jpg", "Description": "Honda CR-V side view"},
    {"FileName": "CR-V(3).jpg", "FilePath": "images/CR-V(3).jpg", "Description": "Honda CR-V rear view"},

    {"FileName": "3-series(1).jpg", "FilePath": "images/3-series.jpg", "Description": "BMW 3 Series front view"},
    {"FileName": "3-series(2).jpg", "FilePath": "images/3-series(2).jpg", "Description": "BMW 3 Series side view"},
    {"FileName": "3-series(3).jpg", "FilePath": "images/3-series(3).jpg", "Description": "BMW 3 Series rear view"},

    {"FileName": "X5.jpg", "FilePath": "images/X5(1).jpg", "Description": "BMW X5 front view"},
    {"FileName": "X5(2).jpg", "FilePath": "images/X5(2).jpg", "Description": "BMW X5 back view"},

    {"FileName": "I4(1).jpg", "FilePath": "images/i4(1).jpg", "Description": "BMW I4 front view"},
    {"FileName": "I4(2).jpg", "FilePath": "images/i4(2).jpg", "Description": "BMW I4 side view"},
    {"FileName": "I4(3).jpg", "FilePath": "images/i4(3).jpg", "Description": "BMW I4 rear view"},

    {"FileName": "Model_S(1).jpg", "FilePath": "images/ModelS(1).jpg", "Description": "Tesla Model S front view"},
    {"FileName": "Model_S(2).jpg", "FilePath": "images/ModelS(2).jpg", "Description": "Tesla Model S side view"},
    {"FileName": "Model_S(3).jpg", "FilePath": "images/ModelS(3).jpg", "Description": "Tesla Model S rear view"},

    {"FileName": "Model_3(1).jpg", "FilePath": "images/Model3(1).jpg", "Description": "Tesla Model 3 front view"},
    {"FileName": "Model_3(2).jpg", "FilePath": "images/Model3(2).jpg", "Description": "Tesla Model 3 side view"},
    {"FileName": "Model_3(3).jpg", "FilePath": "images/Model3(3).jpg", "Description": "Tesla Model 3 top view"},

    {"FileName": "Model_Y(1).jpg", "FilePath": "images/ModelY(1).jpg", "Description": "Tesla Model Y front view"},
    {"FileName": "Model_Y(2).jpg", "FilePath": "images/ModelY(2).jpg", "Description": "Tesla Model Y side view"},
    {"FileName": "Model_Y(3).jpg", "FilePath": "images/ModelY(3).jpg", "Description": "Tesla Model Y rear view"},

    {"FileName": "C-Class(1).jpg", "FilePath": "images/C-Class(1).jpg", "Description": "Mercedes C-Class front view"},
    {"FileName": "C-Class(2).jpg", "FilePath": "images/C-Class(2).jpg", "Description": "Mercedes C-Class side view"},
    
    {"FileName": "E-Class(1).jpg", "FilePath": "images/E-Class(1).jpg", "Description": "Mercedes E-Class front view"},
    {"FileName": "E-Class(2).jpg", "FilePath": "images/E-Class(2).jpg", "Description": "Mercedes E-Class side view"},
    {"FileName": "E-Class(3).jpg", "FilePath": "images/E-Class(3).jpg", "Description": "Mercedes E-Class rear view"},

    {"FileName": "S-Class(1).jpg", "FilePath": "images/S-Class(1).jpg", "Description": "Mercedes S-Class front view"},
    {"FileName": "S-Class(2).jpg", "FilePath": "images/S-Class(2).jpg", "Description": "Mercedes S-Class side view"},
    {"FileName": "S-Class(3).jpg", "FilePath": "images/S-Class(3).jpg", "Description": "Mercedes S-Class rear view"},

    {"FileName": "GLC(1).jpg", "FilePath": "images/GLC(1).jpg", "Description": "Mercedes GLC front view"},
    {"FileName": "GLC(2).jpg", "FilePath": "images/GLC(2).jpg", "Description": "Mercedes GLC side view"},
    {"FileName": "GLC(3).jpg", "FilePath": "images/GLC(3).jpg", "Description": "Mercedes GLC rear view"},

    {"FileName": "GLE(1).jpg", "FilePath": "images/GLE(1).jpg", "Description": "Mercedes GLE front view"},
    {"FileName": "GLE(2).jpg", "FilePath": "images/GLE(2).jpg", "Description": "Mercedes GLE side view"},
    {"FileName": "GLE(3).jpg", "FilePath": "images/GLE(3).jpg", "Description": "Mercedes GLE rear view"},

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
    {"FileName": "Senna2024Orange.jpg", "FilePath": "images/Senna2024Orange.jpg", "Description": "Senna 2024 Orange"},

    {"FileName": "bolide-1.jpg", "FilePath": "images/bolide-1.jpg", "Description": "Gallery"},
    {"FileName": "bolide-2.webp", "FilePath": "images/bolide-2.webp", "Description": "Gallery"},
    {"FileName": "bolide-3.jpg", "FilePath": "images/bolide-3.jpg", "Description": "Gallery"},

    {"FileName": "veyron-1.webp", "FilePath": "images/veyron-1.webp", "Description": "Gallery"},
    {"FileName": "veyron-2.jpg", "FilePath": "images/veyron-2.jpg", "Description": "Gallery"},
    {"FileName": "veyron-3.webp", "FilePath": "images/veyron-3.webp", "Description": "Gallery"},

    {"FileName": "cento-1.jpg", "FilePath": "images/cento-1.jpg", "Description": "Gallery"},
    {"FileName": "cento-2.jpg", "FilePath": "images/cento-2.jpg", "Description": "Gallery"},
    {"FileName": "cento-3.jpg", "FilePath": "images/cento-3.jpg", "Description": "Gallery"},

    {"FileName": "divo-1.jpg", "FilePath": "images/divo-1.jpg", "Description": "Gallery"},
    {"FileName": "divo-2.jpg", "FilePath": "images/divo-2.jpg", "Description": "Gallery"},
    {"FileName": "divo-3.jpg", "FilePath": "images/divo-3.jpg", "Description": "Gallery"},

    {"FileName": "chiron-1.jpg", "FilePath": "images/chiron-1.jpg", "Description": "Gallery"},
    {"FileName": "chiron-1.webp", "FilePath": "images/chiron-1.webp", "Description": "Gallery"},
    {"FileName": "chiron-2.jpg", "FilePath": "images/chiron-2.jpg", "Description": "Gallery"},

    {"FileName": "austral-1.jpg", "FilePath": "images/austral-1.jpg", "Description": "Gallery"},

    {"FileName": "arkana-1.jpg", "FilePath": "images/arkana-1.jpg", "Description": "Gallery"},

    {"FileName": "captur-1.jpg", "FilePath": "images/captur-1.jpg", "Description": "Gallery"},

    {"FileName": "megane-1.jpg", "FilePath": "images/megane-1.jpg", "Description": "Gallery"},

    {"FileName": "clio-1.jpg", "FilePath": "images/clio-1.jpg", "Description": "Gallery"},
    {"FileName": "clio-2.webp", "FilePath": "images/clio-2.webp", "Description": "Gallery"},
    {"FileName": "clio-3.webp", "FilePath": "images/clio-3.webp", "Description": "Gallery"},

    {"FileName": "ono-1.jpg", "FilePath": "images/ono-1.jpg", "Description": "Gallery"},
    {"FileName": "ono-2.webp", "FilePath": "images/ono-2.webp", "Description": "Gallery"},
    {"FileName": "ono-3.webp", "FilePath": "images/ono-3.webp", "Description": "Gallery"},

    {"FileName": "gemera-1.jpg", "FilePath": "images/gemera-1.jpg", "Description": "Gallery"},
    {"FileName": "gemera-2.jpg", "FilePath": "images/gemera-2.jpg", "Description": "Gallery"},
    {"FileName": "gemera-3.jpg", "FilePath": "images/gemera-3.jpg", "Description": "Gallery"},

    {"FileName": "agerars-1.jpg", "FilePath": "images/agerars-1.jpg", "Description": "Gallery"},
    {"FileName": "agerars-2.jpg", "FilePath": "images/agerars-2.jpg", "Description": "Gallery"},
    {"FileName": "agerars-3.jpg", "FilePath": "images/agerars-3.jpg", "Description": "Gallery"},

    {"FileName": "regera-1.jpg", "FilePath": "images/regera-1.jpg", "Description": "Gallery"},
    {"FileName": "regera-2.jpg", "FilePath": "images/regera-2.jpg", "Description": "Gallery"},
    {"FileName": "regera-3.jpg", "FilePath": "images/regera-3.jpg", "Description": "Gallery"},

    {"FileName": "jesko-1.jpg", "FilePath": "images/jesko-1.jpg", "Description": "Gallery"},
    {"FileName": "jesko-2.jpg", "FilePath": "images/jesko-2.jpg", "Description": "Gallery"},
    {"FileName": "jesko-3.jpg", "FilePath": "images/jesko-3.jpg", "Description": "Gallery"},

    {"FileName": "zondacinque-1.jpg", "FilePath": "images/zondacinque-1.jpg", "Description": "Gallery"},
    {"FileName": "zondacinque-2.jpg", "FilePath": "images/zondacinque-2.jpg", "Description": "Gallery"},
    {"FileName": "zondacinque-3.jpg", "FilePath": "images/zondacinque-3.jpg", "Description": "Gallery"},

    {"FileName": "utopia-1.jpg", "FilePath": "images/utopia-1.jpg", "Description": "Gallery"},
    {"FileName": "utopia-2.jpg", "FilePath": "images/utopia-2.jpg", "Description": "Gallery"},
    {"FileName": "utopia-3.jpg", "FilePath": "images/utopia-3.jpg", "Description": "Gallery"},

    {"FileName": "huayra-1.jpg", "FilePath": "images/huayra-1.jpg", "Description": "Gallery"},
    {"FileName": "huayra-2.jpg", "FilePath": "images/huayra-2.jpg", "Description": "Gallery"},
    {"FileName": "huayra-3.jpg", "FilePath": "images/huayra-3.jpg", "Description": "Gallery"},

    {"FileName": "huayrabc-1.jpg", "FilePath": "images/huayrabc-1.jpg", "Description": "Gallery"},
    {"FileName": "huayrabc-2.jpg", "FilePath": "images/huayrabc-2.jpg", "Description": "Gallery"},
    {"FileName": "huayrabc-3.jpg", "FilePath": "images/huayrabc-3.jpg", "Description": "Gallery"},

    {"FileName": "zondar-1.jpg", "FilePath": "images/zondar-1.jpg", "Description": "Gallery"},
    {"FileName": "zondar-2.jpg", "FilePath": "images/zondar-2.jpg", "Description": "Gallery"},
    {"FileName": "zondar-3.jpg", "FilePath": "images/zondar-3.jpg", "Description": "Gallery"}

    
]

manufacturers = [
    {
        "manufacturerName": "Ford",
        "established": "1903-06-16",
        "headquarters": "Dearborn, Michigan, USA",
        "description": "American multinational automaker producing cars, trucks, and SUVs.",
        "logoID": 1,
    },
    {
        "manufacturerName": "Toyota",
        "established": "1937-08-28",
        "headquarters": "Toyota City, Japan",
        "description": "Japanese automaker known for reliability and hybrid technology.",
        "logoID": 2,
    },
    {
        "manufacturerName": "Honda",
        "established": "1948-09-24",
        "headquarters": "Minato, Tokyo, Japan",
        "description": "Japanese manufacturer of cars, motorcycles, and power equipment.",
        "logoID": 3,
    },
    {
        "manufacturerName": "BMW",
        "established": "1916-03-07",
        "headquarters": "Munich, Germany",
        "description": "German luxury vehicle and motorcycle manufacturer.",
        "logoID": 4,
    },
    {
        "manufacturerName": "Tesla",
        "established": "2003-07-01",
        "headquarters": "Palo Alto, California, USA",
        "description": "Electric vehicle and clean energy company.",
        "logoID": 5,
    },
    {
        "manufacturerName": "Mercedes",
        "established": "1926-06-28",
        "headquarters": "Stuttgart, Germany",
        "description": "Luxury vehicles and automotive engineering company.",
        "logoID": 6
    },
    {
        "manufacturerName": "Audi",
        "established": "1909-07-16",
        "headquarters": "Ingolstadt, Germany",
        "description": "Premium automobile manufacturer known for advanced technology.",
        "logoID": 7
    },
    {
        "manufacturerName": "Ferrari",
        "established": "1939-09-13",
        "headquarters": "Maranello, Italy",
        "description": "High-performance sports car manufacturer.",
        "logoID": 8
    },
    {
        "manufacturerName": "Lamborghini",
        "established": "1963-10-30",
        "headquarters": "Sant'Agata Bolognese, Italy",
        "description": "Italian manufacturer of luxury supercars.",
        "logoID": 9
    },
    {

        "manufacturerName": "Volkswagen",
        "established": "1937-05-28",
        "headquarters": "Wolfsburg, Germany",
        "description": "Global automobile manufacturer producing a wide range of vehicles.",
        "logoID": 10
    },
    {

        "manufacturerName": "McLaren",
        "established": "1985-09-02",
        "headquarters": "Woking, Surrey, United Kingdom",
        "description": "British manufacturer of high-performance supercars.",
        "logoID": 11
    },
    {

        "manufacturerName": "Pagani",
        "established": "1992-01-01",
        "headquarters": "San Cesario sul Panaro, Italy",
        "description": "Italian manufacturer of exclusive hypercars.",
        "logoID": 12
    },
    {

        "manufacturerName": "Koenigsegg",
        "established": "1994-08-12",
        "headquarters": "Ängelholm, Sweden",
        "description": "Swedish manufacturer of high-performance hypercars.",
        "logoID": 13
    },
    {

        "manufacturerName": "Renault",
        "established": "1899-02-25",
        "headquarters": "Boulogne-Billancourt, France",
        "description": "French multinational automobile manufacturer.",
        "logoID": 14
    },
    {

        "manufacturerName": "Bugatti",
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

    {"model": "3 Series", "year": 2026, "baseMSRP": 41900, "manufacturerID": 4},
    {"model": "X5", "year": 2026, "baseMSRP": 60900, "manufacturerID": 4},
    {"model": "i4", "year": 2021, "baseMSRP": 51600, "manufacturerID": 4},

    {"model": "Model S", "year": 2012, "baseMSRP": 79990, "manufacturerID": 5},
    {"model": "Model 3", "year": 2016, "baseMSRP": 39990, "manufacturerID": 5},
    {"model": "Model Y", "year": 2020, "baseMSRP": 49990, "manufacturerID": 5},

    {"model": "C-Class", "year": 1993, "baseMSRP": 43900, "manufacturerID": 6},
    {"model": "E-Class", "year": 2023, "baseMSRP": 57900, "manufacturerID": 6},
    {"model": "S-Class", "year": 2026, "baseMSRP": 114500, "manufacturerID": 6},
    {"model": "GLC", "year": 2024, "baseMSRP": 47450, "manufacturerID": 6},
    {"model": "GLE", "year": 2015, "baseMSRP": 62900, "manufacturerID": 6},

    {"model": "A4", "year": 1994, "baseMSRP": 41900, "manufacturerID": 7},
    {"model": "A6", "year": 2018, "baseMSRP": 57900, "manufacturerID": 7},
    {"model": "Q5", "year": 2025, "baseMSRP": 45500, "manufacturerID": 7},
    {"model": "Q7", "year": 2026, "baseMSRP": 59900, "manufacturerID": 7},
    {"model": "R8", "year": 2006, "baseMSRP": 161000, "manufacturerID": 7},

    {"model": "488 GTB", "year": 2015, "baseMSRP": 262000, "manufacturerID": 8},
    {"model": "F8 Tributo", "year": 2019, "baseMSRP": 283950, "manufacturerID": 8},
    {"model": "Roma", "year": 2019, "baseMSRP": 222620, "manufacturerID": 8},
    {"model": "SF90 Stradale", "year": 2019, "baseMSRP": 524815, "manufacturerID": 8},
    {"model": "812 Superfast", "year": 2017, "baseMSRP": 340000, "manufacturerID": 8},

    {"model": "Huracán", "year": 2014, "baseMSRP": 249865, "manufacturerID": 9},
    {"model": "Aventador", "year": 2011, "baseMSRP": 507353, "manufacturerID": 9},
    {"model": "Urus", "year": 2023, "baseMSRP": 237848, "manufacturerID": 9},
    {"model": "Revuelto", "year": 2023, "baseMSRP": 608358, "manufacturerID": 9},
    {"model": "Sian", "year": 2020, "baseMSRP": 3300000, "manufacturerID": 9},

    {"model": "Golf", "year": 2025, "baseMSRP": 24500, "manufacturerID": 10},
    {"model": "Passat", "year": 2023, "baseMSRP": 29900, "manufacturerID": 10},
    {"model": "Tiguan", "year": 2025, "baseMSRP": 28900, "manufacturerID": 10},
    {"model": "Atlas", "year": 2017, "baseMSRP": 36800, "manufacturerID": 10},
    {"model": "ID.4", "year": 2026, "baseMSRP": 39995, "manufacturerID": 10},

    {"model": "720S", "year": 2017, "baseMSRP": 310500, "manufacturerID": 11},
    {"model": "Artura", "year": 2021, "baseMSRP": 233000, "manufacturerID": 11},
    {"model": "765LT", "year": 2021, "baseMSRP": 382500, "manufacturerID": 11},
    {"model": "GT", "year": 2019, "baseMSRP": 210000, "manufacturerID": 11},
    {"model": "Senna", "year": 2018, "baseMSRP": 1000000, "manufacturerID": 11},
    
    {"model": "Huayra", "year": 2011, "baseMSRP": 3500000, "manufacturerID": 12},
    {"model": "Zonda R", "year": 2009, "baseMSRP": 1800000, "manufacturerID": 12},
    {"model": "Huayra BC", "year": 2017, "baseMSRP": 2800000, "manufacturerID": 12},
    {"model": "Utopia", "year": 2023, "baseMSRP": 2500000, "manufacturerID": 12},
    {"model": "Zonda Cinque", "year": 2024, "baseMSRP": 2300000, "manufacturerID": 12},

    {"model": "Jesko", "year": 2023, "baseMSRP": 3000000, "manufacturerID": 13},
    {"model": "Regera", "year": 2015, "baseMSRP": 1900000, "manufacturerID": 13},
    {"model": "Agera RS", "year": 2010, "baseMSRP": 2500000, "manufacturerID": 13},
    {"model": "Gemera", "year": 2024, "baseMSRP": 1700000, "manufacturerID": 13},
    {"model": "One:1", "year": 2022, "baseMSRP": 2800000, "manufacturerID": 13},

    {"model": "Clio", "year": 2025, "baseMSRP": 19000, "manufacturerID": 14},
    {"model": "Megane", "year": 2025, "baseMSRP": 24000, "manufacturerID": 14},
    {"model": "Captur", "year": 2025, "baseMSRP": 23000, "manufacturerID": 14},
    {"model": "Arkana", "year": 2025, "baseMSRP": 27000, "manufacturerID": 14},
    {"model": "Austral", "year": 2025, "baseMSRP": 30000, "manufacturerID": 14},

    {"model": "Chiron", "year": 2016, "baseMSRP": 3000000, "manufacturerID": 15},
    {"model": "Divo", "year": 2020, "baseMSRP": 5800000, "manufacturerID": 15},
    {"model": "Centodieci", "year": 2022, "baseMSRP": 9000000, "manufacturerID": 15},
    {"model": "Veyron Super Sport", "year": 2005, "baseMSRP": 2400000, "manufacturerID": 15},
    {"model": "Bolide", "year": 2025, "baseMSRP": 4700000, "manufacturerID": 15}

]
# images for cars, not the actual car images rn.. to be changed
car_images = [
    # F150
    {"carID": 1, "imageID": 16, "role": "gallery"},
    {"carID": 1, "imageID": 17, "role": "gallery"},
    {"carID": 1, "imageID": 18, "role": "gallery"},

    # Mustang
    {"carID": 2, "imageID": 19, "role": "gallery"},
    {"carID": 2, "imageID": 20, "role": "gallery"},
    {"carID": 2, "imageID": 21, "role": "gallery"},

    # Explorer
    {"carID": 3, "imageID": 22, "role": "gallery"},
    {"carID": 3, "imageID": 23, "role": "gallery"},
    {"carID": 3, "imageID": 24, "role": "gallery"},

    # Camry
    {"carID": 4, "imageID": 25, "role": "gallery"},
    {"carID": 4, "imageID": 26, "role": "gallery"},
    {"carID": 4, "imageID": 27, "role": "gallery"},

    # Corolla
    {"carID": 5, "imageID": 28, "role": "gallery"},
    {"carID": 5, "imageID": 29, "role": "gallery"},

    # RAV4
    {"carID": 6, "imageID": 30, "role": "gallery"},
    {"carID": 6, "imageID": 31, "role": "gallery"},
    {"carID": 6, "imageID": 32, "role": "gallery"},

    # civic
    {"carID": 7, "imageID": 33, "role": "gallery"},
    {"carID": 7, "imageID": 34, "role": "gallery"},
    {"carID": 7, "imageID": 35, "role": "gallery"},

    # Accord
    {"carID": 8, "imageID": 36, "role": "gallery"},
    {"carID": 8, "imageID": 37, "role": "gallery"},
    {"carID": 8, "imageID": 38, "role": "gallery"},

    # CR-V 
    {"carID": 9, "imageID": 39, "role": "gallery"},
    {"carID": 9, "imageID": 40, "role": "gallery"},
    {"carID": 9, "imageID": 41, "role": "gallery"},

    # 3-series
    {"carID": 10, "imageID": 42, "role": "gallery"},
    {"carID": 10, "imageID": 43, "role": "gallery"},
    {"carID": 10, "imageID": 44, "role": "gallery"},

    # X5
    {"carID": 11, "imageID": 45, "role": "gallery"},
    {"carID": 11, "imageID": 46, "role": "gallery"},

    #I4
    {"carID": 12, "imageID": 47, "role": "gallery"},
    {"carID": 12, "imageID": 48, "role": "gallery"},
    {"carID": 12, "imageID": 49, "role": "gallery"},

    #Model_S
    {"carID": 13, "imageID": 50, "role": "gallery"},
    {"carID": 13, "imageID": 51, "role": "gallery"},
    {"carID": 13, "imageID": 52, "role": "gallery"},

    #Model_3
    {"carID": 14, "imageID": 53, "role": "gallery"},
    {"carID": 14, "imageID": 54, "role": "gallery"},
    {"carID": 14, "imageID": 55, "role": "gallery"},

    #Model_Y
    {"carID": 15, "imageID": 56, "role": "gallery"},
    {"carID": 15, "imageID": 57, "role": "gallery"},
    {"carID": 15, "imageID": 58, "role": "gallery"},

    #C-Class
    {"carID": 16, "imageID": 59, "role": "gallery"},
    {"carID": 16, "imageID": 60, "role": "gallery"},

    # E-Class
    {"carID": 17, "imageID": 61, "role": "gallery"},
    {"carID": 17, "imageID": 62, "role": "gallery"},
    {"carID": 17, "imageID": 63, "role": "gallery"},

    # S-Class
    {"carID": 18, "imageID": 64, "role": "gallery"},
    {"carID": 18, "imageID": 65, "role": "gallery"},
    {"carID": 18, "imageID": 66, "role": "gallery"},

    #GLC 
    {"carID": 19, "imageID": 67, "role": "gallery"},
    {"carID": 19, "imageID": 68, "role": "gallery"},
    {"carID": 19, "imageID": 69, "role": "gallery"},

    #GLE
    {"carID": 20, "imageID": 70, "role": "gallery"},
    {"carID": 20, "imageID": 71, "role": "gallery"},
    {"carID": 20, "imageID": 72, "role": "gallery"},

    #A4
    {"carID": 21, "imageID": 73, "role": "gallery"},
    {"carID": 21, "imageID": 74, "role": "gallery"},
    {"carID": 21, "imageID": 75, "role": "gallery"},

    #A6
    {"carID": 22, "imageID": 76, "role": "gallery"},
    {"carID": 22, "imageID": 77, "role": "gallery"},
    {"carID": 22, "imageID": 78, "role": "gallery"},

    #Q5
    {"carID": 23, "imageID": 79, "role": "gallery"},
    {"carID": 23, "imageID": 80, "role": "gallery"},
    {"carID": 23, "imageID": 81, "role": "gallery"},

    #Q7
    {"carID": 24, "imageID": 82, "role": "gallery"},
    {"carID": 24, "imageID": 83, "role": "gallery"},
    {"carID": 24, "imageID": 84, "role": "gallery"},

    #R8
    {"carID": 25, "imageID": 85, "role": "gallery"},
    {"carID": 25, "imageID": 86, "role": "gallery"},
    {"carID": 25, "imageID": 87, "role": "gallery"},

    #488GTB
    {"carID": 26, "imageID": 88, "role": "gallery"},
    {"carID": 26, "imageID": 89, "role": "gallery"},
    {"carID": 26, "imageID": 90, "role": "gallery"},

    #F8
    {"carID": 27, "imageID": 91, "role": "gallery"},
    {"carID": 27, "imageID": 92, "role": "gallery"},
    {"carID": 27, "imageID": 93, "role": "gallery"},

    #Roma
    {"carID": 28, "imageID": 94, "role": "gallery"},
    {"carID": 28, "imageID": 95, "role": "gallery"},
    {"carID": 28, "imageID": 96, "role": "gallery"},

    #SF90
    {"carID": 29, "imageID": 97, "role": "gallery"},
    {"carID": 29, "imageID": 98, "role": "gallery"},
    {"carID": 29, "imageID": 99, "role": "gallery"},

    #B12
    {"carID": 30, "imageID": 100, "role": "gallery"},
    {"carID": 30, "imageID": 101, "role": "gallery"},
    {"carID": 30, "imageID": 102, "role": "gallery"},

    # Huracan
    {"carID": 31, "imageID": 103, "role": "gallery"},
    {"carID": 31, "imageID": 104, "role": "gallery"},
    {"carID": 31, "imageID": 105, "role": "gallery"},

    # Aventador
    {"carID": 32, "imageID": 106, "role": "gallery"},
    {"carID": 32, "imageID": 107, "role": "gallery"},
    {"carID": 32, "imageID": 108, "role": "gallery"},

    # Urus
    {"carID": 33, "imageID": 109, "role": "gallery"},
    {"carID": 33, "imageID": 110, "role": "gallery"},
       
    #Revuelto
    {"carID": 34, "imageID": 111, "role": "gallery"},
    {"carID": 34, "imageID": 112, "role": "gallery"},
    {"carID": 34, "imageID": 113, "role": "gallery"},

    #sian
    {"carID": 35, "imageID": 114, "role": "gallery"},

    #golf
    {"carID": 36, "imageID": 115, "role": "gallery"},
    {"carID": 36, "imageID": 116, "role": "gallery"},
    {"carID": 36, "imageID": 117, "role": "gallery"},

    #Passat
    {"carID": 37, "imageID": 118, "role": "gallery"},
    {"carID": 37, "imageID": 119, "role": "gallery"},
    {"carID": 37, "imageID": 120, "role": "gallery"},

    #Tiguan
    {"carID": 38, "imageID": 121, "role": "gallery"},
    {"carID": 38, "imageID": 122, "role": "gallery"},
    {"carID": 38, "imageID": 123, "role": "gallery"},

    #Atlas
    {"carID": 39, "imageID": 124, "role": "gallery"},
    {"carID": 39, "imageID": 125, "role": "gallery"},
    {"carID": 39, "imageID": 126, "role": "gallery"},

    #ID4
    {"carID": 40, "imageID": 127, "role": "gallery"},
    {"carID": 40, "imageID": 128, "role": "gallery"},
    {"carID": 40, "imageID": 129, "role": "gallery"},

    #720S
    {"carID": 41, "imageID": 130, "role": "gallery"},
    {"carID": 41, "imageID": 131, "role": "gallery"},
    {"carID": 41, "imageID": 132, "role": "gallery"},

    #Artura
    {"carID": 42, "imageID": 133, "role": "gallery"},
    {"carID": 42, "imageID": 134, "role": "gallery"},
    {"carID": 42, "imageID": 135, "role": "gallery"},

    #765
    {"carID": 43, "imageID": 136, "role": "gallery"},
    {"carID": 43, "imageID": 137, "role": "gallery"},
    {"carID": 43, "imageID": 138, "role": "gallery"},

    #GT
    {"carID": 44, "imageID": 139, "role": "gallery"},
    {"carID": 44, "imageID": 140, "role": "gallery"},
    {"carID": 44, "imageID": 141, "role": "gallery"},

    #Senna
    {"carID": 45, "imageID": 142, "role": "gallery"},
    {"carID": 45, "imageID": 143, "role": "gallery"},
    {"carID": 45, "imageID": 144, "role": "gallery"},

    #Huayra
    {"carID": 46, "imageID": 188, "role": "gallery"},
    {"carID": 46, "imageID": 189, "role": "gallery"},
    {"carID": 46, "imageID": 190, "role": "gallery"},

    # Zonda R
    {"carID": 47, "imageID": 194, "role": "gallery"},
    {"carID": 47, "imageID": 195, "role": "gallery"},
    {"carID": 47, "imageID": 196, "role": "gallery"},

    #HuayraBC
    {"carID": 48, "imageID": 191, "role": "gallery"},
    {"carID": 48, "imageID": 192, "role": "gallery"},
    {"carID": 48, "imageID": 193, "role": "gallery"},

    #Utopia
    {"carID": 49, "imageID": 185, "role": "gallery"},
    {"carID": 49, "imageID": 186, "role": "gallery"},
    {"carID": 49, "imageID": 187, "role": "gallery"},

    #Zonda Cinque
    {"carID": 50, "imageID": 182, "role": "gallery"},
    {"carID": 50, "imageID": 183, "role": "gallery"},
    {"carID": 50, "imageID": 184, "role": "gallery"},

    # Jesko
    {"carID": 51, "imageID": 179, "role": "gallery"},
    {"carID": 51, "imageID": 180, "role": "gallery"},
    {"carID": 51, "imageID": 181, "role": "gallery"},

    #Regera
    {"carID": 52, "imageID": 176, "role": "gallery"},
    {"carID": 52, "imageID": 177, "role": "gallery"},
    {"carID": 52, "imageID": 178, "role": "gallery"},

    #AgeraRS
    {"carID": 53, "imageID": 173, "role": "gallery"},
    {"carID": 53, "imageID": 174, "role": "gallery"},
    {"carID": 53, "imageID": 175, "role": "gallery"},

    #Gemera
    {"carID": 54, "imageID": 170, "role": "gallery"},
    {"carID": 54, "imageID": 171, "role": "gallery"},
    {"carID": 54, "imageID": 172, "role": "gallery"},

    #One:1
    {"carID": 55, "imageID": 167, "role": "gallery"},
    {"carID": 55, "imageID": 168, "role": "gallery"},
    {"carID": 55, "imageID": 169, "role": "gallery"},

    #Clio
    {"carID": 56, "imageID": 164, "role": "gallery"},
    {"carID": 56, "imageID": 165, "role": "gallery"},
    {"carID": 56, "imageID": 166, "role": "gallery"},

    #Megane
    {"carID": 57, "imageID": 163, "role": "gallery"},
    
    #Captur
    {"carID": 58, "imageID": 162, "role": "gallery"},
    
    #Arkana
    {"carID": 59, "imageID": 161, "role": "gallery"},

    #Austral
    {"carID": 60, "imageID": 160, "role": "gallery"},
    
    #Chiron
    {"carID": 61, "imageID": 157, "role": "gallery"},
    {"carID": 61, "imageID": 158, "role": "gallery"},
    {"carID": 61, "imageID": 159, "role": "gallery"},

    #Divo
    {"carID": 62, "imageID": 154, "role": "gallery"},
    {"carID": 62, "imageID": 155, "role": "gallery"},
    {"carID": 62, "imageID": 156, "role": "gallery"},

    #Centodieci
    {"carID": 63, "imageID": 151, "role": "gallery"},
    {"carID": 63, "imageID": 152, "role": "gallery"},
    {"carID": 63, "imageID": 153, "role": "gallery"},

    #Veyron
    {"carID": 64, "imageID": 148, "role": "gallery"},
    {"carID": 64, "imageID": 149, "role": "gallery"},
    {"carID": 64, "imageID": 150, "role": "gallery"},

    #Bolide
    {"carID": 65, "imageID": 145, "role": "gallery"},
    {"carID": 65, "imageID": 146, "role": "gallery"},
    {"carID": 65, "imageID": 147, "role": "gallery"},

]
__all__ = ["images", "manufacturers", "cars"]
