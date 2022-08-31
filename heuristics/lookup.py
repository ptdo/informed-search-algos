from heuristics.manhattan import manhattan_distance
from heuristics.hamming import hamming_distance
from heuristics.linearConflict import linearConflict
from puzzle import EightPuzzle


def h(heuristic,state,patterns=None, lookup_table=None):
    state = EightPuzzle(state)
    h=0
    if heuristic == 'manhattan':
        h = manhattan_distance(state)
    elif heuristic == 'hamming':
        h = hamming_distance(state)
    elif heuristic == 'lc':
        h = linearConflict(state)
    elif heuristic == 'pdb':
        for pattern in patterns:
            pattern_tiles = [x for x in pattern if x != -1 and x != 0]
            lst = []
            for tile in state.initial:
                if tile not in pattern_tiles and tile != 0:
                    tile = -1
                lst.append(tile)
            tup = tuple(lst)
            # Regular lookup
            cost = lookup_table[str(tup)]
            h += cost
    
    return h