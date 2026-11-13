from cursed_undead import CursedUndead
from warrior_undead import WarriorUndead


class DeathKnight(CursedUndead, WarriorUndead):

    MIN_HEALTH = 10
    MAX_HEALTH = 500
    MIN_POWER = 50
    MAX_POWER = 3000

    HEALTH_GAIN = 10
    POWER_GAIN = 30
    LEVEL_GAIN = 1

    def __init__(self, id: int, name: str, health: int, power: int):
        super().__init__(id, name, health, power)

    def combat_style(self):
        super().combat_style()
