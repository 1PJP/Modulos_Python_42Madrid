from alchemy import elements as alchemy_element
from .. import potions
import elements

def lead_to_gold() -> str:
    return(f"Recipes transmuting Lead to Gold: brew '{alchemy_element.create_air()}' and '{potions.strength_potion()}' mixed with '{elements.create_fire()}'")