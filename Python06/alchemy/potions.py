from alchemy import elements as alchemy_elemts
import elements


def healing_potion() -> str:
    return (f"Healing potion brewed with"
            f"'{alchemy_elemts.create_earth()}'"
            f" and '{alchemy_elemts.create_air()}'")


def strength_potion() -> str:
    return (f"Strength potion brewed with"
            f" '{elements.create_fire()}'"
            f" and '{elements.create_water()}'")
