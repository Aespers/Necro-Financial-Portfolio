import lib
from resource import Resources
from undead import Undead
from ritual import Ritual


class Necromancer:

    def __init__(self, name: str, necrotic):
        self.__name = name if lib.is_valid_string(name) else "Name is error"
        self.__resource_object = Resources(10, 10, 10, 10, 50)
        self.__collection = []
        self.__id = id if lib.is_valid_integer(id) else "Error"

    def get_name(self) -> str:
        return self.__name

    def get_resource_object(self) -> Resources:
        return self.__resource_object

    def get_id(self) -> int:
        return self.__id

    def get_collection(self) -> list:
        return self.__collection

    id = property(get_id)
    name = property(get_name)
    resources = property(get_resource_object)
    collection = property(get_collection)

    def cast_ritual(self, ritual, undead_id) -> bool:
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

    def dismiss_undead(self, undead_id: int):
        if lib.find_undead(undead_id, self.__collection) != False:
            self.__collection.remove(
                lib.find_undead(undead_id, self.__collection))
            return True

        print("No such undead")
        return False

    def level_undead(self, undead_id: int):
        if lib.find_undead(undead_id, self.__collection) != False:
            lib.find_undead(undead_id, self.__collection).level_up()
