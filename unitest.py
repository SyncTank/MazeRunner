from Maze import Maze
import unittest
from WindowUI import MainWindow
from Maze import Maze


class Tests(unittest.TestCase):
    def setUp(self):
        self.window = MainWindow(None, None)
        self.num_cols = 14
        self.num_rows = 10
        self.m1 = m1 = Maze(5, 5, self.num_rows, self.num_cols, 10, 10, self.window, 200)

    def test_maze_create_cells(self):
        self.assertEqual(
            len(self.m1._cells),
            self.num_cols,
        )
        self.assertEqual(
            len(self.m1._cells[0]),
            self.num_rows,
        )

    def test_all_cells_not_visited(self):
        for col in range(0, self.num_cols):
            for row in range(0, self.num_rows):
                self.assertFalse(self.m1._cells[col][row].visited)

        if __name__ == "__main__":
            unittest.main()
