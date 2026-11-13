import lib as lib


class Resources:

    def __init__(self, necrotic: int, spirit: int, bone: int, flesh: int, ectoplasm: int) -> None:
        self.__necrotic = necrotic if lib.is_valid_quantity(
            necrotic) else lib.MINIMUM_QUANTITY
        self.__spirit = spirit if lib.is_valid_quantity(
            spirit) else lib.MINIMUM_QUANTITY
        self.__bone = bone if lib.is_valid_quantity(
            bone) else lib.MINIMUM_QUANTITY
        self.__flesh = flesh if lib.is_valid_quantity(
            flesh) else lib.MINIMUM_QUANTITY
        self.__ectoplasm = ectoplasm if lib.is_valid_quantity(
            ectoplasm) else lib.MINIMUM_QUANTITY

    def __str__(self) -> str:
        return f"Necrotic: {self.__necrotic}\n,Spirit: {self.__spirit}\n,Bone: {self.__bone}\n,Flesh: {self.__flesh}\n,Ectoplasm: {self.__ectoplasm}"

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

    necrotic = property(get_necrotic)
    spirit = property(get_spirit)
    bone = property(get_bone)
    flesh = property(get_flesh)
    ectoplasm = property(get_ectoplasm)

    def collect(self, necrotic: int = 0, spirit: int = 0, bone: int = 0, flesh: int = 0, ectoplasm: int = 0) -> None:
        """
        Takes the parameter as the amount of resources that are being collected.
        Increments the amount of resource that are being collected.
        """

        if lib.is_valid_quantity(necrotic, lib.MINIMUM_QUANTITY):
            self.__necrotic += necrotic
        else:
            print("Invalid amount of necrotic")

        if lib.is_valid_quantity(spirit, lib.MINIMUM_QUANTITY):
            self.__spirit += spirit
        else:
            print("Invalid amount of spirit")

        if lib.is_valid_quantity(bone, lib.MINIMUM_QUANTITY):
            self.__bone += bone
        else:
            print("Invalid amount of bone")

        if lib.is_valid_quantity(flesh, lib.MINIMUM_QUANTITY):
            self.__flesh += flesh
        else:
            print("Invalid amount of flesh")

        if lib.is_valid_quantity(ectoplasm, lib.MINIMUM_QUANTITY):
            self.__ectoplasm += ectoplasm
        else:
            print("Invalid amount of ectoplasm")

    def require(self, necrotic: int = 0, spirit: int = 0, bone: int = 0, flesh: int = 0, ectoplasm: int = 0) -> bool:
        """
        Checks if the amount of resources are enough with setting a flag, turning the flag if any of the resource entered is invalid, or when the resource is not enough.
        Returns the flag as a boolean
        """

        enough = True
        required_resource = [("Necrotic", necrotic, self.__necrotic),
                             ("Spirit", spirit, self.__spirit),
                             ("Bone", bone, self.__bone),
                             ("Flesh", flesh, self.__flesh),
                             ("Ectoplasm", ectoplasm, self.__ectoplasm)]

        for name, required, current in required_resource:
            if not lib.is_valid_quantity(required, lib.MINIMUM_QUANTITY):
                return False

        for name, required, current in required_resource:
            if required > current:
                print("Not enough", name)
                enough = False

        return enough

    def spend(self, necrotic: int = 0, spirit: int = 0, bone: int = 0, flesh: int = 0, ectoplasm: int = 0) -> bool:
        """
        Spends the resource, subtract the amount of resources by the parameter.
        Checks if the amount of resources that needs to be spent is valid, with the require() function.
        """

        if self.require(necrotic, spirit, bone, flesh, ectoplasm):
            self.__necrotic -= necrotic
            self.__spirit -= spirit
            self.__bone -= bone
            self.__flesh -= flesh
            self.__ectoplasm -= ectoplasm
            return True
        else:
            return False
