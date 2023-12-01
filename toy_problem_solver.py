import argparse
import os
import time as t

from tqdm import tqdm
import orloge
from pulp import *


def init_parser():
    parser = argparse.ArgumentParser(
        prog='Facilities Solver',
        description='Given an instance of the facilities problem, solve it'
    )
    parser.add_argument('-f', '--folder', help='Folder where instances are stored')
    parser.add_argument('-s', '--solver', help=f'Available solvers: {list_solvers(onlyAvailable=True)}', default='PULP_CBC_CMD')
    parser.add_argument('-t', '--timelimit', help='Time limit in seconds')
    parser.add_argument('-p', '--problem', help='Problem version to use (1 or 2)')
    parser.add_argument('-v', '--verbose', action='store_true')
    if len(sys.argv) <= 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    return args


def get_index_string(a: int, b: int = None):
    if b == None:
        return f"{str(a)}"
    return f"{str(a)}-{str(b)}"


class FacilitiesProblem:
    # The variables are named according to the problem description (PDF)
    n: int 
    m: int
    cap: list[int]
    f: list[int]
    d: list[int]
    c: list[list[int]]

    def __init__(self):
        self.n = 0
        self.m = 0
        self.cap = []
        self.f = []
        self.d = []
        self.c = []
      
    @staticmethod
    def get_line_as_int_list(line: str) -> list[int]:
        split_line = line.split(' ')
        int_list = [int(n) for n in split_line]
        return int_list


    def read_problem_instance(self, filename: str):
        current_line_number = 0
        with open(filename, 'r') as file:
            lines = file.readlines()

            # Reads n, m
            self.n, self.m = FacilitiesProblem.get_line_as_int_list(lines[current_line_number])
            current_line_number += 1

            # Reads Cap, f
            for i in range(current_line_number, current_line_number + self.n):
                line = FacilitiesProblem.get_line_as_int_list(lines[i])
                self.cap.append(line[0])
                self.f.append(line[1])
            current_line_number += self.n

            # Reads d, c
            for i in range(current_line_number, current_line_number + self.m):
                line = FacilitiesProblem.get_line_as_int_list(lines[i])
                self.d.append(line[0])
                self.c.append(line[1:])
            current_line_number = i

    def create_minimize_pulp_problem_1(self) -> LpProblem:
        prob = LpProblem("Facilities", LpMinimize)

        x_vars = {}
        y_vars = {}

        for i in range(0, self.n):
            y_vars[get_index_string(i)] = LpVariable(f'y_{get_index_string(i)}', 0, 1, cat='integer')
            for j in range(0, self.m):
                x_vars[get_index_string(i, j)] = LpVariable(f'x_{get_index_string(i, j)}', 0, 1)

        prob += (
            lpSum([self.f[i] * y_vars[get_index_string(i)] for i in range(self.n)]) +
            lpSum([(self.c)[i][j] * x_vars[get_index_string(i, j)] for i in range(self.n) for j in range(self.m)]),
            "Objective Func",
        )

        for j in range(self.m):
            prob += (
                lpSum([x_vars[get_index_string(i, j)] for i in range(self.n)]) == 1,
                f"Demanda 1.{j}",
            )

        for i in range(self.n):
            prob += (
                lpSum([(self.d[j] * x_vars[get_index_string(i, j)]) for j in range(self.m)]) <= self.cap[i] * y_vars[get_index_string(i)],
                f"Demanda 2.{i}"
            )

        return prob


def main():
    args = init_parser()

    list_problem_info = []

    log_path = 'log.txt'

    try:
        solver = getSolver(args.solver, timeLimit=args.timelimit, msg=True)
    except KeyError as e:
        print(e) 

    for file in tqdm(sorted(os.listdir(args.folder))):
        instance = FacilitiesProblem()
        instance.read_problem_instance(f'{args.folder}{file}')
        if args.problem == '1':
            prob = instance.create_minimize_pulp_problem_1()
        else:
            print('ERROR: Failed to create')
            sys.exit(1)

        start = t.time()
        prob.solve(solver)
        end = t.time()

        problem_info = {
            'Name': file,
            #for v in prob.variables():
            'Variables': [str(v.name)+': '+str(v.varValue)+'\n' for v in prob.variables()],
            'Time to Solve': end - start,
            'Minimum cost found': value(prob.objective),
        }

        list_problem_info.append(problem_info)

        if args.verbose:
            print("Status:", LpStatus[prob.status])
            print("Minimum cost found = ", value(prob.objective))
    
    for problem_info in list_problem_info:
        for item in problem_info.items():
            print(item)



if __name__ == '__main__':
    main()