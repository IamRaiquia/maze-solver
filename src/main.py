from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    m1.solve()

    m1._win.wait_for_close()

if __name__ == "__main__":
    print("Executing main.py")
    main()