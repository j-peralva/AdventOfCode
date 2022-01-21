# noinspection DuplicatedCode
"""Jefferson Peralva Machiqueira"""


class Floor:

    counter = 0
    first_time_basement = True

    def __init__(self):
        self.__floor = 0
        self.__position = None

    def move_up(self):
        self.__floor += 1
        self.counter += 1

    def move_down(self):
        self.__floor -= 1
        self.counter += 1
        if self.__floor < 0 and self.first_time_basement:
            self.__position = self.counter
            self.first_time_basement = False

    @property
    def floor(self) -> int:
        return self.__floor

    @property
    def position(self) -> int:
        return self.__position
