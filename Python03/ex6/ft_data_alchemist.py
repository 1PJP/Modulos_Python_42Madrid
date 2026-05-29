import random

players = ['Alice', 'bob', 'Charlie', 'dylan',
           'Emma', 'Gregory', 'john', 'kevin', 'Lian']


if __name__ == '__main__':
    print('=== Game Data Alchemist ===\n')
    print(f'Initial list of players: {players}')
    mayus = [mayus.capitalize() for mayus in players]
    print(f'New list with all players capitalized: {mayus}')
    diferent = [i for i in players if i == i.capitalize()]
    print(f'New lis of capitalized players only: {diferent}\n')
    dix = {name: random.randint(1, 100) for name in mayus}
    print(f'Score dict: {dix}')
    averge = round(sum(dix.values()) / len(dix), 2)
    print(f'Score averge is {averge}')
    promed = {name: score for name, score in dix.items() if score > averge}
    print(f'High score: {promed}')
