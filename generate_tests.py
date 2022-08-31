from puzzle import EightPuzzle
import random

def write(num, tup):
    with open(f'tests/test{num}.txt', 'w') as f:
        line = ','.join(str(x) for x in tup)
        f.write(line)
    f.close()


if __name__ == "__main__":
    count = 0
    tup = (0,1,2,3,4,5,6,7,8)
    lst = list(tup)
    while count < 100:
        random.shuffle(lst)
        new_tup = tuple(lst)
        puzzle = EightPuzzle(new_tup)
        if puzzle.check_solvability(new_tup):
            write(count, new_tup)
            count += 1