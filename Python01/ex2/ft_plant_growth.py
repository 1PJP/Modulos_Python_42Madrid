class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(
            f'{self.name}: {round(self.height, 1)}cm, {self.age_days} days old'
            )

    def grow(self) -> None:
        self.height = self.height + 0.8

    def age(self) -> None:
        self.age_days = self.age_days + 1


def ft_plant_growth() -> None:
    print('=== Garden Plant Growth ===')

    plant1 = Plant('Rose', 25.0, 30)
    plant1.show()
    initial_height = plant1.height

    for i in range(1, 8):
        print(f'=== Day {i} ===')
        plant1.grow()
        plant1.age()
        plant1.show()
    growth = round(plant1.height - initial_height, 1)
    print(f'Growth this week: {growth}cm')


if __name__ == '__main__':
    ft_plant_growth()
