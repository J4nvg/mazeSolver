from graphics import Window, Point, Line, Cell
from maze import Maze

win = Window(1200, 1200)  
nmazes = 10

def main():
    num_rows = 20
    num_cols = 20
    cell_width = 50
    cell_height = 50

    for i in range(nmazes):
       
        m1 = Maze(10, 10, num_rows, num_cols, cell_width, cell_height, win=win)
        m1.solve_dfs()
        win.clear()  # Clears the canvas between each new maze

    win.wait_for_close()

main()
