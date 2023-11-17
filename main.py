import random

def walk(path_length: int, max_steps: int) -> bool:
    pos = path_length // 2

    for _ in range(max_steps):
        r = random.choice((-1, 1))
        pos += r
        if pos == -1 or pos == path_length:
            return True

    return False

def simulate(run_count: int, path_length: int, max_steps: int) -> float:
    finished_count = 0
    for _ in range(run_count):
        if (walk(path_length, max_steps)):
            finished_count += 1

    return finished_count / run_count * 100

def find_best_max_steps(run_count: int, path_length: int) -> None:
    current_max_steps = 1
    success_rate = simulate(run_count, path_length, current_max_steps)
    while success_rate <= 80:
        current_max_steps += 1
        success_rate = simulate(run_count, path_length, current_max_steps)
    print(success_rate)
    print(current_max_steps)

find_best_max_steps(10000, 14)