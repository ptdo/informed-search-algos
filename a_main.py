import time
import matplotlib.pyplot as mpl

from puzzle import EightPuzzle
from stats import get_stats, get_summary, read_pdb, read_test
from algorithms.a_star import a_star


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

            # A* with 3-5 disjoint PDB
            sol, stats = a_star(puzzle, heuristic="pdb", patterns=pattern1,lookup_table=table1)
            get_stats(pdb1, stats)

            # A* with 3-3-2 disjoint PDB
            sol, stats = a_star(puzzle, heuristic="pdb", patterns=pattern2,lookup_table=table2)
            get_stats(pdb2, stats)


            # A* with 4-4 disjoint PDB
            sol, stats = a_star(puzzle, heuristic="pdb", patterns=pattern3,lookup_table=table3)
            get_stats(pdb3, stats)
            

            # A* with Linear Conflict
            sol, stats = a_star(puzzle, heuristic="lc")
            get_stats(lc, stats)


            # A* with Manhattan Distance
            sol, stats = a_star(puzzle, heuristic="manhattan")
            get_stats(md, stats)

        count += 1

    end = time.time()

    print(f"DONE. TOTAL TIME IS \t {end-start} \n")

    print('=========== A* with Manhattan Distance =========== \n')
    get_summary(md)

    print('=========== A* with Linear Conflict =========== \n')
    get_summary(lc)
    
    print('=========== A* with disjoint PDB: 3-5 =========== \n')
    get_summary(pdb1)

    print('=========== A* with disjoint PDB: 3-3-2 =========== \n')
    get_summary(pdb2)
    
    print('=========== A* with disjoint PDB: 4-4 =========== \n')
    get_summary(pdb3)


    # Graphs
    x = list(range(count))

    mpl.plot(x,md["time"],label='MD')
    mpl.plot(x,lc["time"],label='LC')
    mpl.plot(x,pdb2["time"],label='PDB: 3-3-2')

    mpl.title("CPU Time Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('CPU Time') 
    mpl.savefig('a_graphs/time.png')
    mpl.figure(1)


    mpl.plot(x,md["nodes"],label='MD')
    mpl.plot(x,lc["nodes"],label='LC')
    mpl.plot(x,pdb2["nodes"],label='PDB: 3-3-2')

    mpl.title("Expanded Nodes Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('# of Nodes') 
    mpl.savefig('a_graphs/nodes.png')
    mpl.figure(2)


    mpl.plot(x,md['h_vals'],label='MD')
    mpl.plot(x,lc["h_vals"],label='LC')
    mpl.plot(x,pdb2["h_vals"],label='PDB: 3-3-2')

    mpl.title("Average Heuristic Value Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('h(n)') 
    mpl.savefig('a_graphs/hval.png')
    mpl.figure(3)

    mpl.plot(x,md["cost"],label='MD')
    mpl.plot(x,lc["cost"],label='LC')
    mpl.plot(x,pdb2["cost"],label='PDB: 3-3-2')

    mpl.title("Cost Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('Cost') 
    mpl.savefig('a_graphs/cost.png')
    mpl.figure(4)


    mpl.plot(x,pdb2["time"],label='PDB: 3-3-2')
    mpl.plot(x,pdb1["time"],label='PDB: 3-5')
    mpl.plot(x,pdb3["time"],label='PDB: 4-4')
    mpl.title("PDB: CPU Time Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('CPU Time') 
    mpl.savefig('a_graphs/time_pdb.png')
    mpl.figure(5)


    mpl.plot(x,pdb1["nodes"],label='PDB: 3-5')
    mpl.plot(x,pdb2["nodes"],label='PDB: 3-3-2')
    mpl.plot(x,pdb3["nodes"],label='PDB: 4-4') 
    mpl.title("PDB: Expanded Nodes Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('# of Nodes') 
    mpl.savefig('a_graphs/nodes_pdb.png')
    mpl.figure(6)


    mpl.plot(x,pdb1["h_vals"],label='PDB: 3-5 ')
    mpl.plot(x,pdb2["h_vals"],label='PDB: 3-3-2 ')
    mpl.plot(x,pdb3["h_vals"],label='PDB: 4-4')
    mpl.title("PDB: Average Heuristic Value Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('Avg h(n)') 
    mpl.savefig('a_graphs/hval_pdb.png')
    mpl.figure(7)

    mpl.plot(x,pdb1["cost"],label='PDB: 3-5')
    mpl.plot(x,pdb2["cost"],label='PDB: 3-3-2')
    mpl.plot(x,pdb3["cost"],label='PDB: 4-4') 
    mpl.title("PDB: Cost Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('Cost') 
    mpl.savefig('a_graphs/cost_pdb.png')
    mpl.figure(8)


    label = ['MD', 'LC', '3-5', '3-3-2', '4-4']

    data_time = [md['avg_time'], lc['avg_time'], pdb1['avg_time'], \
        pdb2['avg_time'], pdb3['avg_time']]
    mpl.bar(label, data_time)
    mpl.xlabel('Heuristic Types')
    mpl.ylabel('Avg CPU Time')
    mpl.title('Average CPU Time Per Heuristic')
    mpl.savefig('a_graphs/time_heuristic.png')
    mpl.figure(9)
    

    data_cost = [md['avg_cost'], lc['avg_cost'], pdb1['avg_cost'], \
        pdb2['avg_cost'], pdb3['avg_cost']]
    mpl.bar(label, data_cost)
    mpl.xlabel('Heuristic Types')
    mpl.ylabel('Avg Cost')
    mpl.title('Average Cost Per Heuristic')
    mpl.savefig('a_graphs/cost_heuristic.png')
    mpl.figure(10)


    data_nodes = [md['avg_nodes'], lc['avg_nodes'], pdb1['avg_nodes'], \
        pdb2['avg_nodes'], pdb3['avg_nodes']]
    mpl.bar(label, data_nodes)
    mpl.xlabel('Heuristic Types')
    mpl.ylabel('Avg # of Nodes ')
    mpl.title('Average Expanded Nodes Per Heuristic')
    mpl.savefig('a_graphs/nodes_heuristic.png')
    mpl.figure(11)


    data_h = [md['avg_hvals'], lc['avg_hvals'], pdb1['avg_hvals'], \
        pdb2['avg_hvals'], pdb3['avg_hvals']]
    mpl.bar(label, data_h)
    mpl.xlabel('Heuristic Types')
    mpl.ylabel('Avg h(n)')
    mpl.title('Average h(n) Per Heuristic')
    mpl.savefig('a_graphs/hvals_heuristic.png')
    mpl.figure(12)


    mpl.plot(x,md["nodes"],label='MD')
    mpl.plot(x,lc["nodes"],label='LC')
    mpl.plot(x,pdb2["nodes"],label='PDB: 3-3-2')

    mpl.title("Expanded Nodes Per Puzzle")
    mpl.legend()
    mpl.xlabel('Puzzle #') 
    mpl.ylabel('# of Nodes') 
    mpl.savefig('a_graphs/nodes.png')
    mpl.figure(13)