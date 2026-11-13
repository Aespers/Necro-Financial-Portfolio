from undead import Undead

class CursedUndead(Undead):
    def __init__(self, id, name:str, health:int, power:int):
        super().__init__(id, name, health, power)

    def command(self) -> str:
        return f"{self.name} is a cursed undead with {self.health} health and {self.power} power."