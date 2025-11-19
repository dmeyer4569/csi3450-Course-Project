"""
anything edit related to the db goes here... if this gets too big I might split it who knows :p
you will only be able to edit manufacturer and cars, idk why you should be able to edit images... 
might make something to edit assigned images to cars later :D
"""

from sqlalchemy import text

# I'm lazy and dont wanna think too much about this. so will make this
# seems the simplest and most straight forward way to do it <3 Python


# edit manufacturrere
manu_add_name = "manufacturerName = :manufacturerName, "
manu_add_established = "established = :established, "
manu_add_headquarters = "headquarters = :headquarters, "
manu_add_description = "description = :description, "
manu_add_where = "WHERE manufacturerID = :manufacturerID"

# manufacturer base
base_manufacturer ="UPDATE manufacturers SET "

def edit_manufacturer_script(manufacturerID, manufacturerName, established, headquarters, description) -> text:
    final_script = base_manufacturer
    to_add = ""

    if manufacturerName is not None:
        to_add += manu_add_name
    if established is not None:
        to_add += manu_add_established
    if headquarters is not None:
        to_add += manu_add_headquarters
    if description is not None:
        to_add += manu_add_description

    # remove last comma and space
    if to_add.endswith(", "):
        to_add = to_add[:-2] + " "

    final_script += to_add + manu_add_where

    return text(final_script)
# edit car

# stuff to add conditionally
add_model = "model = :model, "
add_year = "year = :year, "
add_baseMSRP = "baseMSRP = :baseMSRP, "
add_manufacturerID = "manufacturerID = :manufacturerID, "
add_where = "WHERE carID = :carID"

# base car
base_car = "UPDATE cars SET "

def edit_car_script(model, year, baseMSRP, manufacturerID) -> text:
    final_script = base_car
    to_add = ""

    if model is not None:
        to_add += add_model
    if year is not None:
        to_add += add_year
    if baseMSRP is not None:
        to_add += add_baseMSRP
    if manufacturerID is not None:
        to_add += add_manufacturerID

    # remove last comma and space
    if to_add.endswith(", "):
        to_add = to_add[:-2] + " "

    final_script += to_add + add_where

    return text(final_script)