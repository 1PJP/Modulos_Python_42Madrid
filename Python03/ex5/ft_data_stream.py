import random

actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim']
names = ['alice', 'bob', 'charlie', 'dylan']


def gen_event():
    while True:
        yield (random.choice(names), random.choice(actions))


def consume_event(lista):
    while lista:
        item = random.choice(lista)
        lista.remove(item)
        yield (item)


if __name__ == '__main__':
    print('=== Game Data Stream Processor ===')
    gen = gen_event()
    for i in range(1000):
        action = next(gen)
        print(f'Event {i}: Player {action[0]} did action {action[1]}')
    event = [next(gen) for _ in range(10)]
    print(f'Built list of 10 events: {event}')
    for j in consume_event(event):
        print(f'Got event from list: {j}')
        print(f'Remains in list {event}')
