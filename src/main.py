from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c2 = Cell(win)
    c3 = Cell(win)
    c4 = Cell(win)

    c1.has_bottom_wall = False
    c1.draw(100, 200, 200, 100)
    
    c2.has_top_wall = False
    c2.has_right_wall = False
    c2.draw(100, 200, 300, 200)

    c3.has_left_wall = False
    c3.has_bottom_wall = False
    c3.draw(200, 300, 300, 200)

    c4.has_top_wall = False
    c4.draw(200, 300, 400, 300)

    c1.draw_move(c2)
    c2.draw_move(c3)
    c3.draw_move(c4)

    win.wait_for_close()


if __name__ == "__main__":
    print("Executing main.py")
    main()