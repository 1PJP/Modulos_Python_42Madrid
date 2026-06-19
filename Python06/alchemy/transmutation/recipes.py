from alchemy import elements as alchemy_element
from .. import potions
import elements


def lead_to_gold() -> str:
    return (f"Recipes transmuting Lead to Gold: brew"
            f" '{alchemy_element.create_air()}'"
            f" and '{potions.strength_potion()}'"
            f" mixed with '{elements.create_fire()}'")
