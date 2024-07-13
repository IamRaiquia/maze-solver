import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 20
        num_rows = 20
        m1 = Maze(50, 50, num_rows, num_cols, 30, 30)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )


if __name__ == "__main__":
    unittest.main()