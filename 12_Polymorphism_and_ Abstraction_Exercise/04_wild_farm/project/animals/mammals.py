from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self) -> float:
        return 0.10

    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Cat(Mammal):
    @property
    def food_that_eats(self):
        return [Vegetable, Meat]

    @property
    def gained_weight(self) -> float:
        return 0.30

    @staticmethod
    def make_sound() -> str:
        return "Meow"


class Dog(Mammal):
    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.40

    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Tiger(Mammal):
    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 1.00

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"
