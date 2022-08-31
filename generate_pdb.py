import time

from heuristics.pdb import generate_disjoint_pdb

if __name__=="__main__":
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

    print(f"Generating disjoint_pdb1.txt ...")
    pdb1_start = time.time()
    generate_disjoint_pdb(pattern1, 1)
    pdb1_end = time.time()
    print(f"Done. Total time is {round(pdb1_end-pdb1_start, 2)}s")

    print(f"Generating disjoint_pdb2.txt ...")
    pdb2_start = time.time()
    generate_disjoint_pdb(pattern2, 2)
    pdb2_end = time.time()
    print(f"Done. Total time is {round(pdb2_end-pdb2_start, 2)}s")

    print(f"Generating disjoint_pdb3.txt ...")
    pdb3_start = time.time()
    generate_disjoint_pdb(pattern3, 3)
    pdb3_end = time.time()
    print(f"Done. Total time is {round(pdb3_end-pdb3_start, 2)}s")