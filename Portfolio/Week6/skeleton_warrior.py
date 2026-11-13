from warrior_undead import WarriorUndead

class SkeletonWarrior(WarriorUndead):
    """Represent a skeleton warrior with its own command."""
    def __init__(self, id, name:str, health:int, power:int):
        super().__init__(id, name, health, power)

    def command(self) -> str:
        return f"{self.name} is a skeleton warrior with {self.health} health and {self.power} power."

    