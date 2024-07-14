from graphics import Window, Point, Line

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, x2, y1, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        left = Line(Point(x1, y1), Point(x1, y2))
        right = Line(Point(x2, y1), Point(x2, y2))
        top = Line(Point(x1, y1), Point(x2, y1))
        bottom = Line(Point(x1, y2), Point(x2, y2))   
        
        line_color = "black"
        no_walls = "white"

        if self.has_left_wall:
            self._win.draw_line(left, fill_color=line_color)
        else:
            self._win.draw_line(left, fill_color=no_walls)

        if self.has_right_wall:
            self._win.draw_line(right, fill_color=line_color)
        else:
            self._win.draw_line(right, fill_color=no_walls)
            
        if self.has_top_wall:
            self._win.draw_line(top, fill_color=line_color)
        else:
            self._win.draw_line(top, fill_color=no_walls)

        if self.has_bottom_wall:
            self._win.draw_line(bottom, fill_color=line_color)
        else:
            self._win.draw_line(bottom, fill_color=no_walls)

    def draw_move(self, to_cell, undo=False):
        line_color = "gray"
        if not undo:
            line_color = "red"
        
        x1 = (self._x2-self._x1)/2 + self._x1
        y1 = (self._y2-self._y1)/2 + self._y1
        x2 = (to_cell._x2-to_cell._x1)/2 + to_cell._x1
        y2 = (to_cell._y2-to_cell._y1)/2 + to_cell._y1

        self._win.draw_line(
            Line(Point(x1, y1), Point(x2, y2)), 
            fill_color=line_color
        )