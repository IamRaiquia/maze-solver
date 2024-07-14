from cell import Cell
from graphics import Window
import random
import time


class Maze():
    def __init__(
            self, 
            x1, 
            y1, 
            num_rows, 
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win=None,
            seed=None
        ):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        if win is None:
            w = (x1 * 4) + (cell_size_x * num_cols)
            h = (y1 * 4)+ (cell_size_y * num_rows)
            win = Window(w, h)
        self._win = win

        if seed:
            random.seed(seed)

        self._cells = []

        self._create_cells()
        self._break_entrance_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            cells = []
            for j in range(self._num_rows):
                cells.append(Cell(self._win))
            self._cells.append(cells)
    
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                
                self._draw_cell(i, j)
        

    def _draw_cell(self, i, j):

        x1 = self._x1 + (self._cell_size_x * i)
        y1 = self._y1 + (self._cell_size_y * j)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1,x2,y1,y2)
        
        #Change animate speed to low, medium, fast.
        self._animate("fast")


    def _animate(self, s="fast"):
        self._win.redraw()
        speed = 0.005
        if s == "low":
            speed = 0.05
        if s == "medium":
            speed = 0.01
        if s == "fast":
            speed = 0.005
        else:
            print(f"Invalid speed: {s}. Defaulting to fast")
        time.sleep(speed)

    def _break_entrance_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            
            not_visited = []

            if i > 0 and not self._cells[i - 1][j].visited:
                    not_visited.append((i-1, j))
            if i < len(self._cells) - 1 and not self._cells[i + 1][j].visited:
                    not_visited.append((i+1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                    not_visited.append((i, j-1))
            if j < len(self._cells[i]) - 1 and not self._cells[i][j + 1].visited:
                    not_visited.append((i, j+1))

            if len(not_visited) == 0:
                self._draw_cell(i, j)
                return
            
            choice = random.randrange(len(not_visited))
            choice_index = not_visited[choice - 1]

            if choice_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if choice_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if choice_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            if choice_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            
            self._break_walls_r(choice_index[0], choice_index[1])

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate("medium")

        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        if (i > 0 
            and not self._cells[i][j].has_left_wall 
            and not self._cells[i-1][j].visited
            ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            self._animate("fast")
            self._cells[i][j].draw_move(self._cells[i-1][j], True)

        if (i < len(self._cells) - 1 
            and not self._cells[i][j].has_right_wall 
            and not self._cells[i+1][j].visited
            ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            self._animate("medium")
            self._cells[i][j].draw_move(self._cells[i+1][j], True)

        if (j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j-1].visited
            ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            self._animate("medium")
            self._cells[i][j].draw_move(self._cells[i][j-1], True)

        if (j < len(self._cells[i]) - 1 
            and not self._cells[i][j].has_bottom_wall 
            and not self._cells[i][j+1].visited
            ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self._animate("medium")
            self._cells[i][j].draw_move(self._cells[i][j+1], True) 
        
        return False
                 
                