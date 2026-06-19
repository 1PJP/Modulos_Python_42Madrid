from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    temp = dark_spell_allowed_ingredients()
    if any(data in ingredients.lower() for data in temp):
        return (f'{ingredients} - VALID ')
    else:
        return (f'{ingredients} - INVALID')
