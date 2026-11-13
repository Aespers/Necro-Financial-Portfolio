from undead import Undead
from cursed_undead import CursedUndead
from warrior_undead import WarriorUndead
from death_knight import DeathKnight
from putrid_zombie import PutridZombie
from phantom_guardian import PhantomGuardian


from resource import Resources
import lib as lib


class Ritual:

    """Store the cost and starting stats for summoning an undead."""
    def __init__(self, ritual_name: str, undead_name: str, health: int, power: int, necrotic: int, spirit: int, bone: int, flesh: int, ectoplasm: int, undead_type: type[Undead]) -> None:
        self.__ritual_name = ritual_name if lib.is_valid_string(
            ritual_name) else "Error ritual name"
        self.__undead_name = undead_name if lib.is_valid_string(
            undead_name) else "Error undead name"
        self.__health = health if lib.is_valid_quantity(
            health, undead_type.MIN_HEALTH) and health <= undead_type.MAX_HEALTH else undead_type.MIN_HEALTH
        self.__power = power if lib.is_valid_quantity(
            power, undead_type.MIN_POWER) and power <= undead_type.MAX_POWER else undead_type.MIN_POWER
        self.__necrotic = necrotic if lib.is_valid_quantity(
            necrotic, lib.MINIMUM_QUANTITY) else lib.MINIMUM_QUANTITY
        self.__spirit = spirit if lib.is_valid_quantity(
            spirit, lib.MINIMUM_QUANTITY) else lib.MINIMUM_QUANTITY
        self.__bone = bone if lib.is_valid_quantity(
            bone, lib.MINIMUM_QUANTITY) else lib.MINIMUM_QUANTITY
        self.__flesh = flesh if lib.is_valid_quantity(
            flesh, lib.MINIMUM_QUANTITY) else lib.MINIMUM_QUANTITY
        self.__ectoplasm = ectoplasm if lib.is_valid_quantity(
            ectoplasm, 1) else 1
        self.__undead_type = undead_type if isinstance(undead_type, type) and issubclass(
            undead_type, Undead) else "Undead type must be an Undead subclass"

    def __str__(self):
        return f""

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

    def get_undead_type(self) -> type[Undead]:
        return self.__undead_type

    ritual_name = property(get_ritual_name)
    undead_name = property(get_undead_name)
    init_health = property(get_health)
    init_power = property(get_power)
    necrotic = property(get_necrotic)
    spirit = property(get_spirit)
    bone = property(get_bone)
    flesh = property(get_flesh)
    ectoplasm = property(get_ectoplasm)
    undead_type = property(get_undead_type)

    def check_ritual_require(self, resource: Resources) -> bool:
        """Check whether the resources can cover the ritual cost."""
        if isinstance(resource, Resources):
            return resource.require(necrotic=self.__necrotic,
                                    spirit=self.__spirit,
                                    bone=self.__bone,
                                    flesh=self.__flesh,
                                    ectoplasm=self.__ectoplasm)
        return False

    def consume_ritual_resource(self, resource: Resources) -> bool:
        """Pay for the ritual and return True if payment succeeds."""
        if isinstance(resource, Resources):
            return (
                resource.spend(necrotic=self.__necrotic,
                               spirit=self.__spirit,
                               bone=self.__bone,
                               flesh=self.__flesh,
                               ectoplasm=self.__ectoplasm))

        return False

    def create_undead(self, undead_id: int) -> Undead:
        """Create the stored type of undead with the given ID.

        Return None for an invalid ID. No resources are spent here.
        """

        if lib.is_valid_quantity(undead_id, 1):
            return self.__undead_type(undead_id, self.undead_name, self.__health, self.__power)
        else:
            print("ID cannot be negative!")
