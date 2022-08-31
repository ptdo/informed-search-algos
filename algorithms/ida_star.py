import sys
sys.path.append('')
import time as timer

from utils.node import Node
from puzzle import EightPuzzle
from stats import Statistics
from heuristics.lookup import h

h_val = 0
count = 0

def get_successors(node):
    state = node.state.initial
    puzzle = EightPuzzle(state)
    successors = []
    for action in puzzle.actions(state):
        result = puzzle.result(state, action)
        child_puzzle = EightPuzzle(result)
        node = Node(child_puzzle, parent=node, depth=node.depth+1)
        successors.append(node)
    return successors

def search(path, g, bound, heuristic, patterns=None, lookup_table=None):
    global h_val, count
    if heuristic == 'pdb':
        assert patterns is not None
        assert lookup_table is not None
    node = path[-1]
    puzzle = node.state
    h_n = h(heuristic, puzzle.initial, patterns, lookup_table)
    f = g + h_n
    h_val += h_n
    count += 1
    if f > bound:
        return f
    if puzzle.goal_test(puzzle.initial):
        return 'found'
    min_val = float('inf')
    for successor in get_successors(node):
        if successor not in path:
            path.append(successor)
            t = search(path, g+1, bound, patterns, lookup_table)
            if t == 'found':
                return 'found'
            if t < min_val:
                min_val = t
            path.pop()
    return min_val

def ida_star(puzzle, heuristic,patterns=None,lookup_table=None):
    global h_val, count
    if heuristic == 'pdb':
        assert patterns is not None
        assert lookup_table is not None

    start = timer.time()
    stats = Statistics('IDA*')
    root = Node(puzzle)

    bound = h(heuristic, puzzle.initial,patterns,lookup_table)
    h_val += bound
    count += 1

    path = []
    path.append(root)
    while True:
        t = search(path,0,bound,heuristic,patterns,lookup_table)
        if t == 'found':
            end = timer.time() - start
            stats.result['CPU_time'] = end
            avg_h = h_val/count
            stats.result['avg_h'] = avg_h
            stats.result['solution_length'] = len(path)
            return path, stats
        if t == float('inf'):
            return 'not found'
        bound = t