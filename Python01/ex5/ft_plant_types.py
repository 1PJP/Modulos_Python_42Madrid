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

    def get_age_(self) -> int:
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

    def grow(self) -> None:
        self._height = self._height + 0.8

    def age(self) -> None:
        self._age_ = self._age_ + 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color

    def show(self) -> None:
        super().show()
        print(f' Color: {self._color}')

    def bloom(self) -> None:
        print(f'{self._name} is bloomming beautifully!')


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk: float):
        super().__init__(name, height, age)
        self._trunk = trunk

    def show(self) -> None:
        super().show()
        print(f' Trunk diameter: {self._trunk}')

    def produce_shade(self) -> None:
        print(f'Tree {self._name} now produces a shade of '
              f'{self._height}cm long and {self._trunk}cm wide.')


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_seaason: str, nutritional: int):
        super().__init__(name, height, age)
        self._harvest_season = harvest_seaason
        self._nutritional = 0

    def show(self) -> None:
        super().show()
        print(f' Harvest season: {self._harvest_season}')
        print(f' Nutricional value: {self._nutritional}')

    def grow(self) -> None:
        super().grow()
        self._nutritional = self._nutritional

    def age(self) -> None:
        super().age()
        self._nutritional = self._nutritional + 1


def ft_plant_types() -> None:
    print('=== Garden Plants Types ===')
    rose = Flower('Rose', 15.0, 10, 'red')
    oak = Tree('Oak', 200.0, 365, 5.0)
    tomato = Vegetable('Tomato', 5.0, 10, 'Abril', 0)
    print('=== Flower')
    rose.show()
    print(' Rose has not bloomed yet')
    print('[asking the rose to bloom]')
    rose.show()
    rose.bloom()
    print()
    print('=== Tree')
    oak.show()
    print('[asking the oak to produce shade]')
    oak.produce_shade()
    print()
    print('=== Tomato')
    tomato.show()
    print('[make tomato grow and age 20 days]')
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == '__main__':
    ft_plant_types()
