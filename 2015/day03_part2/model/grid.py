# noinspection DuplicatedCode
"""Jefferson Peralva Machiqueira"""


class Grid:

    # This class atribute is used for adjustment in grid offset.
    # This is a horrible solution, maybe one day I will review this
    offset_adjustment = [0, 0]

    def __init__(self):
        self.__grid = [[0]]         # Every grid starts with only one position
        self.__objects = []         # Every grid has a list of objects that lives on it

    def append(self, obj: object):
        self.__objects.append(obj)
        self.__add_to_zero_position()

    def __add_to_zero_position(self):
        self.__grid[self.offset_adjustment[0]][self.offset_adjustment[1]] += 1

    def __out_of_grid(self, lin: int, col: int) -> bool:
        line_condition = lin < 0 or lin > len(self.__grid) - 1
        column_condition = col < 0 or col > len(self.__grid[0]) - 1
        if line_condition or column_condition:
            return True
        else:
            return False

    def recalculate_grid(self, lin: int, col: int) -> tuple[int, int]:
        if self.__out_of_grid(lin, col):
            if lin < 0:
                self.offset_adjustment[0] += 1
                return self.__insert_new_line(0, col)
            elif lin >= len(self.__grid):
                return self.__insert_new_line(len(self.__grid), col)
            elif col < 0:
                self.offset_adjustment[1] += 1
                return self.__insert_new_column(lin, 0)
            elif col >= len(self.__grid[0]):
                return self.__insert_new_column(lin, len(self.__grid[0]))
        else:
            self.__grid[lin][col] += 1
            return lin, col

    def __insert_new_line(self, lin: int, col: int):
        new_line = [0] * len(self.__grid[0])
        new_line[col] = 1
        self.__grid.insert(lin, new_line)
        return lin, col

    def __insert_new_column(self, lin: int, col: int):
        new_column = [0] * len(self.__grid)
        new_column[lin] = 1
        if col <= 0:
            for line_index in range(len(self.__grid)):
                self.__grid[line_index].insert(0, new_column.pop(0))
        elif col >= len(self.__grid[0]):
            for line_index in range(len(self.__grid)):
                self.__grid[line_index].append(new_column.pop(0))
        return lin, col

    def total_number_of_gifts(self) -> int:
        accumulator = 0
        for line in self.__grid:
            accumulator += sum(line)
        return accumulator

    def grid_dimensions(self) -> str:
        return f"{len(self.__grid)} lines, {len(self.__grid[0])} columns"

    def __len__(self) -> int:
        return len(self.__grid) * len(self.__grid[0])

    def at_least_one_gift(self) -> int:
        return sum([len([value for value in self.__grid[index] if value != 0]) for index in range(len(self.__grid))])
