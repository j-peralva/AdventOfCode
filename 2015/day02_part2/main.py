# noinspection DuplicatedCode
"""Jefferson Peralva Machiqueira"""

from model.WrappingPaper import WrappingPaper
from util.read_file import ReadFile


class Main:
    @classmethod
    def run(cls):
        data = ReadFile('data/day02.dat')
        print(WrappingPaper(data)[1])


if __name__ == '__main__':
    Main.run()
