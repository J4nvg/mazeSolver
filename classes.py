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
            self._win.draw_line()
            pass