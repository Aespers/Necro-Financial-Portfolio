from undead import Undead


class WarriorUndead(Undead):
    """Represent an undead with a warrior command."""
    def __init__(self, id, name: str, health: int, power: int):
        super().__init__(id, name, health, power)

    def command(self) -> str:
        return f"{self.name} is a warrior undead with {self.health} health and {self.power} power."

    def combat_style(self):
        pass
