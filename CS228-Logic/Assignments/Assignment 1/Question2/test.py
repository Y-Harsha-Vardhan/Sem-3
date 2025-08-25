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
        self.N = len(grid)  # N-> vertical length
        self.M = len(grid[0]) # M -> horizontal length

        self.goals = []
        self.boxes = []
        self.walls=[]
        self.player_start = None
        # TODO: Parse grid to fill self.goals, self.boxes, self.player_start
        self._parse_grid()

        self.num_boxes = len(self.boxes)
        self.cnf = CNF()

    def _parse_grid(self):
        """Parse grid to find player, boxes, and goals."""  # x is vertical, y is horizintal
        # TODO: Implement parsing logic
        for x in range(self.N):
            for y in range(self.M):
                cell = self.grid[x][y]
                if cell == 'P':
                    self.player_start = ((x, y))
                elif cell == 'B':
                    self.boxes.append((x, y))
                elif cell == 'G':
                    self.goals.append((x, y))
                elif cell == '#':
                    self.walls.append((x,y))

    # ---------------- Variable Encoding ----------------
    def var_player(self, x, y, t):
        """
        Variable ID for player at (x, y) at time t.
        """
        # TODO: Implement encoding scheme
        return 1 + (t * self.N * self.M) + (x * self.M) + y

    def var_box(self, b, x, y, t):
        """
        Variable ID for box b at (x, y) at time t.
        """
        # TODO: Implement encoding scheme
        k = (self.T + 1) * self.N * self.M
        return k + 1 + (b * k) + (t * self.N * self.M) + (x * self.M) + y

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
        
        # 1. Initial conditions
        self.cnf.append([self.var_player(self.player_start[0], self.player_start[1], 0)])
        for b, (x, y) in enumerate(self.boxes):
            self.cnf.append([self.var_box(b, x, y, 0)])
        
        # 2. Player movement
        for t in range(self.T):
            for x in range(self.N):
                for y in range(self.M):
                    if self.grid[x][y] == '#': continue
                    v = self.var_player(x, y, t)
                    poss_moves = []
                    for d, (dx, dy) in DIRS.items():
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x < self.N and 0 <= new_y < self.M and self.grid[new_x][new_y] != '#':
                            poss_moves.append(self.var_player(new_x, new_y, t + 1))
                    if poss_moves: self.cnf.append([-v] + poss_moves)

        # # 3. Box movement (push rules)
        # for t in range(self.T +1):
        #     for b in range(len(self.boxes)):
        #         for x in range(self.N):
        #             for y in range(self.M):
        #                 if self.grid[x][y] == '#': continue
        #             X=[]
        #             # 1- Box stayed in same position
        #             X.append(self.var_box(b, x, y, t))
                    
        #             # 2- Box was pushed from each possible direction
        #             for (dx, dy) in DIRS.values():
        #                 player_x, player_y = x - dx, y - dy  # player initial pos
        #                 box_x, box_y = x + dx, y + dy  # box final pos
                        
        #                 # Check if this push scenario is physically possible
        #                 if (0 <= player_x < self.N and 0 <= player_y < self.M and 0 <= box_x < self.N and 0 <= box_y < self.M and
        #                     self.grid[player_x][player_y]!= "#" and self.grid[box_x][box_y] != "#"):
                            
                            
        #                     # If box moved due to this push, ensure push conditions
        #                     # (box at destination) ∧ (box was at source) → push conditions must hold
        #                     self.cnf.append([-self.var_box(b, box_x, box_y, t + 1), -self.var_box(b, x, y, t), self.var_player(player_x, player_y, t)])
        #                     self.cnf.append([-self.var_box(b, box_x, box_y, t + 1), -self.var_box(b, x, y, t), self.var_player(x, y, t + 1)])
                            
        #                     # Add this as a possible reason box is at (x,y)
        #                     X.append(self.var_box(b, x, y, t))
                    
        #             # Box at (box_x,box_y) at t+1 requires at least one valid reason
        #             if X:
        #                 temp = [-self.var_box(b, box_x, box_y, t + 1)] + X
        #                 self.cnf.append(temp)

        for b in range(len(self.boxes)):
            for t in range(self.T):
                for x in range(self.N):
                    for y in range(self.M):
                        if self.grid[x][y]=='#': continue
                    
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
            for x in range(self.N):
                for y in range(self.M):
                    if self.grid[x][y] == '#':
                        self.cnf.append([-self.var_player(x,y,t)])
                        for b in range(self.num_boxes):
                            self.cnf.append([-self.var_box(b,x,y,t)])
                    
                    a = [self.var_box(b, x, y, t) for b in range(self.num_boxes)]
                    for i in range(len(a)):
                        for j in range(i + 1, len(a)):
                            self.cnf.append([-a[i], -a[j]])
                    
                    for b in range(self.num_boxes):
                        self.cnf.append([-self.var_player(x, y, t), -self.var_box(b, x, y, t)])

        # 5. Goal conditions
        # Fixed: Each box must be on some goal
        for i in range(self.num_boxes):
            self.cnf.append([self.var_box(i,g[0],g[1],self.T) for g in self.goals])

        
        # 6. Other conditions (Object Uniqueness and Existence)
        for t in range(self.T + 1):
            # Player uniqueness and existence
            player_vars = []
            for x in range(self.N):
                for y in range(self.M):
                    if self.grid[x][y] != '#':
                        player_vars.append(self.var_player(x, y, t))

            for i in range(len(player_vars)):
                for j in range(i + 1, len(player_vars)):
                    self.cnf.append([-player_vars[i], -player_vars[j]])
            if player_vars: self.cnf.append(player_vars)

            # Box uniqueness and existence
            for b in range(self.num_boxes):
                box_vars = []
                for x in range(self.N):
                    for y in range(self.M):
                        if self.grid[x][y] != '#':
                            box_vars.append(self.var_box(b, x, y, t))
                for i in range(len(box_vars)):
                    for j in range(i + 1, len(box_vars)):
                        self.cnf.append([-box_vars[i], -box_vars[j]])
                if box_vars: self.cnf.append(box_vars)
        
        return self.cnf


def decode(model, encoder):
    """
    Decode SAT model into list of moves ('U', 'D', 'L', 'R').

    Args:
        model (list[int]): Satisfying assignment from SAT solver.
        encoder (SokobanEncoder): Encoder object with grid info.

    Returns:
        str: Sequence of moves.
    """
    N, M, T = encoder.N, encoder.M, encoder.T
    if not model: return -1

    # TODO: Map player positions at each timestep to movement directions
    model_set = set(model)
    player_pos = []
    for t in range(T + 1):
        found = False
        for x in range(N):
            for y in range(M):
                if encoder.grid[x][y] != '#':
                    if encoder.var_player(x, y, t) in model_set:
                        player_pos.append((x, y))
                        found = True
                        break
            if found: break
    
    moves = []
    DIRS_mapping = {(-1, 0): 'U', (1, 0): 'D', (0, -1): 'L', (0, 1): 'R'}

    for i in range(1, len(player_pos)):
        xi, yi = player_pos[i - 1]
        xf, yf = player_pos[i]
        dx = xf - xi
        dy = yf - yi
        if (dx, dy) in DIRS_mapping:
            moves.append(DIRS_mapping[(dx, dy)])
    
    return "".join(moves)


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
        solver.append_formula(cnf)
        if not solver.solve():
            return -1

        model = solver.get_model()
        if not model:
            return -1

        return decode(model, encoder)