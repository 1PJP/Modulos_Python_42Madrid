def ft_plant_age() -> None:
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to hervest")
    else:
        print("Plant needs more time to grow")
