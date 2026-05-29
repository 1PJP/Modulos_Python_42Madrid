import math


def get_player_pos():
    while True:
        try:
            location = input("Enter new coordinates as floats in"
                             " format 'x,y,z': ").split(',')
            if len(location) != 3:
                print('Invalid syntax')
                continue
            return (float(location[0]), float(location[1]), float(location[2]))
        except ValueError as e:
            for j in location:
                try:
                    float(j)
                except ValueError:
                    print(f"Error on parameter '{j}': {e}")


if __name__ == '__main__':
    print('=== Game Coordinate system ===\n')
    print('Get a first set of coordinates')
    temp = get_player_pos()
    print(f'Got a first tuple: {temp}')
    print(f'It includes: X={temp[0]}, Y={temp[1]}, Z={temp[2]}')
    print(f'Distance to center: '
          f'{round(math.sqrt((temp[0]**2 + temp[1]**2 + temp[2]**2)), 4)}\n')
    print('Get a second set of coordinates')
    temp1 = get_player_pos()
    print(f'Distance between the 2 sets of coordinates:'
          f' {round(math.sqrt((temp[0]-temp1[0])**2 + (temp[1]-temp1[1])**2 +
                              (temp[2]-temp1[2])**2), 4)}')
