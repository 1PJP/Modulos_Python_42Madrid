from .creature import Creature
from .creature_factory import CreatureFactory


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__('Flameling', 'Fire')

    def attack(self) -> str:
        return ('Flameling uses Ember!')


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__('Pyrodon', 'Fire/Flying')

    def attack(self) -> str:
        return ('Pyrodon uses Flamethrower!')
