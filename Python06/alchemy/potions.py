from alchemy import elements as alchemy_elemts
import elements

def healing_potion() -> str:
    return(f"Healing potion brewed with '{alchemy_elemts.create_earth()}' and '{alchemy_elemts.create_air()}'")

def strength_potion() -> str:
    return(f"Strength potion brewed with '{elements.create_fire()}' and '{elements.create_water()}'")