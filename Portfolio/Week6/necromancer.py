import lib
from resource import Resources
from undead import Undead
from ritual import Ritual


class Necromancer:

    # Share the next ID so each necromancer gets a different number.
    """Keep track of a necromancer, its resources and its undead."""
    __next_id = 1

    def __init__(self, name: str, necrotic: int, spirit: int, bone: int, flesh: int, ectoplasm: int):
        """Set the starting resources and give the necromancer an ID."""

        self.__name = name if lib.is_valid_string(name) else "Name is error"
        self.__resource_object = Resources(
            necrotic, spirit, bone, flesh, ectoplasm)
        self.__collection = []

        self.__id = Necromancer.__next_id
        Necromancer.__next_id += 1

    def __str__(self):
        """Show the necromancer, resources and summoned undead."""

        message = ''
        resource = self.__resource_object

        for i in self.__collection:
            message += f"{i}\n"
        return (
            f"Necromancer {self.__name}, you have:\n"
            f"{resource.necrotic}Necrotic\n"
            f"{resource.spirit}Spirit\n"
            f"{resource.bone}Bone\n"
            f"{resource.flesh}Flesh\n"
            f"{resource.ectoplasm}Ectoplasm\n"
            f"Your collection of undead:\n{message}"
        )

    def get_name(self) -> str:
        """Gets the name of the Necromancer and returns it"""
        return self.__name

    def get_resource_object(self) -> Resources:
        """Gets the resource object and returns it"""
        return self.__resource_object

    def get_id(self) -> int:
        """Gets the ID of Necromancer and returns it"""
        return self.__id

    def get_collection(self) -> list:
        """Return a copy of the list of summoned undead."""
        return self.__collection.copy()

    id = property(get_id)
    name = property(get_name)
    resources = property(get_resource_object)
    collection = property(get_collection)

    def cast_ritual(self, ritual, undead_id) -> bool:
        """Pay for the ritual and add the undead to the collection.

        Return False for an invalid ritual, an ID already in use, or
        there are not enough resources.
        """

        if isinstance(ritual, Ritual):
            if lib.find_undead(undead_id, self.__collection) != False:
                print("Same ID with", lib.find_undead(
                    undead_id, self.__collection))
                return False

            # Only create the undead after paying for the ritual.
            if ritual.consume_ritual_resource(self.__resource_object):
                undead = ritual.create_undead(undead_id)
                self.__collection.append(undead)
                print("You casted", ritual, "summoned", undead)
                return True
            else:
                print("Insufficient resource")
                return False
        else:
            print("Ritual is error")
            return False

    def dismiss_undead(self, undead_id: int) -> bool:
        """Remove the undead by ID. Return True if it was found."""
        if lib.find_undead(undead_id, self.__collection) != False:
            self.__collection.remove(
                lib.find_undead(undead_id, self.__collection))
            return True

        print("No such undead")
        return False

    def level_undead(self, undead_id: int) -> None:
        """Level up the undead if its ID is in the collection."""
        if lib.find_undead(undead_id, self.__collection) != False:
            lib.find_undead(undead_id, self.__collection).level_up()
