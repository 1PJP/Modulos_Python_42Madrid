class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age_ = age

    def show(self) -> None:
        print(
            f'{self._name}: {round(self._height, 1)}cm, {self._age_} days old'
            )

    def get_height(self) -> float:
        return self._height

    def get_age_days(self) -> int:
        return self._age_

    def set_heigth(self, value_cm: float) -> None:
        if value_cm < 0:
            print(f'{self._name}: Error, height can`t be negative')
            print('Height update rejected')
        else:
            self._height = value_cm
            print(f'Height update: {value_cm}cm')

    def set_age_days(self, value_days: int) -> None:
        if value_days < 0:
            print(f'{self._name}: Error, age can`t be negative')
            print('Age, update rejected')
        else:
            self._age_ = value_days
            print(f'Age update: {value_days} days old')


def ft_garden_security() -> None:

    print('=== Garden Security System ===')
    print('Plant created:', end=' ')
    plant = Plant('Rose', 15.0, 10)
    plant.show()
    print()
    plant.set_heigth(25)
    plant.set_age_days(30)
    print()
    plant.set_heigth(-12.5)
    plant.set_age_days(-15)
    print()
    print('Current state:', end=' ')
    plant.show()


if __name__ == '__main__':
    ft_garden_security()
