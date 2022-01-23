# noinspection DuplicatedCode
"""Jefferson Peralva Machiqueira"""

try:
    from model.grid import Grid
except ImportError:
    from grid import Grid


class Agent:

    __grid = Grid()                         # Every Agent shares the same Grid

    def __init__(self):
        coordinates = self.__grid.offset_adjustment[0], self.__grid.offset_adjustment[1]
        self.__cur_position = coordinates   # Every new agent starts at (0, 0) position of Grid
        self.__grid.append(self)

    def move_north(self):
        line = self.__cur_position[0] - 1
        column = self.__cur_position[1]
        self.__cur_position = self.__grid.recalculate_grid(line, column)

    def move_south(self):
        line = self.__cur_position[0] + 1
        column = self.__cur_position[1]
        self.__cur_position = self.__grid.recalculate_grid(line, column)

    def move_east(self):
        line = self.__cur_position[0]
        column = self.__cur_position[1] + 1
        self.__cur_position = self.__grid.recalculate_grid(line, column)

    def move_west(self):
        line = self.__cur_position[0]
        column = self.__cur_position[1] - 1
        self.__cur_position = self.__grid.recalculate_grid(line, column)

    def show_results(self):
        print(f"Grid dimensions is: {self.__grid.grid_dimensions()}")
        print(f"Number of cells of grid is: {len(self.__grid)}")
        print(f"Total gifts delivered: {self.__grid.total_number_of_gifts()}")
        print(f"Houses with at least one gift: {self.__grid.at_least_one_gift()}")


if __name__ == '__main__':
    Agent()
