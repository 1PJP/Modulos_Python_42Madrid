def input_temperature(temp_str):
    return int(temp_str)


def test_temperature():
    print('=== Garden Temperature ===')
    print()
    print("Input data is '25'")
    try:
        result = input_temperature('25')
        print(f'Temperature is now {result}°C')
        print()
    except ValueError as e:
        print(f'Caught input_temperature error: {e}')

    print("Input data is 'abc'")
    try:
        result = input_temperature('abc')
        print(f"Input data is {result}")
    except ValueError as e:
        print(f'Caught input_temperature error: {e}')
    print()
    print(' All test completed - program didnt`t chash!')


if __name__ == '__main__':
    test_temperature()
