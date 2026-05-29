import sys

achievements: dict[str, int] = {}

if __name__ == '__main__':
    print('=== Inventory System Analyis ===')
    for i in range(1, len(sys.argv)):
        space = sys.argv[i].split(':')

        if len(space) != 2:
            print(f"Error - Invalid parameter '{sys.argv[i]}'")
            continue
        if space[0] in achievements:
            print(f"Redundant item '{space[0]}' - discarding")
            continue
        try:
            achievements[space[0]] = int(space[1])
        except ValueError as e:
            print(f"Quantity error for'{space[0]}': {e}")
            continue
    print(f'Got inventory: {achievements}')
    print(f'Item list: {achievements.keys()}')
    print(f'Total quantity of the {len(achievements)} items:'
          f' {sum(achievements.values())}')
    for key, value in achievements.items():
        porcen = round(value / sum(achievements.values()) * 100, 1)
        print(f'Item {key} represents {porcen}%')

    name_max = max(achievements, key=lambda j: achievements[j])
    valor_max = achievements[max(achievements, key=lambda j: achievements[j])]

    print(f'Item most abundant: {name_max} with quantity {valor_max}')
    name_min = min(achievements, key=lambda j: achievements[j])
    valor_min = achievements[min(achievements, key=lambda j: achievements[j])]
    print(f'Item least abundant: {name_min} with quantity {valor_min}')

    achievements.update({'magic_item': 1})
    print(f'Updated inventory: {achievements}')
