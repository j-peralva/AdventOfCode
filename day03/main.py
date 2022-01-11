"""Jefferson Peralva Machiqueira"""

from model.grid import SantaClausGrid
from util.read_file import ReadFile


class Main:
    @classmethod
    def run(cls):
        data = list(ReadFile('data/day03.dat'))
        grid = SantaClausGrid()
        for move in data:
            if move == '^':
                grid.move_north()
            elif move == 'v':
                grid.move_south()
            elif move == '>':
                grid.move_east()
            elif move == '<':
                grid.move_west()
        print(f"Grid dimensions is: {grid.grid_dimensions()}")
        print(f"Number of cells of grid is: {len(grid)}")
        print(f"Total gifts delivered: {grid.total_number_of_gifts()}")
        print(f"Houses with at least one gift: {grid.at_least_one_gift()}")


if __name__ == '__main__':
    Main.run()
