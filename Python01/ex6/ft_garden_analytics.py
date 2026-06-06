class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(f' Stats: {self._grow_count} grow,'
                  f' {self._age_count} age, {self._show_count} show')

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age_ = age
        self._stats = Plant.Stats()

    def show(self) -> None:
        print(
            f'{self._name}: {round(self._height, 1)}cm, {self._age_} days old'
            )
        self._stats._show_count += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
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

    def grow(self, grow_day: float) -> None:
        self._height = self._height + grow_day
        self._stats ._grow_count += 1

    def age(self, age_days: int) -> None:
        self._age_ = self._age_ + age_days
        self._stats._age_count += 1

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> 'Plant':
        return cls('Unknow plant', 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f' Color: {self._color}')
        if self._bloomed:
            print(f'{self._name} is blooming beautifully!')

    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk: float,):
        super().__init__(name, height, age)
        self._trunk = trunk
        self._shade_count = 0

    def show(self) -> None:
        super().show()
        print(f' Trunk diameter {self._trunk}')

    def produce_shade(self) -> None:
        print(f'Tree {self._name} now produce a shade of'
              f'{self._height} long and {self._trunk}cm wide.')
        self._shade_count += 1


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str, seeds: int):
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def show(self) -> None:
        super().show()


def display_status(plant: Plant) -> None:
    print(f' [Statistics for {plant._name}]')
    plant._stats.display()
    if isinstance(plant, Tree):
        print(f'{plant._shade_count} shade')


def ft_garden_analytics() -> None:
    print('=== Garden statistics ===')
    print('=== Check year-ods')
    print(f'Is 30 days more than a year? -> {Plant.is_older_than_year(30)}')
    print(f'Is 400 days more than a year? -> {Plant.is_older_than_year(400)}')
    print()
    rose = Flower('Rose', 15.0, 10, 'red')
    oak = Tree('Oak', 200.0, 365, 5.0)
    sunflower = Seed('Sunflower', 80.0, 45, 'yellow', 0)
    anonymous = Plant.anonymous()

    print('=== Flower')
    rose.show()
    print(' Rose has not bloomed yet')
    display_status(rose)
    print(' [asking the rose to grow and blood]')
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_status(rose)
    print()

    print('=== Tree')
    oak.show()
    display_status(oak)
    print(' [asking the oak to produce shade]')
    oak.produce_shade()
    display_status(oak)
    print()

    print('=== Seed')
    sunflower.show()
    print(' Sunflower has not bloomed yet')
    print(f' Seeds: {sunflower._seeds}')
    print(' [make sunflower grow, age and bloom]')
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower._seeds = 42
    sunflower.bloom()
    sunflower.show()
    print(f' Seeds: {sunflower._seeds}')
    display_status(sunflower)
    print()
    print('=== Anonymous')
    anonymous.show()
    display_status(anonymous)


if __name__ == '__main__':
    ft_garden_analytics()
