from WindowUI import Point, Line
import random
import time


class Cell:
    def __init__(self, p1, p2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.directions = {
            (0, 1): self.has_top_wall,
            (0, -1): self.has_bottom_wall,
            (1, 0): self.has_right_wall,
            (-1, 0): self.has_left_wall
        }
        self._x1: int = p1.x
        self._x2: int = p2.x
        self._y1: int = p1.y
        self._y2: int = p2.y
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
        self.x1: int = x1
        self.y1: int = y1
        self.num_rows: int = num_rows
        self.num_cols: int = num_cols
        self.cell_size_x: int = cell_size_x
        self.cell_size_y: int = cell_size_y
        self.win = window
        self._cells: list = []
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.seed: int = seed  # if not defined it uses system's time
        if self.seed is not None:
            random.seed(self.seed)
        self._create_cells()
        self._break_entrance_and_exit()
        print(self.num_rows, self.num_cols)
        self._break_walls_r(random.randrange(0, self.num_cols), random.randrange(0, self.num_rows))
        self._reset_cells_visited()

    def _create_cells(self):
        for col_Value in range(self.num_cols):
            col = []
            for row_Value in range(self.num_rows):
                point1 = Point((self.x1 + self.x1 * col_Value) * self.cell_size_x,
                               (self.y1 + self.y1 * row_Value) * self.cell_size_y)

                point2 = Point((self.x1 + self.x1 + self.x1 * col_Value) * self.cell_size_x,
                               (self.y1 + self.y1 + self.y1 * row_Value) * self.cell_size_y)
                col.append(Cell(point1, point2, self.win))
                self._draw_cell(col[row_Value])
            self._cells.append(col)

    def _draw_cell(self, c: Cell) -> None:
        c.draw()
        self._animate()

    def _animate(self) -> None:
        self.win.redraw()
        #time.sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        col_length = len(self._cells)
        row_length = len(self._cells[0])
        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0])
        self._cells[col_length - 1][row_length - 1].has_bottom_wall = False
        self._draw_cell(self._cells[col_length - 1][row_length - 1])

    def break_walls(self, col_Value: int, row_Value: int, TO_Col: int, TO_row: int) -> None:
        movement = (col_Value - TO_Col, row_Value - TO_row)
        # print(f"movement: {movement}, {col_Value}, {TO_Col}, {row_Value}, {TO_row}")
        match movement:
            case (-1, 0):
                self._cells[col_Value][row_Value].has_right_wall = False
                self._cells[TO_Col][TO_row].has_left_wall = False
                self._cells[col_Value][row_Value].directions[(-1, 0)] = False
                self._cells[TO_Col][TO_row].directions[(1, 0)] = False
                # print("right")
                return
            case (1, 0):
                self._cells[col_Value][row_Value].has_left_wall = False
                self._cells[TO_Col][TO_row].has_right_wall = False
                self._cells[col_Value][row_Value].directions[(1, 0)] = False
                self._cells[TO_Col][TO_row].directions[(-1, 0)] = False
                # print("left")
                return
            case (0, 1):
                self._cells[col_Value][row_Value].has_top_wall = False
                self._cells[TO_Col][TO_row].has_bottom_wall = False
                self._cells[col_Value][row_Value].directions[(0, 1)] = False
                self._cells[TO_Col][TO_row].directions[(0, -1)] = False
                # print("up")
                return
            case (0, -1):
                self._cells[col_Value][row_Value].has_bottom_wall = False
                self._cells[TO_Col][TO_row].has_top_wall = False
                self._cells[col_Value][row_Value].directions[(0, -1)] = False
                self._cells[TO_Col][TO_row].directions[(0, 1)] = False
                # print("down")
                return
            case _:
                print("Something went wrong")
                return

    def _break_walls_r(self, col_Value: int, row_Value: int) -> None:
        self._cells[col_Value][row_Value].visited = True
        while True:
            vist_list = []

            if row_Value + 1 < self.num_rows:
                if not self._cells[col_Value][row_Value + 1].visited:
                    vist_list.append((col_Value, row_Value + 1))
            if row_Value - 1 >= 0:
                if not self._cells[col_Value][row_Value - 1].visited:
                    vist_list.append((col_Value, row_Value - 1))
            if col_Value + 1 < self.num_cols:
                if not self._cells[col_Value + 1][row_Value].visited:
                    vist_list.append((col_Value + 1, row_Value))
            if col_Value - 1 >= 0:
                if not self._cells[col_Value - 1][row_Value].visited:
                    vist_list.append((col_Value - 1, row_Value))

            if len(vist_list) == 0:
                self._draw_cell(self._cells[col_Value][row_Value])
                return
            else:
                direction_to_move = random.randrange(0, len(vist_list))
                moving = vist_list[direction_to_move - 1]

            self.break_walls(col_Value, row_Value, moving[0], moving[1])

            self._break_walls_r(moving[0], moving[1])

    def _reset_cells_visited(self) -> None:
        for col in range(0, self.num_cols):
            for row in range(0, self.num_rows):
                self._cells[col][row].visited = False

    def solve(self) -> bool:
        return self._solve_dfs_r(0, 0)

    def _solve_dfs_r(self, start_X: int, start_Y: int) -> bool:
        self._animate()
        self._cells[start_X][start_Y].visited = True
        if self._cells[start_X][start_Y] == self._cells[self.num_cols - 1][self.num_rows - 1]:
            return True

        for dir in self.directions:
            new_cell_dir_x = start_X + (-dir[0])
            new_cell_dir_y = start_Y + (-dir[1])
            within_cells_x = self.num_cols > new_cell_dir_x >= 0
            within_cells_y = self.num_rows > new_cell_dir_y >= 0
            if within_cells_x and within_cells_y and self._cells[new_cell_dir_x][new_cell_dir_y].visited is False and self._cells[start_X][start_Y].directions[dir] is False:
                self._cells[start_X][start_Y].draw_move(self._cells[new_cell_dir_x][new_cell_dir_y])
                dfs = self._solve_dfs_r(new_cell_dir_x, new_cell_dir_y)
                if dfs:
                    return True
                else:
                    self._cells[start_X][start_Y].draw_move(self._cells[new_cell_dir_x][new_cell_dir_y], True)

        return False



















