def manhattan_distance(puzzle):
    state = puzzle.initial
    index_goal = {} #{0: [2, 2], 1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1]}
    index_state = {}
    index = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

    for i in range(len(state)):
        index_state[state[i]] = index[i]
        index_goal[puzzle.goal[i]] = index[i]

    ymhd = 0
    xmhd = 0

    for i in range(len(state)):
        xmhd += abs(index_goal[i][0] - index_state[i][0])
        ymhd += abs(index_goal[i][1] - index_state[i][1])

    mhd = ymhd + xmhd

    return mhd
