from warrior_undead import WarriorUndead

class PhantomGuardian(WarriorUndead):

    """Represent a phantom guardian with its own command."""
    def __init__(self, id, name:str, health:int, power:int):
        super().__init__(id, name, health, power)

    def command(self) -> str:
        return f"{self.name} is a phantom guardian with {self.health} health and {self.power} power."