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


def ft_plant_factory() -> None:

    print('=== Plant Factory Output ===')
    plant1 = Plant('Rose', 25.0, 30)
    plant2 = Plant('Oak', 200.0, 365)
    plant3 = Plant('Cactus', 5.0, 90)
    plant4 = Plant('Sunflower', 80.0, 45)
    plant5 = Plant('Fern', 15.0, 120)
    plants = [plant1, plant2, plant3, plant4, plant5]

    for plant in plants:
        print('Created:', end=' ')
        plant.show()


if __name__ == '__main__':
    ft_plant_factory()
