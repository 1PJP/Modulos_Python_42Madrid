import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <file>')
    else:
        print('=== Cyber Archives Recovery ===')
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            txt = open(sys.argv[1])
            print('---\n')
            print(f'{txt.read()}')
            print('---\n')
            txt.close()
            print(f"File '{sys.argv[1]}' closed.")
        except OSError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
