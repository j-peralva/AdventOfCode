# noinspection DuplicatedCode
"""Jefferson Peralva Machiqueira"""

from model.agent import Agent
from util.read_file import ReadFile


class Main:
    @classmethod
    def run(cls):
        data = list(ReadFile('data/day03.dat'))
        data = cls.__filter_data(data)
        santa_claus = Agent()
        for move in data[0]:
            if move == '^':
                santa_claus.move_north()
            elif move == 'v':
                santa_claus.move_south()
            elif move == '>':
                santa_claus.move_east()
            elif move == '<':
                santa_claus.move_west()
        robot = Agent()
        for move in data[1]:
            if move == '^':
                robot.move_north()
            elif move == 'v':
                robot.move_south()
            elif move == '>':
                robot.move_east()
            elif move == '<':
                robot.move_west()
        santa_claus.show_results()
        print()
        robot.show_results()

    @classmethod
    def __filter_data(cls, data: list) -> tuple[list, list]:
        data1 = []
        data2 = []
        for ind in range(len(data)):
            if ind % 2 == 0:
                data1.append(data[ind])
            else:
                data2.append(data[ind])
        return data1, data2


if __name__ == '__main__':
    Main.run()
