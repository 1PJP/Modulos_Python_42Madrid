import sys

if __name__ == '__main__':
    print('=== Player Score Analytics ===')
    score = []
    for i in range(1, len(sys.argv)):
        try:
            score.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
    if score == []:
        print(f'No score provided. Usage: python3 '
              f'{sys.argv[0]} <score1> <score2> ...')
    else:
        print(f'Scores processed: {score}')
        print(f'Total players: {len(score)}')
        print(f'Total score: {sum(score)}')
        print(f'Average score: {sum(score) / len(score)}')
        print(f'High score:{max(score)}')
        print(f'low Score: {min(score)}')
        print(f'Score range: {max(score) - min(score)}')
