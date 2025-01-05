from tkinter import Tk,BOTH,Canvas
import time

class Window():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = ("Window")
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def close(self):
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def wait_for_close(self):
        i = 0
        while(i<100000):
            self.redraw()
            i+=1
        self.close()

    def draw_line(self,Line,fill_color):
        Line.draw(self.canvas,fill_color)

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line():
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self,canvas,fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color,width=2
        )
        

class Cell():
    def __init__(self,x1,y1,x2,y2,win ,has_left_wall=True,has_right_wall=True,has_top_wall=True,has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall 
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
    
    def draw(self):
        if self.has_left_wall:
            ll = Line(Point(self._x1, self._y1),Point(self._x1, self._y2))
            self._win.draw_line(ll,"black")
        if self.has_right_wall:
            rl = Line(Point(self._x2, self._y1),Point(self._x2, self._y2))
            self._win.draw_line(rl,"black")
        if self.has_top_wall:
            tl = Line(Point(self._x1, self._y1),Point(self._x2, self._y1))
            self._win.draw_line(tl,"black")
        if self.has_bottom_wall:
            tl = Line(Point(self._x1, self._y2),Point(self._x2, self._y2))
            self._win.draw_line(tl,"black")

    def draw_move(self,to_cell,undo=False):
        line_color = "gray"
        if not undo:
            line_color = "red"
        C1 = (.5 * (self._x2 + self._x1),.5 * (self._y2 + self._y1))
        C2 = (.5 * (to_cell._x2 + to_cell._x1),.5 * (to_cell._y2 + to_cell._y1))
        connect = Line(Point(*C1),Point(*C2))
        self._win.draw_line(connect,line_color)


class Maze():
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
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
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)