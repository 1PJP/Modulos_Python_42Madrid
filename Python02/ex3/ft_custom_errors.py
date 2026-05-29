class GardenError(Exception):
    def __init__(self, message='Unknown garden error'):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message='Unknown plant error'):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message='Unknown water error'):
        super().__init__(message)


def get_plant_error():
    raise PlantError('The tomato plant is wilting!')


def get_water_error():
    raise WaterError('Not enough water in the tank!')


def testing_errors():
    print('=== Custom Garden Errors Demo ===')
    print()
    print('Testing PlantError...')
    try:
        get_plant_error()
    except PlantError as e:
        print(f'Caught PlantError: {e}')
    print()
    print('Testing WaterError...')
    try:
        get_water_error()
    except WaterError as e:
        print(f'Caught WaterError: {e}')
    print()
    print('Testing catching all garden errors...')
    try:
        get_plant_error()
    except GardenError as e:
        print(f'Caught GardenError: {e}')
    try:
        get_water_error()
    except GardenError as e:
        print(f'Caught GardenError: {e}')
    print()
    print('All custom error types work correctly!')


if __name__ == '__main__':
    testing_errors()
