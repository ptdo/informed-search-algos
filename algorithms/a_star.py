import statistics
import time as timer

from utils.node import Node
from utils.priority_queue import PriorityQueue
from stats import Statistics
from puzzle import EightPuzzle
from heuristics.lookup import h as h_lookup


def a_star(puzzle, heuristic=None, patterns=None, lookup_table=None):
    start_time = timer.time()
    if heuristic == "pdb":
        assert patterns is not None
    if heuristic:
        stats = Statistics(heuristic)
    else:
        stats = Statistics("no heuristic")
    open_list = PriorityQueue()
    closed_list = []
    root = Node(state=puzzle)
    open_list.push(root)
    h_vals = []
    
    count = 0
    while open_list.size() > 0:
        curr = open_list.pop()
        stats.result['expanded_nodes'] += 1
        state = curr.state.initial
        
        if curr.state.goal_test(state):
            end_time = timer.time() - start_time
            stats.result['CPU_time'] = end_time
            stats.result['solution_length'] = len(curr.path())
            stats.result['avg_h'] = statistics.mean(h_vals)
            return curr, stats
        for action in curr.state.actions(state):
            result = curr.state.result(state, action)
            if result not in closed_list:
                closed_list.append(result)
                child_puzzle = EightPuzzle(initial=result, goal=puzzle.goal)
                h = h_lookup(heuristic, result)
                h_vals.append(h)
                child = Node(state=child_puzzle, parent=curr, h_val=h, depth=curr.depth+1)
                open_list.push(child)
            count += 1

    return None