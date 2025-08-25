"""
Sokoban Solver using SAT (Boilerplate)
--------------------------------------
Instructions:
- Implement encoding of Sokoban into CNF.
- Use PySAT to solve the CNF and extract moves.
- Ensure constraints for player movement, box pushes, and goal conditions.

Grid Encoding:
- 'P' = Player
- 'B' = Box
- 'G' = Goal
- '#' = Wall
- '.' = Empty space
"""

from pysat.formula import CNF
from pysat.solvers import Solver

# Directions for movement
DIRS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

class SokobanEncoder:
    def __init__(self, grid, T):
        """
        Initialize encoder with grid and time limit.

        Args:
            grid (list[list[str]]): Sokoban grid.
            T (int): Max number of steps allowed.
        """
        self.grid = grid
        self.T = T
        self.N = len(grid)
        self.M = len(grid[0])

        self.goals = []
        self.boxes = []
        self.walls = []
        self.player_start = None

        # TODO: Parse grid to fill self.goals, self.boxes, self.player_start
        self._parse_grid()

        self.num_boxes = len(self.boxes)
        self.cnf = CNF()

    def _parse_grid(self):
        """Parse grid to find player, boxes, and goals."""
        # TODO: Implement parsing logic
        for i in range(self.N):
            for j in range(self.M):
                if(self.grid[i][j] == 'P'):
                    self.player_start = (i,j)
                if(self.grid[i][j] == 'B'):
                    self.boxes.append((i,j))
                if(self.grid[i][j] == 'G'):
                    self.goals.append((i,j))
                if(self.grid[i][j] == '#'):
                    self.walls.append((i,j))
        

    # ---------------- Variable Encoding ----------------
    def var_player(self, x, y, t):
        """
        Variable ID for player at (x, y) at time t.
        """
        # TODO: Implement encoding scheme
        return x*(self.M)*(self.T + 1) + y*(self.T + 1) + (t+1) 
    
    def var_box(self, b, x, y, t):
        """
        Variable ID for box b at (x, y) at time t.
        """
        # TODO: Implement encoding scheme
        # Fixed: Add offset to avoid conflict with player variables
        offset = self.N * self.M * (self.T + 1)
        return offset + (b+1)*(self.M)*(self.T + 1)*(self.N) + x*(self.M)*(self.T + 1) + y*(self.T + 1) + (t+1)

    # ---------------- Encoding Logic ----------------
    def encode(self):
        """
        Build CNF constraints for Sokoban:
        - Initial state
        - Valid moves (player + box pushes)
        - Non-overlapping boxes
        - Goal condition at final timestep
        """
        # TODO: Add constraints for:
        valid_cells = [(x, y) for x in range(self.N) for y in range(self.M) if (x, y) not in self.walls]

        # 1. Initial conditions
        xp,yp = self.player_start
        self.cnf.append([self.var_player(xp,yp,0)])   # Player 
        for i in range(self.num_boxes):
            xb,yb = self.boxes[i]                    # Boxes
            self.cnf.append([self.var_box(i,xb,yb,0)])

        # 2. Player movement
        for t in range(self.T): # Player can only move when time < T
            for i in range(self.N):
                for j in range(self.M):
                    if (i,j) in self.walls:  # Fixed: Skip walls
                        continue
                    move_list = [-self.var_player(i,j,t)]
                    # Can stay in same place
                    move_list.append(self.var_player(i,j,t+1))
                    for (dx,dy) in DIRS.values():
                        x1 = i + dx
                        y1 = j + dy
                        if 0<=x1<self.N and 0<=y1<self.M and (x1,y1) not in self.walls:
                            move_list.append(self.var_player(x1,y1,t+1))
                    self.cnf.append(move_list)
                    
        # 3. Box movement (push rules)
        # for t in range(self.T):
        #     for i in range(self.N):
        #         for j in range(self.M):
        #             if (i,j) in self.walls:  # Fixed: Skip walls
        #                 continue
        #             for b in range(self.num_boxes):
        #                 # Fixed: Proper box push logic
        #                 for d,(dx,dy) in DIRS.items():
        #                     x1 = i + dx  # box destination
        #                     y1 = j + dy
        #                     px = i - dx  # player push position
        #                     py = j - dy
                            
        #                     if (0<=x1<self.N and 0<=y1<self.M and (x1,y1) not in self.walls and
        #                         0<=px<self.N and 0<=py<self.M and (px,py) not in self.walls):
                                
        #                         # If box at (i,j) and player pushes from (px,py) to (i,j), box must move to (x1,y1)
        #                         self.cnf.append([-self.var_box(b,i,j,t),-self.var_player(px,py,t),-self.var_player(i,j,t+1),self.var_box(b,x1,y1,t+1)])
                                
        #                         # If box moves from (i,j) to (x1,y1), must have been pushed
        #                         self.cnf.append([-self.var_box(b,i,j,t),-self.var_box(b,x1,y1,t+1),self.var_player(px,py,t)])
        #                         self.cnf.append([-self.var_box(b,i,j,t),-self.var_box(b,x1,y1,t+1),self.var_player(i,j,t+1)])
                        
        #                 # Fixed: If box not pushed, it stays
        #                 no_push = []
        #                 for (dx,dy) in DIRS.values():
        #                     px = i - dx
        #                     py = j - dy
        #                     if 0<=px<self.N and 0<=py<self.M and (px,py) not in self.walls:
        #                         no_push.append(self.var_player(px,py,t))
        #                         no_push.append(-self.var_player(i,j,t+1))
                        
        #                 if no_push:
        #                     self.cnf.append([-self.var_box(b,i,j,t),self.var_box(b,i,j,t+1)] + no_push)


            for b in range(len(self.boxes)):
                        for t in range(self.T):
                            for x, y in valid_cells:
                                
                                possible_reasons = []
                                
                                # 1- Box stayed in same position
                                possible_reasons.append(self.var_box(b, x, y, t))
                                
                                # 2- Box was pushed from each possible direction
                                for (dx, dy) in DIRS.values():
                                    from_x, from_y = x - dx, y - dy  # where box was pushed from
                                    player_at_x, player_at_y = x - 2 * dx, y - 2 * dy  # where player pushed from
                                    
                                    # Check if this push scenario is physically possible
                                    if (0 <= from_x < self.N and 0 <= from_y < self.M and 0 <= player_at_x < self.N and 0 <= player_at_y < self.M and
                                        (from_x, from_y) not in self.walls and (player_at_x, player_at_y) not in self.walls):
                                        
                                        
                                        # If box moved due to this push, ensure push conditions
                                        # (box at destination) ∧ (box was at source) → push conditions must hold
                                        self.cnf.append([-self.var_box(b, x, y, t + 1), -self.var_box(b, from_x, from_y, t), self.var_player(player_at_x, player_at_y, t)])
                                        self.cnf.append([-self.var_box(b, x, y, t + 1), -self.var_box(b, from_x, from_y, t), self.var_player(from_x, from_y, t + 1)])
                                        
                                        # Add this as a possible reason box is at (x,y)
                                        possible_reasons.append(self.var_box(b, from_x, from_y, t))
                                
                                # Box at (x,y) at t+1 requires at least one valid reason
                                if possible_reasons:
                                    temp = [-self.var_box(b, x, y, t + 1)] + possible_reasons
                                    self.cnf.append(temp)
                    





        # 4. Non-overlap constraints
        for t in range(self.T + 1):
            for w in range(len(self.walls)): # if wall, then no player or box
                xw,yw = self.walls[w]
                self.cnf.append([-self.var_player(xw,yw,t)])
                for b in range(self.num_boxes):
                    self.cnf.append([-self.var_box(b,xw,yw,t)])
            for i in range(self.N):
                for j in range(self.M):
                    for b in range(self.num_boxes): # No 2 boxes in same place
                        for b0 in range(self.num_boxes):
                            if(b0 != b):
                                self.cnf.append([-self.var_box(b,i,j,t),-self.var_box(b0,i,j,t)])

                        self.cnf.append([-self.var_player(i,j,t),-self.var_box(b,i,j,t)]) # either player or box or none
        
        # 5. Goal conditions
        # Fixed: Each box must be on some goal
        for i in range(self.num_boxes):
            self.cnf.append([self.var_box(i,g[0],g[1],self.T) for g in self.goals])

        # 6. Other conditions
        for t in range(0,self.T + 1):
            p1 = []
            for i in range(0,self.N): # atleast 1 player
                for j in range(0,self.M):
                    if (i,j) not in self.walls:  # Fixed: Only valid positions
                        p1.append(self.var_player(i,j,t))
            self.cnf.append(p1)

            for i in range(self.N):
                for j in range(self.M):
                    for i1 in range(i, self.N):
                        for j1 in range(self.M):
                            if (i1 > i) or (i1 == i and j1 > j):
                                self.cnf.append([-self.var_player(i,j,t),-self.var_player(i1,j1,t)])

            # for boxes
            for b in range(0,self.num_boxes):
                p2 = []
                for i in range(0,self.N): # atleast 1 box
                    for j in range(0,self.M):
                        if (i,j) not in self.walls:  # Fixed: Only valid positions
                            p2.append(self.var_box(b,i,j,t))
                self.cnf.append(p2)

                for i in range(self.N):
                    for j in range(self.M):
                        for i1 in range(i, self.N):
                            for j1 in range(self.M):
                                if (i1 > i) or (i1 == i and j1 > j):
                                    self.cnf.append([-self.var_box(b,i,j,t),-self.var_box(b,i1,j1,t)])

        return self.cnf
                    
def decode(model, encoder):
    """
    Decode SAT model into list of moves ('U', 'D', 'L', 'R').

    Args:
        model (list[int]): Satisfying assignment from SAT solver.
        encoder (SokobanEncoder): Encoder object with grid info.

    Returns:
        list[str]: Sequence of moves.
    """
    N, M, T = encoder.N, encoder.M, encoder.T

    # TODO: Map player positions at each timestep to movement directions
    # x*(self.M)*(self.T + 1) + y*(self.T + 1) + (t+1)
    # (b+1)*(self.M)*(self.T + 1)*(self.N) + x*(self.M)*(self.T + 1) + y*(self.T + 1) + (t+1)

    check = {v for v in model if v > 0}
    dec_path = [None]*(T+1)
    
    # Fixed: Use correct threshold for separating player and box variables
    player_var_max = N * M * (T + 1)
    
    for v in check:
        if v <= player_var_max:  # Fixed: This is a player variable
            v = v-1
            t = v % (T+1)
            v = (v - t)//(T+1)
            y = v % M
            x = (v - y)//M
            dec_path[t] = (x,y)

    path = []
    for t in range(T): # since only T moves are possible
        if dec_path[t] is not None and dec_path[t + 1] is not None:
            x1, y1 = dec_path[t]
            x2, y2 = dec_path[t + 1]
            
            for d, (dx, dy) in DIRS.items(): # parse all directions
                if (x2 - x1, y2 - y1) == (dx, dy):
                    path.append(d)
                    break
                # If no movement found and dec_path are the same, player stayed (don't add move)

    return path

def solve_sokoban(grid, T):
    """
    DO NOT MODIFY THIS FUNCTION.

    Solve Sokoban using SAT encoding.

    Args:
        grid (list[list[str]]): Sokoban grid.
        T (int): Max number of steps allowed.

    Returns:
        list[str] or "unsat": Move sequence or unsatisfiable.
    """
    encoder = SokobanEncoder(grid, T)
    cnf = encoder.encode()

    with Solver(name='g3') as solver:
        # for clause in cnf:
        #     print(clause)
        solver.append_formula(cnf)
        if not solver.solve():
            return -1

        model = solver.get_model()
        if not model:
            return -1

        return decode(model, encoder)