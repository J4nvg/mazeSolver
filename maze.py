from graphics import Window,Point,Line,Cell
import time
import random

class Maze():
    """Maze type"""
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None,seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)
            self.seed = seed
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            row_of_cells = []
            for j in range(self.num_cols):
                # Initialize with dummy coordinates (0,0,0,0) – 
                c = Cell(0, 0, 0, 0, self.win)
                row_of_cells.append(c)
            self._cells.append(row_of_cells)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self._cells[i][j].visited:
                    self._cells[i][j].visited = False

    def _draw_cell(self, i, j):
        left   = self.x1 + j * self.cell_size_x
        top    = self.y1 + i * self.cell_size_y
        right  = left + self.cell_size_x
        bottom = top + self.cell_size_y

        cell = self._cells[i][j]
        cell._x1 = left
        cell._y1 = top
        cell._x2 = right
        cell._y2 = bottom

        cell.draw()
        self._animate()
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while(True):
            nextcells = []
            if i+1 < self.num_rows and not self._cells[i+1][j].visited:
                nextcells.append((i+1,j))
            if j+1 < self.num_cols and not self._cells[i][j+1].visited:
                nextcells.append((i,j+1))
            if i-1 >= 0 and not self._cells[i-1][j].visited:
                nextcells.append((i-1,j))
            if j-1 >= 0 and not self._cells[i][j-1].visited:
                nextcells.append((i,j-1))
            if len(nextcells) == 0:
                self._draw_cell(i,j)
                return
            
            ni, nj = nextcells[random.randint(0,len(nextcells)-1)]
            
            if ni  == i+1:
                # Moving down: knock down BOTTOM of current, TOP of next
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False
            elif ni  == i-1:
                # Moving up: knock down TOP of current, BOTTOM of next
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False
            elif nj  == j+1:
                # Moving right: knock down RIGHT of current, LEFT of next
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False
            elif nj  == j-1:
                # Moving left: knock down LEFT of current, RIGHT of next
                self._cells[i][j].has_left_wall = False
            
            self._break_walls_r(ni, nj)


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)