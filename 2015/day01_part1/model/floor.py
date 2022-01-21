# noinspection DuplicatedCode
"""Jefferson Peralva Machiqueira"""


class Floor:
    def __init__(self):
        self.__floor = 0

    def move_up(self):
        self.__floor += 1

    def move_down(self):
        self.__floor -= 1

    @property
    def floor(self) -> int:
        return self.__floor
