import random

# Input layer
def take_input() -> tuple:
    path_length = int(input('Path length: '))
    max_steps = int(input('Max steps: '))
    return (path_length, max_steps)

# Computational + output layer
def walk(path_length: int, max_steps: int) -> None:
    # Initialize variables
    pos = path_length // 2
    path = ['.'] * path_length
    is_terminated = False

    # Main loop
    for _ in range(max_steps):
        # Print progress
        path[pos] = '*'
        print('HOME', *path, 'PUB')
        path[pos] = '.'

        # Update position
        r = random.choice((-1, 1))
        pos += r

        # Check if we got home or to the pub
        if pos < 0:
            print('HOME*', *path, 'PUB')
            print('The drunk man ended up at home.')
            is_terminated = True
            break
        elif pos == path_length:
            print('HOME', *path, '*PUB')
            print('The drunk man ended up in the pub.')
            is_terminated = True
            break

    # Check if we fell asleep or not
    if not is_terminated:
        print('The drunk man fell asleep on the pavement and got nowhere.')

def main() -> None:
    input = take_input()
    walk(input[0], input[1])

main()