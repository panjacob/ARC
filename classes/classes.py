from abc import abstractmethod


class Plant:
    pass


class Rose(Plant):
    pass


class Building:
    pass


class Tavern(Building):
    pass


class Race:
    height = 5
    strength = 10
    mana = 20
    attack = 100
    defence = 100

    def __init__(self, height, strength, mana, attack, defence):
        self.height = height
        self.strength = strength
        self.mana = mana
        self.attack = attack
        self.defence = defence


class Humanoid(Race):
    color = "green"
    size = "medium"
    weapon = []
    movement = []

    def __init__(self, height, strength, mana, attack, defence, weapons):
        super.__init__(height, strength, mana, attack, defence)
        self.weapon = weapons


class Elf(Humanoid):
    pass


class Orc(Humanoid):
    pass


class Human(Humanoid):
    pass


class Combat:
    def fight(race1, race2):
        pass


class Movement:
    available_terrain = []

    @abstractmethod
    def move():
        pass
