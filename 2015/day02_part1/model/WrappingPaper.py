# noinspection DuplicatedCode
"""Jefferson Peralva Machiqueira"""

from typing import Generator


class WrappingPaper:
    def __new__(cls, gen: Generator) -> int:
        return cls.__calculate_area(gen)

    @classmethod
    def __calculate_area(cls, gen: Generator) -> int:
        area = 0
        for values in gen:
            aux = (values[0] * values[1], values[0] * values[2], values[1] * values[2])
            area += 2 * (aux[0] + aux[1] + aux[2]) + min(aux)
        return area
