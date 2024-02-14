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

    def draw_cell(self, cell, colour):
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
        self._win = window

    def draw_move(self, to_cell, undo=False):
        self_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        new_center = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        if undo:
            self._win.draw_line(Line(self_center, new_center), "grey")
        else:
            self._win.draw_line(Line(self_center, new_center), "red")

    def draw(self, canvas, fill_colour):
        if self.has_left_wall:
            canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill=fill_colour, width=2)
        if self.has_right_wall:
            canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill=fill_colour, width=2)
        if self.has_top_wall:
            canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill=fill_colour, width=2)
        if self.has_bottom_wall:
            canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill=fill_colour, width=2)


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = window
        self._cells = []
        self._create_cells()

        def _create_cells(self):
            print(self)

        def _draw_cell(self, I, J):
            print(self)

        def _animate(self):
            print(self)


def graph(columns, row):
    for c in range(1, columns + 1):
        for r in range(row):
            top_list.append(Point(c * 50, 50 + (50 * r)))
            bottom_list.append(Point((c * 50) + 50, 100 + (50 * r)))
    return top_list, bottom_list


# region static builds Points for objects
# point1 = Point(75, 75)
# point2 = Point(125, 75)
# line = Line(point1, point2)

# top_left = Point(50,50)
# bottom_right = Point(100,100)
# cell = Cell(top_left,bottom_right)

# endregion

win = MainWindow(800, 600)

# region defining variables for graph
top_list = []
bottom_list = []
row = 10
columns = 14
cells = []
# endregion

# region Generate the cells for the graph, & draw the cells

top_list, bottom_list = graph(columns, row)
for item in range(len(top_list)):
    cells.append(Cell(top_list[item], bottom_list[item], win))

for item in cells:
    win.draw_cell(item, "black")

# endregion

cells[0].draw_move(cells[1])
cells[0].draw_move(cells[10], True)

# win.draw_line(line, "red")

win.wait_for_close()
