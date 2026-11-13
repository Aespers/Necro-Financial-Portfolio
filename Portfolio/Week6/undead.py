import lib as lib
from abc import ABC, abstractmethod


class Undead:
    # constants for undead
    MIN_HEALTH = 10
    MAX_HEALTH = 1000

    MIN_POWER = 10
    MAX_POWER = 1000

    MAX_LEVEL = 100
    MIN_LEVEL = 1

    HEALTH_GAIN = 10
    POWER_GAIN = 10
    LEVEL_GAIN = 1

    def __init__(self, id: int, name: str, health: int, power: int):
        self.__id = id if lib.is_valid_quantity(id) else 0
        self.__name = name if lib.is_valid_string(name) else "Error name"
        self.__level = self.MIN_LEVEL
        self.__health = health if lib.is_valid_quantity(
            health, self.MIN_HEALTH) and health <= self.MAX_HEALTH else self.MIN_HEALTH
        self.__power = power if lib.is_valid_quantity(
            power, self.MIN_POWER) and power <= self.MAX_POWER else self.MIN_POWER

    def __str__(self):
        return f"ID: {self.__id}\nName: {self.__name}\nLevel: {self.__level}\nCurrent Health: {self.__health}/{self.MAX_HEALTH}(Max)\nCurrent Power: {self.__power}/{self.MAX_POWER}(Max)"

    def get_id(self):
        '''Gets the if of the undead'''
        return self.__id

    def get_name(self):
        '''Gets the name of the undead'''
        return self.__name

    def get_level(self):
        '''Gets the level of the undead'''
        return self.__level

    def get_health(self):
        "Gets the health of the undead"
        return self.__health

    def get_power(self):
        '''Gets the power of the undead'''
        return self.__power

    id = property(get_id)
    name = property(get_name)
    level = property(get_level)
    health = property(get_health)
    power = property(get_power)

    def level_up(self) -> None:
        '''
        Level up the undead, using the constants declared above.
        Checks if the undead has reached max level, prints a message if max level is reached.
        '''
        if self.__level < self.MAX_LEVEL:
            self.__level += self.LEVEL_GAIN

            self.__health += self.HEALTH_GAIN
            if self.__health > self.MAX_HEALTH:
                self.__health = self.MAX_HEALTH

            self.__power += self.POWER_GAIN
            if self.__power > self.MAX_POWER:
                self.__power = self.MAX_POWER
        else:
            print("Max Level!")

    @abstractmethod
    def command(self):
        '''A method prototype of command'''
        pass
