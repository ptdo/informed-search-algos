import time

from puzzle import EightPuzzle
from stats import get_stats, get_summary, read_test
from algorithms.a_star import a_star


if __name__=="__main__":
    hm = {'nodes': [], 'cost': [], 'time':[], 'h_vals': [], 'avg_cost': 0, 'avg_nodes': 0, 'avg_hvals': 0, 'avg_time': 0}

    start = time.time()
    count = 0
    while count < 100:
        data = read_test(f"tests/test{count}.txt")
        initial = tuple(int(num) for num in data)
        puzzle = EightPuzzle(initial)

        if not puzzle.check_solvability(initial):
            print("puzzle instance is not solvable")

        else:
            if count % 10 == 0:
                print(f"Solving Puzzle #{count}")

            sol, stats = a_star(puzzle, heuristic="hamming")
            get_stats(hm, stats)

        count += 1

    end = time.time()
    print(f"DONE. TOTAL TIME IS \t {end-start} \n")

    print('=========== A* with Hamming Distance =========== \n')
    get_summary(hm)