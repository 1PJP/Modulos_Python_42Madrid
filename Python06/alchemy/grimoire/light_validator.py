def validate_ingredients(ingredients: str) -> str:
    temp = ['earth', 'air', 'fire', 'water']
    if any(data in ingredients.lower() for data in temp):
        return (f'{ingredients} - VALID ')
    else:
        return (f'{ingredients} - INVALID')
