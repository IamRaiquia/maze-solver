from maze import Maze
import sys

def main():
    
 
    sys.setrecursionlimit(10**6)
    num_cols = 80
    num_rows = 50
    m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
    m1.solve()

    m1._win.wait_for_close()

if __name__ == "__main__":
    print("Executing main.py")
    main()