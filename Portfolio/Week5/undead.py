import lib as lib

class Undead:
    #constants are declared in the file lib.py
    def __init__(self, id:int, name:str, health:int, power:int):
        self.__id = id if lib.is_valid_quantity(id) else 0
        self.__name = name if lib.is_valid_string(name) else "Error name"
        self.__level = lib.MIN_LEVEL
        self.__health = health if lib.is_valid_quantity(health, lib.MIN_HEALTH) and health <= lib.MAX_HEALTH else lib.MIN_HEALTH
        self.__power = power if lib.is_valid_quantity(power, lib.MIN_POWER) and power <= lib.MAX_POWER else lib.MIN_POWER
    def __str__(self):
        return f"ID: {self.__id}\nName: {self.__name}\nLevel: {self.__level}\nCurrent Health: {self.__health}/{lib.MAX_HEALTH}(Max)\nCurrent Power: {self.__power}/{lib.MAX_POWER}(Max)"

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_health(self):
        return self.__health

    def get_power(self):
        return self.__power
    

    id = property(get_id)
    name = property(get_name)
    level = property(get_level)
    health = property(get_health)
    power = property(get_power)


    def level_up(self) -> None:
        if self.__level < lib.MAX_LEVEL:
            self.__level += lib.LEVEL_GAIN

            self.__health += lib.HEALTH_GAIN
            if self.__health > lib.MAX_HEALTH:
                self.__health = lib.MAX_HEALTH

            self.__power += lib.POWER_GAIN
            if self.__power > lib.MAX_POWER:
                self.__power = lib.MAX_POWER


    def command(self):
        return f"{self.name} is a undead with {self.health} health and {self.power} power."
    