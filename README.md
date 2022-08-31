# Implement Informed Search Algorithms With Different Heuristics

## Pre-requisites
matplotlib package for visualizing results: `pip install matplotlib`

## Generate Test Instances 

`python generate_tests.py`

This will generate 100 solvable 8-puzzle boards, each is stored in a text file, in tests/ folder
. Run this only when more test cases are needed, as the test files are already generated for report purposes.

## Generate Disjoint Pattern Database Files 
`python generate_pdb.py`

## Generate Experiment Results for A* Search Algorithm
`python a_main.py`

## Generate Experiment Results for IDA* Search Algorithm
`python ida_main.py`

## Run A* with Hamming Distance
`python hamming_main.py`