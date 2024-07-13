from cell import Cell
from graphics import Window
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
        ):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        if win is None:
            w = (self._x1 * 4) + (cell_size_x * num_cols)
            h = (self._y1 * 4)+ (cell_size_y * num_rows)
            win = Window(w, h)
        self._win = win

        self._cells = []

        self._create_cells()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            cells = []
            for j in range(self._num_rows):
                cells.append(Cell(self._win))
            self._cells.append(cells)
    
        for column in self._cells:
            for cell in column:
                self._draw_cell(column, cell)
        

    def _draw_cell(self, i, j):
        x1 = self._x1 + (self._cell_size_x * self._cells.index(i))
        y1 = self._y1 + (self._cell_size_y * i.index(j))
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        j.draw(x1,x2,y1,y2)

        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

        






        



