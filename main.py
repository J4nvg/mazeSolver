from classes import *


def main():
    win = Window(800,600)
    l1 = Line(Point(0,10),Point(100,0))
    l2 = Line(Point(0,20),Point(20,0))
    l3 = Line(Point(10,20),Point(20,10))
    win.draw_line(l1,"black")
    win.draw_line(l2,"red")
    win.draw_line(l3,"green")
    win.wait_for_close()

if __name__ == '__main__':
    main()
