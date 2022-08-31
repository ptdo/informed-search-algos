def hamming_distance(puzzle):
    hmd = 0
    state = puzzle.initial
    goal_state = puzzle.goal
    for idx, x in enumerate(state):
        if x != 0 and goal_state[idx] != x:
            hmd += 1
    return hmd