from pulp import *

def get_index_string(a: int, b: int = None):
    if b == None:
        return f"{str(a)}"
    return f"{str(a)}-{str(b)}"

class FacilitiesProblem:
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


    def read_problem(self, filename: str):
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

    def create_minimize_pulp_problem(self) -> LpProblem:
        prob = LpProblem("Facilities", LpMinimize)

        x_vars = {}
        y_vars = {}

        for i in range(0, self.n):
            y_vars[get_index_string(i)] = LpVariable(f'y_{get_index_string(i)}', 0, 1, cat='Integer')
            for j in range(0, self.m):
                x_vars[get_index_string(i, j)] = LpVariable(f'x_{get_index_string(i, j)}', 0, 1)

        prob += (
            lpSum([self.f[i] * y_vars[get_index_string(i)] for i in range(self.n)]) +
            lpSum([(self.c)[j][i] * x_vars[get_index_string(i, j)] for i in range(self.n) for j in range(self.m)]),
            "Objective Func",
        )

        for j in range(self.m):
            prob += (
                lpSum([x_vars[get_index_string(i, j)] for i in range(self.n)]) == 1,
                f"Demanda 1.{j}",
            )

        for i in range(self.n):
            prob += (
                lpSum([(self.d[j] * x_vars[get_index_string(i, j)]) for j in range(self.m)]) <= self.cap[i],
                f"Demanda 2.{i}",
            )

        for i in range(self.n):
            for j in range(self.m):
                prob += (
                    x_vars[get_index_string(i, j)] <= y_vars[get_index_string(i)],
                    f"Demanda 3.{i}_{j}"
                )

        return prob



solver = getSolver('GUROBI_CMD')          

instance = FacilitiesProblem()
instance.read_problem('../instancias/Adaptada-wlp01.txt')
prob = instance.create_minimize_pulp_problem()

prob.solve(solver)
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", str(v.varValue))
print("Minimum cost found = ", value(prob.objective))
