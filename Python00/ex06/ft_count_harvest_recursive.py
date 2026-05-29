def ft_count_harvest_recursive():
    recursive = int(input('Days until harvest: '))

    def ft_aux(number=1):
        if number > recursive:
            print('Harvest time!')
            return
        print(f'Day {number}')
        ft_aux(number + 1)
    ft_aux()


#if __name__ == '__main__':
#    ft_count_harvest_recursive()
