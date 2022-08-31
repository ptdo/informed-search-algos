from collections import deque
from math import factorial
import json
import sys
sys.path.append('')
from puzzle import EightPuzzle       


def write(data, num):
    with open(f"pdb/disjoint_pdb{num}.txt", "w") as f:
        for row in data:
            f.write(json.dumps(row))
            f.write('\n')

"""
    Logic adapted from: https://stackoverflow.com/questions/59770840/8-puzzle-pattern-database-in-python
"""

def generate_disjoint_pdb(patterns, num):
    w_data =[]
    bound=0
    entries = 0

    for pattern in patterns:
        # Gets pattern tiles
        pattern_tiles = [x for x in pattern if x != -1 and x != 0]
        bound += factorial(9)/factorial(len(pattern_tiles))

        queue = deque([(pattern, 0)])
        closed = []

        while queue:
            entry = queue.popleft()
            state = entry[0]

            # Keeps track of pattern tiles indices 
            pattern_idx = [state.index(x) for x in pattern_tiles]
            
            curr_puzzle = EightPuzzle(entry[0])
            for action in curr_puzzle.actions(state):
                result = curr_puzzle.result(state, action)
                if result not in closed:
                    blank_idx = result.index(0)
                    closed.append(result)
                    
                    # Increments cost if blank tile is swapped with 
                    # any pattern tile, by comparing their indices
                    row = (result, entry[1]+1) if blank_idx in pattern_idx \
                        else (result, entry[1])
                    
                    w_data.append({f"{row[0]}": row[1]})
                    entries += 1
                    
                    queue.append(row)
        if entries > bound:
            print(bound)
            break
    write(w_data, num)