from undead import Undead
from resource import Resources
import lib as lib

class Ritual:

    def __init__(self, ritual_name:str, undead_name:str, health:int, power:int, necrotic:int, spirit:int, bone:int, flesh:int, ectoplasm:int) -> None:
        self.__ritual_name = ritual_name if lib.is_valid_string(ritual_name) else "Error ritual name"
        self.__undead_name = undead_name if lib.is_valid_string(undead_name) else "Error undead name"
        self.__health = health if lib.is_valid_quantity(health, lib.MIN_HEALTH) and health <= lib.MAX_HEALTH else lib.MIN_HEALTH
        self.__power = power if lib.is_valid_quantity(power, lib.MIN_POWER) and power <= lib.MAX_POWER else lib.MIN_POWER
        self.__necrotic = necrotic if lib.is_valid_quantity(necrotic, lib.MINIMUM_QUANTITY) else lib.MINIMUM_QUANTITY
        self.__spirit = spirit if lib.is_valid_quantity(spirit, lib.MINIMUM_QUANTITY) else lib.MINIMUM_QUANTITY
        self.__bone = bone if lib.is_valid_quantity(bone, lib.MINIMUM_QUANTITY) else lib.MINIMUM_QUANTITY
        self.__flesh = flesh if lib.is_valid_quantity(flesh, lib.MINIMUM_QUANTITY) else lib.MINIMUM_QUANTITY
        self.__ectoplasm = ectoplasm if lib.is_valid_quantity(ectoplasm, 1) else 1


    def get_ritual_name(self) -> str:
        return self.__ritual_name

    def get_undead_name(self) -> str:
        return self.__undead_name

    def get_health(self) -> int:
        return self.__health

    def get_power(self) -> int:
        return self.__power

    def get_necrotic(self) -> int:
        return self.__necrotic

    def get_spirit(self) -> int:
        return self.__spirit

    def get_bone(self) -> int:
        return self.__bone

    def get_flesh(self) -> int:
        return self.__flesh

    def get_ectoplasm(self) -> int:
        return self.__ectoplasm
    

    ritual_name = property(get_ritual_name)
    undead_name = property(get_undead_name)
    init_health = property(get_health)
    init_power = property(get_power)
    necrotic = property(get_necrotic)
    spirit = property(get_spirit)
    bone = property(get_bone)
    flesh = property(get_flesh)
    ectoplasm = property(get_ectoplasm)


    def check_ritual_require(self, resource:Resources) -> bool:
        if isinstance(resource, Resources):
            return resource.require(necrotic = self.__necrotic,
                                    spirit = self.__spirit,
                                    bone = self.__bone,
                                    flesh = self.__flesh,
                                    ectoplasm = self.__ectoplasm)
        return False

    def consume_ritual_resource(self, resource:Resources) -> bool:
        if isinstance(resource, Resources):
            return(
                resource.spend(necrotic = self.__necrotic,
                               spirit = self.__spirit,
                               bone = self.__bone,
                               flesh = self.__flesh,
                               ectoplasm = self.__ectoplasm))

        return False

    def create_undead(self, id:int) -> Undead:
        return Undead(id, self.__undead_name, self.__health, self.__power)