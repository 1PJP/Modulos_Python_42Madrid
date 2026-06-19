from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ['bats', 'frogs', 'arsenic', 'eyeball']


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    temp = dark_validate_ingredients(ingredients)
    if '- VALID' in temp:
        return (f'Spell recorded: {spell_name} ({temp})')
    else:
        return (f'Spell rejected {spell_name} ({temp})')
