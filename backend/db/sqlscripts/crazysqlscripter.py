"""
I cook like no one else,
guaranteed most abysmal sql scripter in the west.
"""

from sqlalchemy import text

str_limit = " LIMIT 200 OFFSET 0; "

str_orderT1_cfm_d = "ORDER BY c.year DESC, c.baseMSRP"
str_orderT1_cfm_a = "ORDER BY c.year ASC, c.baseMSRP"
str_orderT2_cfm_d = "ORDER BY c.baseMSRP DESC, c.year"
str_orderT2_cfm_a = "ORDER BY c.baseMSRP ASC, c.year"


car_from_manufacturer_base = """
    SELECT 
        c.carID,
        c.model,
        c.year,
        c.baseMSRP,
        c.manufacturerID,
        ci.carImageID,
        ci.addedAt,
        i.FilePath,
        i.FileName
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
    LEFT JOIN images i ON i.imageID = ci.imageID
    WHERE c.manufacturerID = :manufacturerID
"""

def custom_car_from_manu_script(order) -> text:

    # default 0 = descending c.year, 1 = ascending c.year, 2 = descending c.baseMSRP, 3 = ascending c.baseMSRP

    base_script = car_from_manufacturer_base

    if order == 0:
        final_script = base_script + str_orderT1_cfm_d + str_limit
    elif order == 1:
        final_script = base_script + str_orderT1_cfm_a + str_limit
    elif order == 2:
        final_script = base_script + str_orderT2_cfm_d + str_limit
    elif order == 3:
        final_script = base_script + str_orderT2_cfm_a + str_limit

    return text(final_script)

