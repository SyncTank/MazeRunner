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
        self.values = (p1.x, p1.y, p2.x, p2.y)
        self.cell_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        self._win = window
        self.visited = False

    def draw_move(self, to_cell, undo=False) -> None:
        if undo:
            self._win.draw_line(Line(self.cell_center, to_cell.cell_center), "grey")
        else:
            self._win.draw_line(Line(self.cell_center, to_cell.cell_center), "red")

    def draw(self, colour="black") -> None:
        color_or_white = colour if self.has_left_wall else "white"
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), color_or_white)

        color_or_white = colour if self.has_right_wall else "white"
        self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), color_or_white)

        color_or_white = colour if self.has_top_wall else "white"
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), color_or_white)

        color_or_white = colour if self.has_bottom_wall else "white"
        self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), color_or_white)


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
        self._break_entrance_and_exit()
        self._break_walls_r(random.randrange(0, self.num_cols), random.randrange(0, self.num_rows))

    def _create_cells(self):
        for I in range(self.num_cols):
            col = []
            for J in range(self.num_rows):
                point1 = Point((self.x1 + self.x1 * I) * self.cell_size_x,
                               (self.y1 + self.y1 * J) * self.cell_size_y)

                point2 = Point((self.x1 + self.x1 + self.x1 * I) * self.cell_size_x,
                               (self.y1 + self.y1 + self.y1 * J) * self.cell_size_y)
                col.append(Cell(point1, point2, self.win))
                self._draw_cell(col[J])
            self._cells.append(col)

    def _draw_cell(self, c) -> None:
        c.draw()
        self._animate()

    def _animate(self) -> None:
        self.win.redraw()
        # time.sleep(0.02)

    def _break_entrance_and_exit(self) -> None:
        col_length = len(self._cells)
        row_length = len(self._cells[0])
        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0])
        self._cells[col_length - 1][row_length - 1].has_bottom_wall = False
        self._draw_cell(self._cells[col_length - 1][row_length - 1])

    def _break_walls_r(self, I: int, J: int) -> None:
        self._cells[I][J].visited = True
        while True:
            to_visit = []
            if self._cells[I + 1][J] and self._cells[I + 1][J].visited is not True:
                to_visit.append((I + 1, J))
            if self._cells[I - 1][J] and self._cells[I - 1][J].visited is not True:
                to_visit.append((I - 1, J))
            if self._cells[I][J + 1] and self._cells[I][J + 1].visited is not True:
                to_visit.append((I, J + 1))
            if self._cells[I][J - 1] and self._cells[I][J - 1].visited is not True:
                to_visit.append((I, J - 1))

            print(I, J)
            for item in to_visit:
                print(item)

            possible_move = []
            if self._cells[I][J]:
                print(self._cells[I][J].values, self._cells[I][J].visited)

            break
