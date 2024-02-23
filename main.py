import random
import time
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

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()

    def close(self):
        self.isRunning = False

    def draw_line(self, line, colour):
        line.draw(self.canvas, colour)

    def draw_cell(self, cell):
        cell.draw()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self._point1 = point1
        self._point2 = point2

    def draw(self, canvas, fill_colour):
        canvas.create_line(self._point1.x, self._point1.y, self._point2.x, self._point2.y, fill=fill_colour, width=2)


class Cell:
    def __init__(self, p1, p2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = p1.x
        self._x2 = p2.x
        self._y1 = p1.y
        self._y2 = p2.y
        self.cell_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        self._win = window
        self.visited = False

    def draw_move(self, to_cell, undo=False):
        if undo:
            self._win.draw_line(Line(self.cell_center, to_cell.cell_center), "grey")
        else:
            self._win.draw_line(Line(self.cell_center, to_cell.cell_center), "red")

    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black")
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black")


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self.seed = None
        if self.seed is not None:
            random.seed(self.seed)

    def _create_cells(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                firstpoint = Point(self.x1 + col*self.x1, self.y1 + row*self.y1)
                secondpoint = Point((self.x1*self.cell_size_x + col*self.x1), (self.y1 + row*self.y1) + self.cell_size_y*self.y1)
                #print(f"cell : {row} {col} |",firstpoint.x,firstpoint.y, secondpoint.x, secondpoint.y)
                self._cells.append(Cell(firstpoint, secondpoint, self.win))

        for c in range(len(self._cells)):
            print(c, len(self._cells))
            if c == 0:
                self._cells[c].has_left_wall = self._break_entrance_and_exit(self._cells[c].has_left_wall)
            if c == len(self._cells)-1:
                self._cells[c].has_right_wall = self._break_entrance_and_exit(self._cells[c].has_right_wall)
            self._draw_cell(self._cells[c])

    def _draw_cell(self, c):
        self.win.draw_cell(c)
        self._animate()

    def _animate(self):
        win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self, wall):
        wall = False

    def _break_walls_r(self):
        print("s")


#region graph
#def graph(columns, row):
#   for c in range(1, columns + 1):
#       for r in range(row):
#           top_list.append(Point(c * 50, 50 + (50 * r)))
#           bottom_list.append(Point((c * 50) + 50, 100 + (50 * r)))
#   return top_list, bottom_list
#endregion

win = MainWindow(1200, 720)

#region basic graph
#top_list = []
#bottom_list = []
#row = 10
#columns = 14
#cells = []
#top_left = Point(50,50)
#bottom_right = Point(100,100)
#
#top_list, bottom_list = graph(columns, row)
#for item in range(len(top_list)):
#    cells.append(Cell(top_list[item], bottom_list[item], win))
#for item in cells:
#    print(f"cell : {item._x1} {item._y1} {item._x2} {item._y2}")
#    win.draw_cell(item)
#endregion

# cells[0].draw_move(cells[1])
# cells[0].draw_move(cells[10], True)

maze = Maze(50, 50, 10, 14, 2, 2, win)

win.wait_for_close()
