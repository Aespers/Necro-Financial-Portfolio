from typing import Final
# constant for integer verify
MINIMUM_QUANTITY: Final[int] = 0

# The maximum amount of undead that can be controlled
MAX_UNDEAD = 100


# This function is used to verify integer quantity
def is_valid_quantity(value, minimum=MINIMUM_QUANTITY) -> bool:
    '''Returns a True or False, to check if the parameter is a valid quantity'''
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
        and value >= minimum
    )

# This function is used to verify strings


def is_valid_string(string) -> bool:
    '''Returns a True or False, checks if the parameter is a valid string'''
    return (
        isinstance(string, str)
        and string.strip() != ""
    )

# This function only checks if the parameter is an integer


def is_valid_integer(value) -> bool:
    '''Returns a True or False, checks if the parameter is a type integer'''

    return (
        isinstance(value, int)
        and not isinstance(value, bool)
    )

# Finds the undead by id


def find_undead(undead_id: int, collection_list: list) -> bool:
    '''Goes through the undead list, and finds the undead by the id, and returns the undead'''

    for i in collection_list:
        if undead_id == i.id:
            return i
    return False
