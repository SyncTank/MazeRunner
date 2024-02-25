from tkinter import *
from tkinter import Tk, BOTH, Canvas


class MainWindow:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("MazeRunner")
        self._canvas = Canvas(self.__root, width=width, height=height, background="white")
        self._canvas.pack(anchor=CENTER, expand=True)
        self.isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.isRunning = True
        while self.isRunning:
            self.redraw()

    def close(self) -> None:
        self.isRunning = False

    def draw_line(self, line, colour="black") -> None:
        line.draw(self._canvas, colour)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2) -> None:
        self._point1 = point1
        self._point2 = point2

    def draw(self, canvas, fill_colour) -> None:
        canvas.create_line(self._point1.x, self._point1.y, self._point2.x, self._point2.y, fill=fill_colour, width=2)
        canvas.pack(fill=BOTH, expand=1)
