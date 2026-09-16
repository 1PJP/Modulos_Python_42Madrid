from ex0.creature import Creature
from .capabilities import TransformCapability
from ex0 import CreatureFactory


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self.transformation:
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} performs a boosted strike!"

    def transform(self) -> str:
        self.transformation = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformation = False
        return f"{self._name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self.transformation:
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.transformation = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformation: bool = False
        return f"{self._name} stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
