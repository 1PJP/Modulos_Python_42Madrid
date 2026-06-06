import random

archivements = ['Crafting Genius', 'World Savior', 'Collector Supreme',
                'Untouchable', 'Boss Slayer', 'Strategist', 'Survivor',
                'Master Explorer', 'Treasure Hunter', 'First Steps',
                'Sharp Mind', 'Speed Runner', 'Unstoppable']


def gen_player_archivements() -> set[str]:
    chance = random.randint(3, len(archivements))
    return (set(random.sample(archivements, chance)))


if __name__ == '__main__':
    print('=== Achivemets Tracker System ===\n')
    alice = gen_player_archivements()
    print(f'Player Alice: {type(alice)}')
    bob = gen_player_archivements()
    print(f'Player Bob: {bob}')
    chalie = gen_player_archivements()
    print(f'Player Charlie: {chalie}')
    dylan = gen_player_archivements()
    print(f'Player Dylan: {dylan}')

    union = alice.union(bob).union(chalie).union(dylan)
    print(f' All distinct achievements: {union}\n')

    common = alice.intersection(bob).intersection(chalie).intersection(dylan)
    print(f'Common achivements: {common}\n')

    alice_dif = alice.difference(bob).difference(chalie).difference(dylan)
    print(f'Only Alice has: {alice_dif}')
    bob_dif = bob.difference(alice).difference(chalie).difference(dylan)
    print(f'Only Bob has: {bob_dif}')
    chalie_dif = chalie.difference(bob).difference(alice).difference(dylan)
    print(f'Only Charlie has: {chalie_dif}')
    dylan_dif = dylan.difference(alice).difference(bob).difference(chalie)
    print(f'Only Dylan has: {dylan_dif}\n')

    print(f'Alice is missing: {set(archivements).difference(alice)}')
    print(f'Bob is missing: {set(archivements).difference(bob)}')
    print(f'Charlie is missing: {set(archivements).difference(chalie)}')
    print(f'Dylan is missing: {set(archivements).difference(dylan)}')
