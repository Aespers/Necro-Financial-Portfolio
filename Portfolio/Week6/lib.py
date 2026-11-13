from typing import Final
# constant for integer verify
MINIMUM_QUANTITY: Final[int] = 0

# The maximum amount of undead that can be controlled
MAX_UNDEAD = 100


# This function is used to verify integer quantity
def is_valid_quantity(value, minimum=MINIMUM_QUANTITY) -> bool:
    """Check for an integer at or above the minimum."""
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
        and value >= minimum
    )

# This function is used to verify strings


def is_valid_string(string) -> bool:
    """Check that the value is a string with some text."""
    return (
        isinstance(string, str)
        and string.strip() != ""
    )

# This function only checks if the parameter is an integer


def is_valid_integer(value) -> bool:
    """Check for an integer without accepting booleans."""

    return (
        isinstance(value, int)
        and not isinstance(value, bool)
    )

# Finds the undead by id


def find_undead(undead_id: int, collection_list: list) -> bool:
    """Return the undead with this ID, or False if none is found."""

    for i in collection_list:
        if undead_id == i.id:
            return i
    return False
