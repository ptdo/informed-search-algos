def linearConflict(puzzle):
    state = puzzle.initial
    index_goal = {} #{0: [2, 2], 1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1]}
    index_state = {}
    index = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    lc = 0
    confCount = 0
    confTable = [()]#[(1,2,3,6),(0,2,4,7),(0,1,5,8),(0,4,5,6),(1,3,5,7),(2,3,4,8),(0,3,7,8),(1,4,6,8),(2,5,6,7)]
    conflicts = [()]


    for i in range(len(state)):
        index_state[state[i]] = index[i]
        index_goal[puzzle.goal[i]] = index[i]

    confTable.append((puzzle.goal[1],puzzle.goal[2],puzzle.goal[3],puzzle.goal[6]))
    confTable.append((puzzle.goal[0],puzzle.goal[2],puzzle.goal[4],puzzle.goal[7]))
    confTable.append((puzzle.goal[0],puzzle.goal[1],puzzle.goal[5],puzzle.goal[8]))

    confTable.append((puzzle.goal[0],puzzle.goal[4],puzzle.goal[5],puzzle.goal[6]))
    confTable.append((puzzle.goal[1],puzzle.goal[3],puzzle.goal[5],puzzle.goal[7]))
    confTable.append((puzzle.goal[2],puzzle.goal[3],puzzle.goal[4],puzzle.goal[8]))

    confTable.append((puzzle.goal[0],puzzle.goal[3],puzzle.goal[7],puzzle.goal[8]))
    confTable.append((puzzle.goal[1],puzzle.goal[4],puzzle.goal[6],puzzle.goal[8]))
    confTable.append((puzzle.goal[2],puzzle.goal[5],puzzle.goal[6],puzzle.goal[7]))

    if confTable[0] == ():
        confTable.pop(0)
    if conflicts[0] == ():
        conflicts.pop(0)

    ymhd = 0
    xmhd = 0

    for i in range(len(state)):
        currYd = abs(index_goal[i][0] - index_state[i][0])
        currXd = abs(index_goal[i][1] - index_state[i][1])
        xmhd += currXd
        ymhd += currYd

        if state[i] == 0 or state[state[i]] == 0:
            continue
        if state[i] in confTable[i] and state[state[i]] == puzzle.goal[i]:
            if state[i]<puzzle.goal[i]:
                if (state[i],puzzle.goal[i]) not in conflicts:
                    conflicts.append((state[i],puzzle.goal[i]))
            else:
                if (puzzle.goal[i],state[i]) not in conflicts:
                    conflicts.append((puzzle.goal[i],state[i]))
            confCount += 1


        if (currYd == 2 and currXd == 0): #index and goal opposite row, same col
            if state[3+index_state[i][1]] == puzzle.goal[3+index_state[i][1]]:  #middle row object in goal loc
                if state[i]<puzzle.goal[i]:
                    if (state[i],puzzle.goal[i]) not in conflicts:
                        conflicts.append((state[i],puzzle.goal[i]))
                else:
                    if (puzzle.goal[i],state[i]) not in conflicts:
                        conflicts.append((puzzle.goal[i],state[i]))
                confCount += 1

        elif (currYd == 0 and currXd == 2): #same row, opposite col
            if state[1+3*index_state[i][0]] == puzzle.goal[1+3*index_state[i][0]]:  #middle col object in goal loc
                if state[i]<puzzle.goal[i]:
                    if (state[i],puzzle.goal[i]) not in conflicts:
                        conflicts.append((state[i],puzzle.goal[i]))
                else:
                    if (puzzle.goal[i],state[i]) not in conflicts:
                        conflicts.append((puzzle.goal[i],state[i]))
                confCount += 1 

    mhd = ymhd + xmhd
    lc = 2 * confCount + mhd
    return lc
