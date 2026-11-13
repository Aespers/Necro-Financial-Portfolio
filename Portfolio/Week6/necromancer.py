import lib
from resource import Resources
from undead import Undead
from ritual import Ritual


class Necromancer:

    # This is a variable declare to make the Necromancer's ID to automatically increment every time an necromancer object is created
    __next_id = 1

    def __init__(self, name: str, necrotic: int, spirit: int, bone: int, flesh: int, ectoplasm: int):
        """Initializes the Necromancer.
        Takes the name of the Necromancer, and enters the amount of resource the Necromancer have, and stores it in a resource object
        The Necromancer id is given automatically every Necromancer object created, increments by 1
        The collection list stores a collection of the Necromancer's collection of summoned undead
        """

        self.__name = name if lib.is_valid_string(name) else "Name is error"
        self.__resource_object = Resources(
            necrotic, spirit, bone, flesh, ectoplasm)
        self.__collection = []

        # This increments the Necromancer ID
        self.__id = Necromancer.__next_id
        Necromancer.__next_id += 1

    def __str__(self):
        """Returns a Necromancer"""

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
        """Gets the collection of Necromancer's summoned undead and returns it"""
        return self.__collection.copy()

    id = property(get_id)
    name = property(get_name)
    resources = property(get_resource_object)
    collection = property(get_collection)

    def cast_ritual(self, ritual, undead_id) -> bool:
        """
        This function creates an Undead object by casting a ritual

        Checks if the parameter entered is a type ritual
        Checks if the entered undead ID clashes with other undead

        Checks if the amount of resources needed for ritual exists, than creates the undead through the ritual method
        Adds the created undead to the collection list

        Returns false and prints a message if any of the requirements are not met
        """

        if isinstance(ritual, Ritual):
            if lib.find_undead(undead_id, self.__collection) != False:
                print("Same ID with", lib.find_undead(
                    undead_id, self.__collection))
                return False

            # checks for resource
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
        '''
        Removes the undead from the collection list, if it exists
        Returns true if successfully remove, returns false if the undead intended to delete do not exist
        '''
        if lib.find_undead(undead_id, self.__collection) != False:
            self.__collection.remove(
                lib.find_undead(undead_id, self.__collection))
            return True

        print("No such undead")
        return False

    def level_undead(self, undead_id: int) -> None:
        '''
        Level up the undead using the level up function
        '''
        if lib.find_undead(undead_id, self.__collection) != False:
            lib.find_undead(undead_id, self.__collection).level_up()
