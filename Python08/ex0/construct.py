import sys
import os
import site


def detect_venv() -> bool:
    if sys.prefix != sys.base_prefix:
        return True
    else:
        return False


def outside_venv() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")

    print(f'Current Python: {sys.executable}')
    print(f'Virtual Environment:'
          f'{os.environ.get("VIRTUAL_ENV", "None detected")}\n')

    print("WARNING: You're in the global environment!")
    print('The machines can see everything you install.\n')

    print('To enter the construct, run:')
    print('python -m venv matrix_env')
    print('source matrix_env/bin/activate # On Unix')
    print(r'matrix_env\Scripts\activate # On Windows')

    print('\nThen run this program again.')


def inside_venv() -> None:
    print('\nMATRIX STATUS: Welcome to the construct\n')

    print(f'Current Python: {sys.executable}')
    print(f'Virtual Environment:'
          f'{os.path.basename(os.environ.get("VIRTUAL_ENV", ""))}')
    print(f'Environment Path: {os.environ.get("VIRTUAL_ENV")}\n')

    print("SUCCESS: You're in an isolated environment!")
    print('Safe to install packages without affecting')
    print('the global system\n')

    print('Package installation path:')
    print(f'{site.getsitepackages()[0]}')


if __name__ == '__main__':
    if detect_venv():
        inside_venv()
    else:
        outside_venv()
