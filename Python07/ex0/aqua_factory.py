from .creature import Creature
from .creature_factory import CreatureFactory


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__('Aquabub', 'Water')

    def attack(self) -> str:
        return ('Aquabub uses Water Gun!')


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__('Torragon', 'Water')

    def attack(self) -> str:
        return ('Torragon uses Hydro Pump!')
