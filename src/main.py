from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    p1 = Point(100, 200)
    p2 = Point(200, 500)
    line = Line(p1, p2)
    win.draw_line(line, "blue")
    win.wait_for_close()


if __name__ == "__main__":
    print("Executing main.py")
    main()