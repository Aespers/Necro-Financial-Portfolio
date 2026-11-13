from cursed_undead import CursedUndead

class VengefulGhost(CursedUndead):

    def __init__(self, id, name:str, health:int, power:int):
        super().__init__(id, name, health, power)

    def command(self) -> str:
        return f"{self.name} is a vengeful ghost with {self.health} health and {self.power} power."