from abc import ABC, abstractmethod
from typing import cast
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability


class InvalidStrategy(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> list[str]:
        if self.is_valid(creature):
            casted = cast(TransformCapability, creature)
            return [casted.transform(), creature.attack(),
                    casted.revert()]
        else:
            raise InvalidStrategy(f"Invalid Creature '{creature._name}'"
                                  " for this aggressive strategy")

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        else:
            return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> list[str]:
        if self.is_valid(creature):
            casted = cast(HealCapability, creature)
            return [creature.attack(), casted.heal()]
        else:
            raise InvalidStrategy(f"Invalid Creature '{creature._name}'"
                                  " for this defensive strategy")

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        else:
            return False
