from typing import Final
#constant for integer verify
MINIMUM_QUANTITY: Final[int] = 0


#constants for undead
MIN_HEALTH = 10
MAX_HEALTH = 1000

MIN_POWER = 10
MAX_POWER = 1000

MAX_LEVEL = 100
MIN_LEVEL = 1

HEALTH_GAIN = 10
POWER_GAIN = 10
LEVEL_GAIN = 1


#The maximum amount of undead that can be controlled
MAX_UNDEAD = 100


#This function is used to verify integer quantity
def is_valid_quantity(value, minimum = MINIMUM_QUANTITY) -> bool:
    return(
        isinstance(value, int)
        and not isinstance(value, bool)
        and value >= minimum
    )

#This function is used to verify strings
def is_valid_string(string) -> bool:
    return(
        isinstance(string, str)
        and string.strip() != ""
    )

#This function only checks if the parameter is an integer
def is_valid_integer(value) -> bool:
    return(
        isinstance(value, int)
        and not isinstance(value, bool)
    )

#Finds the undead by id
def find_undead(undead_id:int, collection_list:list) -> bool:
    for i in collection_list:
        if undead_id == i.id:
            return i
    return False