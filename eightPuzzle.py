'''
    Using the AIMA python repo implementations with some modifications.
    Heuristics added are in aima/search.py 'EightPuzzle' class definition
'''

import time
import random
import os

from aima.search import astar_search
from aima.search import EightPuzzle



def readPathInfo():
    file = open('pathInfo.txt', 'r')
    pathInfo = file.readlines()
    file.close()
    os.remove('pathInfo.txt')

    return pathInfo

def report(report_name, entry):
    data = ''
    if os.path.exists(report_name):
        file = open(report_name, 'r')
        data = file.read()
        file.close()

    file = open(report_name, 'w')
    file.write(data)
    file.write(entry)
    file.close()

def get_random_initial_state():
        initial = (3, 2, 0, 4, 6, 8, 1, 5, 7)
        while not EightPuzzle.check_solvability(initial):
            initial = tuple(random.sample((1, 2, 3, 4, 5, 6, 7, 8, 0), 9))
        return initial

def run_heuristic(problem, h):
    start = time.time()
    search_results = astar_search(problem, h, display=True).state
    exe_time = float(time.time()-start)
    entry = '{} ==> {:.2f} s\n{}\n'.format(h.__name__, exe_time, readPathInfo())
    return entry

def run(n):
    report_name = 'report_{}.txt'.format(time.time())
    data = []

    for i in range(n):
        entry = ''
        # Random solvable initial state
        initial = get_random_initial_state()
        entry += str(initial) + '\n'

        problem = EightPuzzle(initial)
        entry += run_heuristic(problem, problem.h)

        problem = EightPuzzle(initial)
        entry += run_heuristic(problem, problem.manhatten)

        problem = EightPuzzle(initial)
        entry += run_heuristic(problem, problem.nillson)
        entry += '\n'

        data.append(entry)
        print(entry)
        report(report_name, entry)

    return data


def main():
 
    data = run(40)

main()
