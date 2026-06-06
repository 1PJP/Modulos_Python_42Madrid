def ft_count_harvest_recursive() -> None:
    recursive = int(input('Days until harvest: '))

    def ft_aux(number: int = 1) -> None:
        if number > recursive:
            print('Harvest time!')
            return
        print(f'Day {number}')
        ft_aux(number + 1)
    ft_aux()
