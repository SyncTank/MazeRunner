from WindowUI import Point, Line
import random
import time

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
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = window
        self._cells = []
        self.seed = seed  # if not defined it uses system's time
        if self.seed is not None:
            random.seed(self.seed)
        self._create_cells()

    def _create_cells(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                firstpoint = Point(self.x1 + col * self.x1, self.y1 + row * self.y1)

                secondpoint = Point((self.x1 * self.cell_size_x + col * self.x1),
                                    (self.y1 + row * self.y1) + self.cell_size_y * self.y1)

                self._cells.append(Cell(firstpoint, secondpoint, self.win))

        self._break_entrance_and_exit()
        self._break_walls_r()

        for c in self._cells:
            self._draw_cell(c)

    def _draw_cell(self, c):
        self.win.draw_cell(c)
        self._animate()

    def _animate(self):
        self.win.redraw()
        # time.sleep(0.02)

    def _break_entrance_and_exit(self):
        cells_len = len(self._cells)
        self._cells[0].has_left_wall = False
        self._cells[0].has_right_wall = False
        self._cells[0].has_bottom_wall = False
        self._cells[cells_len - 1].has_right_wall = False
        self._cells[cells_len - 1].has_top_wall = False
        self._cells[cells_len - 1].has_left_wall = False

    def _break_walls_r(self):
        self._cells[0].visited = True
        for cell in self._cells:
            print(cell.visited)