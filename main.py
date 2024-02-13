from tkinter import *
from tkinter import Tk, BOTH, Canvas

class MainWindow:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("MazeRunner")
        self.canvas = Canvas(self.__root, width=width, height=height, background="white")
        self.canvas.pack(anchor=CENTER, expand=True)
        self.isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def reDraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.reDraw()

    def close(self):
        self.isRunning = False

    def draw_line(self, line, colour):
        line.draw(self.canvas, colour)

    def draw_cell(self,cell, colour):
        cell.draw(self.canvas, colour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self._point1 = point1
        self._point2 = point2

    def draw(self, canvas, fill_colour):
        canvas.create_line(self._point1.x, self._point1.y, self._point2.x, self._point2.y, fill="red", width=2)

class Cell:
    def __init__(self, point1, point2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = point1.x
        self._x2 = point2.x
        self._y1 = point1.y
        self._y2 = point2.y

    def draw_move(self, to_cell, undo=False):
        print("df")


    def draw(self, canvas, fill_colour):
        if self.has_left_wall:
            canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill=fill_colour, width=2)
        if self.has_right_wall:
            canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill=fill_colour, width=2)
        if self.has_top_wall:
            canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill=fill_colour, width=2)
        if self.has_bottom_wall:
            canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill=fill_colour, width=2)

def graph(columns , row):
    for c in range(1, columns + 1):
        for r in range(row):
            top_list.append(Point(c * 50, 50 + (50 * r)))
            bottom_list.append(Point((c * 50) + 50, 100 + (50 * r)))
    return top_list, bottom_list

#build Points for objects
point1 = Point(50,  50)
point2 = Point(100,  100)

top_left = Point(50,50)
bottom_right = Point(100,100)

# Creating objects
line = Line(point1, point2)
cell = Cell(top_left,bottom_right)

win = MainWindow(800, 600)

# graphing
top_list = []
bottom_list = []
row = 10
columns = 14
cells = []

top_list, bottom_list = graph(columns, row)
for item in range(len(top_list)):
    cells.append(Cell(top_list[item], bottom_list[item]))


for item in cells:
    win.draw_cell(item, "black")

win.draw_cell(cell,"black")
win.draw_line(line, "red")

win.wait_for_close()






















