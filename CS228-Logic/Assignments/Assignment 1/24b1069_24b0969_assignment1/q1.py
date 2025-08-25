"""
sudoku_solver.py

Implement the function `solve_sudoku(grid: List[List[int]]) -> List[List[int]]` using a SAT solver from PySAT.
"""

from pysat.formula import CNF
from pysat.solvers import Solver
from typing import List

#xij_k is the variable thats defined to be true when the digit in box(i,j) is k
#There are 729 such variables as 81 boxes and 9 possibilities(1-9) for each
#Now ,the propositional statements are....
#   1)each row and column should not have any repeating digit, and should have all of 1-9
#   2)each 3X3 subgrid should not have any repeating digit, and should have all of 1-9
#   3)each cell i,j should have atleast 1 true xij_k and not more than 1(xij_k1 and xij_k2 both cant be true)<- each cell should have only 1 digit

def solve_sudoku(grid: List[List[int]]) -> List[List[int]]:
    """Solves a Sudoku puzzle using a SAT solver. Input is a 2D grid with 0s for blanks."""
    sudoku = CNF()
    def x(i,j,k):
        # using a 3-digit number to represent the propositional variable
        return 100*(i) + 10*(j) + k
    
    # 3) each cell must have at least one digit(1-9)
    for i in range(9):
        for j in range(9):
            # (xij_1 V xij_2 V ... V xij_9)
            sudoku.append([x(i,j,k) for k in range(1,10)])
            
    # 3) each cell must have at most one digit(1-9)
    for i in range(9):
        for j in range(9):
            for k1 in range(1,10):
                for k2 in range(k1 + 1,10):
                    # (~xij_k1 V ~xij_k2)
                    sudoku.append([-x(i,j,k1),-x(i,j,k2)])
    
    # 1) each row and column should have all the digits (At least one of each k)
    for i in range(9): 
        for k in range(1,10): 
            sudoku.append([x(i,j,k) for j in range(9)])
    for j in range(9):
        for k in range(1,10):
            sudoku.append([x(i,j,k) for i in range(9)])

    # 1) each row and column should not have any repeating digit (At most one of each k)
    for i in range(9):
        for k in range(1, 10):
            for j1 in range(9):
                for j2 in range(j1 + 1, 9):
                    sudoku.append([-x(i, j1, k), -x(i, j2, k)])
    for j in range(9):
        for k in range(1, 10):
            for i1 in range(9):
                for i2 in range(i1 + 1, 9):
                    sudoku.append([-x(i1, j, k), -x(i2, j, k)])

    # 2) each 3X3 subgrid should have all digits (At least one of each k)
    for t1 in range(0,9,3):
        for t2 in range(0,9,3):
            for k in range(1,10):
                sudoku.append([x(i+t1,j+t2,k) for i in range(3) for j in range(3)])
                
    # 2) each 3X3 subgrid should not have any repeating digit (At most one of each k)
    for k in range(1, 10):
        for t1 in range(0, 9, 3):
            for t2 in range(0, 9, 3):
                cells = [x(i + t1, j + t2, k) for i in range(3) for j in range(3)]
                for c1 in range(len(cells)):
                    for c2 in range(c1 + 1, len(cells)):
                        sudoku.append([-cells[c1], -cells[c2]])
    
    # for the given numbers in the input grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                sudoku.append([x(i, j, grid[i][j])])
    
    with Solver(name='glucose3') as solver:
        solver.append_formula(sudoku.clauses)
        if solver.solve():
            model = solver.get_model()
            sol = [[0 for _ in range(9)] for _ in range(9)]
            
            # filtering for positive literals (true variables)
            for x in model:
                if x > 0:
                    k = x % 10
                    j = (x // 10) % 10
                    i = x // 100
                    
                    sol[i][j] = k
            
            return sol
        else:
            return [[]]