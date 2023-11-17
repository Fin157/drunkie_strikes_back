#fin
import random

def walk(path_length: int, max_steps: int) -> bool:
    delka = path_length
    kroky = max_steps
    pozice = delka // 2
    # cesta = []
    # for z in range(delka):
    #     cesta.append(".")
    # cesta[pozice] = "*"
    # print("domov",*cesta,"hospoda")

    for i in range(kroky):
        # cesta = []
        # for y in range(delka):
        #     cesta.append(".")
        r = random.choice((-1, 1))
        pozice += r
        if pozice == -1 or pozice == delka:
            return True
            # print("DOMOV*",*cesta,"hospoda")
            # print("Skončil jsi doma")
        # else:
        #     return True
            # cesta[pozice] = "*"
            # print("domov",*cesta,"hospoda")

    return False
        # print("Usnul jsi na cestě")

def simulate(run_count: int, path_length: int, max_steps: int) -> float:
    finished_count = 0
    for _ in range(run_count):
        if (walk(path_length, max_steps)):
            finished_count += 1

    return finished_count / 100

def find_best_max_steps(run_count: int, path_length: int) -> None:
    current_max_steps = 1
    success_rate = simulate(run_count, path_length, current_max_steps)
    while success_rate <= 80:
        current_max_steps += 1
        success_rate = simulate(run_count, path_length, current_max_steps)
    print(success_rate)
    print(current_max_steps)

find_best_max_steps(10000, 14)