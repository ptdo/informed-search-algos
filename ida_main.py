import time
import matplotlib.pyplot as mpl

from puzzle import EightPuzzle
from algorithms.ida_star import ida_star
from stats import get_stats, get_summary, read_pdb, read_test


if __name__ == '__main__':

    pattern1 = [
        (1,2,3,-1,-1,-1,-1,-1,0),
        (-1,-1,-1,4,5,6,7,8,0)
    ]

    pattern2 = [
        (-1,2,3,-1,-1,-1,7,-1,0),
        (1,-1,-1,4,5,-1,-1,-1,0),
        (-1,-1,-1,-1,-1,6,-1,8,0)
    ]

    pattern3 = [
        (-1,2,3,-1,-1,6,7,-1,0),
        (1,-1,-1,4,5,-1,-1,8,0),
    ]

    # Load txt file into dictionary
    table1 = read_pdb(1)
    table2 = read_pdb(2)
    table3 = read_pdb(3)

    md = {'nodes': [], 'cost': [], 'time':[], 'h_vals': [], 'avg_cost': 0, 'avg_nodes': 0, 'avg_hvals': 0, 'avg_time': 0}
    lc = {'nodes': [], 'cost': [], 'time':[], 'h_vals': [], 'avg_cost': 0, 'avg_nodes': 0, 'avg_hvals': 0, 'avg_time': 0}
    pdb1 = {'nodes': [], 'cost': [], 'time':[], 'h_vals': [], 'avg_cost': 0, 'avg_nodes': 0, 'avg_hvals': 0, 'avg_time': 0}
    pdb2 = {'nodes': [], 'cost': [], 'time':[], 'h_vals': [], 'avg_cost': 0, 'avg_nodes': 0, 'avg_hvals': 0, 'avg_time': 0}
    pdb3 = {'nodes': [], 'cost': [], 'time':[], 'h_vals': [], 'avg_cost': 0, 'avg_nodes': 0, 'avg_hvals': 0, 'avg_time': 0}

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
                tt = time.localtime()
                print(f"Solving Puzzle #{count}", '     LocalTime =  ', tt.tm_hour,':',str(tt.tm_min).rjust(2,'0'),':',str(tt.tm_sec).rjust(2,'0'))
                print("   Puzzle:   ", initial)

            # IDA* with 3-5 disjoint PDB
            sol, stats = ida_star(puzzle, heuristic="pdb", patterns=pattern1,lookup_table=table1)
            get_stats(pdb1, stats)

            # IDA* with 3-3-2 disjoint PDB
            sol, stats = ida_star(puzzle, heuristic="pdb", patterns=pattern2,lookup_table=table2)
            get_stats(pdb2, stats)

            # IDA* with 4-4 disjoint PDB
            sol, stats = ida_star(puzzle, heuristic="pdb", patterns=pattern3,lookup_table=table3)
            get_stats(pdb3, stats)

        count += 1

    end = time.time()

    print(f"DONE. TOTAL TIME IS \t {end-start} \n")
    
    print('=========== IDA* with disjoint PDB: 3-5 =========== \n')
    get_summary(pdb1)

    print('=========== IDA* with disjoint PDB: 3-3-2 =========== \n')
    get_summary(pdb2)

    print('=========== IDA* with disjoint PDB: 4-4 =========== \n')
    get_summary(pdb3)
    
    x = list(range(count))
    

    mpl.plot(x,pdb2["time"],label='PDB: 3-3-2')
    mpl.plot(x,pdb1["time"],label='PDB: 3-5')
    mpl.plot(x,pdb3["time"],label='PDB: 4-4')
    mpl.title("PDB: CPU Time Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('CPU Time') 
    mpl.savefig('ida_graphs/time_pdb.png')


    mpl.plot(x,pdb1["nodes"],label='PDB: 3-5')
    mpl.plot(x,pdb2["nodes"],label='PDB: 3-3-2')
    mpl.plot(x,pdb3["nodes"],label='PDB: 4-4') 
    mpl.title("PDB: Expanded Nodes Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('# of Nodes') 
    mpl.savefig('ida_graphs/nodes_pdb.png')


    mpl.plot(x,pdb1["h_vals"],label='PDB: 3-5 ')
    mpl.plot(x,pdb2["h_vals"],label='PDB: 3-3-2 ')
    mpl.plot(x,pdb3["h_vals"],label='PDB: 4-4')
    mpl.title("PDB: Average Heuristic Value Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('Avg h(n)') 
    mpl.savefig('ida_graphs/hval_pdb.png')

    mpl.plot(x,pdb1["cost"],label='PDB: 3-5')
    mpl.plot(x,pdb2["cost"],label='PDB: 3-3-2')
    mpl.plot(x,pdb3["cost"],label='PDB: 4-4') 
    mpl.title("PDB: Cost Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('Cost') 
    mpl.savefig('ida_graphs/cost_pdb.png')


    label = ['3-5', '3-3-2', '4-4']


    data_time = [pdb1['avg_time'], pdb2['avg_time'], pdb3['avg_time']]
    mpl.bar(label, data_time)
    mpl.xlabel('Heuristic Types')
    mpl.ylabel('Avg CPU Time')
    mpl.title('Average CPU Time Per Heuristic')
    mpl.savefig('ida_graphs/time_heuristic.png')

    data_cost = [pdb1['avg_cost'], pdb2['avg_cost'], pdb3['avg_cost']]
    mpl.bar(label, data_cost)
    mpl.xlabel('Heuristic Types')
    mpl.ylabel('Avg Cost')
    mpl.title('Average Cost Per Heuristic')
    mpl.savefig('ida_graphs/cost_heuristic.png')


    data_nodes = [pdb1['avg_nodes'], pdb2['avg_nodes'], pdb3['avg_nodes']]
    mpl.bar(label, data_nodes)
    mpl.xlabel('Heuristic Types')
    mpl.ylabel('Avg # of Nodes ')
    mpl.title('Average Expanded Nodes Per Heuristic')
    mpl.savefig('ida_graphs/nodes_heuristic.png')


    data_h = [pdb1['avg_hvals'],pdb2['avg_hvals'], pdb3['avg_hvals']]
    mpl.bar(label, data_h)
    mpl.xlabel('Heuristic Types')
    mpl.ylabel('Avg h(n)')
    mpl.title('Average h(n) Per Heuristic')
    mpl.savefig('ida_graphs/hvals_heuristic.png')
    mpl.figure(12)