from statistics import mean
import pprint as pp

class Statistics:
    def __init__(self, algo):
        self.result = {
            'algorithm': algo,
            'expanded_nodes': 0,
            'solution_length': 0,
            'CPU_time': 0.0,
            'avg_h': 0
        }


def get_stats(report, stats):
    report['nodes'].append(stats.result['expanded_nodes'])
    report['cost'].append(stats.result['solution_length'])
    report['time'].append(stats.result['CPU_time'])
    report['h_vals'].append(stats.result['avg_h'])


def get_summary(report):
    report["avg_cost"] = mean(report["cost"])
    report["avg_nodes"] = mean(report["nodes"])
    report["avg_time"] = mean(report["time"])
    report["avg_hvals"] = mean(report["h_vals"])

    pp.pprint(f"Average expanded nodes: {report['avg_nodes']}")
    pp.pprint(f"Average time:           {round(report['avg_time'], 2)}")
    pp.pprint(f"Average cost:           {report['avg_cost']}")
    pp.pprint(f"Average h value:        {round(report['avg_hvals'], 2)}")


def read_test(file):
    tup = ()
    with open(file, 'r') as f:
        for line in f:
            line = line.split(',')
            tup = line
    return tup


def read_pdb(num):
    table = dict()
    with open(f"pdb/disjoint_pdb{num}.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            value = str(line).partition(':')[2].partition('}')[0]
            line = '(' + str(line).partition('(')[2].partition(')')[0] + ')'
            table[str(line)] = int(value)

    return table

