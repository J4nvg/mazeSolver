import unittest
from graphics import Window,Cell,Line,Point
from maze import Maze

win = Window(800, 600)            
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(20, 20, num_rows, num_cols, 20, 20, win=win)
    # def test_maze_create_cells_more(self):
    #     num_cols = 120
    #     num_rows = 2
    #     m1 = Maze(0, 0, num_rows, num_cols, 5, 5, win=win)

    # def testmazetwo(self):
    #     num_cols = 5
    #     num_rows = 5
    #     m3 = Maze(0, 0, num_rows, num_cols, 40, 40, win=win)
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 40, 40, win=win)
    #     self.assertNotEqual(m1,m3,"Not equal")

if __name__ == "__main__":
    unittest.main()