from tkinter import Tk,BOTH,Canvas


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
    def __init__(self,x1,y1,x2,y2,win=None ,has_left_wall=True,has_right_wall=True,has_top_wall=True,has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall 
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.visited = False
    
    def draw(self):
        if self.has_left_wall:
            ll = Line(Point(self._x1, self._y1),Point(self._x1, self._y2))
            self._win.draw_line(ll,"black")
        else:
            ll = Line(Point(self._x1, self._y1),Point(self._x1, self._y2))
            self._win.draw_line(ll,"#d9d9d9")

        if self.has_right_wall:
            rl = Line(Point(self._x2, self._y1),Point(self._x2, self._y2))
            self._win.draw_line(rl,"black")
        else:
            rl = Line(Point(self._x2, self._y1),Point(self._x2, self._y2))
            self._win.draw_line(rl,"#d9d9d9")
        if self.has_top_wall:
            tl = Line(Point(self._x1, self._y1),Point(self._x2, self._y1))
            self._win.draw_line(tl,"black")
        else:
            tl = Line(Point(self._x1, self._y1),Point(self._x2, self._y1))
            self._win.draw_line(tl,"#d9d9d9")
        if self.has_bottom_wall:
            bl = Line(Point(self._x1, self._y2),Point(self._x2, self._y2))
            self._win.draw_line(bl,"black")
        else:
            bl = Line(Point(self._x1, self._y2),Point(self._x2, self._y2))
            self._win.draw_line(bl,"#d9d9d9")

    def draw_move(self,to_cell,undo=False):
        line_color = "gray"
        if not undo:
            line_color = "red"
        C1 = (.5 * (self._x2 + self._x1),.5 * (self._y2 + self._y1))
        C2 = (.5 * (to_cell._x2 + to_cell._x1),.5 * (to_cell._y2 + to_cell._y1))
        connect = Line(Point(*C1),Point(*C2))
        self._win.draw_line(connect,line_color)
