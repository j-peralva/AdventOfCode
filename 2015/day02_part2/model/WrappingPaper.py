# noinspection DuplicatedCode
"""Jefferson Peralva Machiqueira"""

from typing import Generator, List, Tuple


class WrappingPaper:
    def __new__(cls, gen: Generator) -> Tuple[int, int]:
        aux = list(gen)
        return cls.__calculate_area(aux), cls.__feet_of_ribbon(aux)

    @classmethod
    def __calculate_area(cls, data: List[Tuple[int, int, int]]) -> int:
        area = 0
        for values in data:
            aux = (values[0] * values[1], values[0] * values[2], values[1] * values[2])
            area += 2 * (aux[0] + aux[1] + aux[2]) + min(aux)
        return area

    @classmethod
    def __feet_of_ribbon(cls, data: List[Tuple[int, int, int]]) -> int:
        acc = 0
        for values in data:
            aux1 = list(values)
            aux2 = aux1[0] * aux1[1] * aux1[2]
            aux1.remove(max(values))
            acc += 2 * sum(aux1) + aux2
        return acc
