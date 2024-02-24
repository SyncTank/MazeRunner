from WindowUI import MainWindow
from Maze import Maze


# region graph
# def graph(columns, row):
#   for c in range(1, columns + 1):
#       for r in range(row):
#           top_list.append(Point(c * 50, 50 + (50 * r)))
#           bottom_list.append(Point((c * 50) + 50, 100 + (50 * r)))
#   return top_list, bottom_list
# endregion

# region basic graph
# top_list = []
# bottom_list = []
# row = 10
# columns = 14
# cells = []
# top_left = Point(50,50)
# bottom_right = Point(100,100)
#
# top_list, bottom_list = graph(columns, row)
# for item in range(len(top_list)):
#    cells.append(Cell(top_list[item], bottom_list[item], win))
# for item in cells:
#    print(f"cell : {item._x1} {item._y1} {item._x2} {item._y2}")
#    win.draw_cell(item)
# endregion

# cells[0].draw_move(cells[1])
# cells[0].draw_move(cells[10], True)

def main():
    win = MainWindow(1200, 720)
    maze = Maze(5, 5, 10, 14, 10, 10, win, 5)
    win.wait_for_close()


main()
