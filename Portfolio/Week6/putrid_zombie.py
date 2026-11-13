from undead import Undead

class PutridZombie(Undead):
    """Represent a putrid zombie with its own command."""
    def __init__(self, id, name:str, health:int, power:int):
        super().__init__(id, name, health, power)

    def command(self) -> str:
        return f"{self.name} is a putrid zombie with {self.health} health and {self.power} power."