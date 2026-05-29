def ft_count_harvest_iterative():
    iterative = int(input('Days until harvest: '))
    #i = 1 //es un poco inesesario ya que va ya en el for
    for i in range(1, iterative + 1):
        print(f'Day {i}')
    #i = i + 1 //se dice que for avanza solo
    print('Hervest time!')


#if __name__ == '__main__':
#    ft_count_harvest_iterative()
