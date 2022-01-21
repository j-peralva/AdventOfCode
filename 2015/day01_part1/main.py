# noinspection DuplicatedCode
"""Jefferson Peralva Machiqueira"""

from model.floor import Floor
from util.read_file import ReadFile


class Main:
    @classmethod
    def run(cls):
        data = list(ReadFile('data/day01.dat'))
        floor = Floor()
        for direction in data:
            if direction == ')':
                floor.move_down()
            elif direction == '(':
                floor.move_up()
        print(f'Final floor is: {floor.floor}')


if __name__ == '__main__':
    Main.run()
