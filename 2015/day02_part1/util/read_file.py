# noinspection DuplicatedCode
"""Jefferson Peralva Machiqueira"""

from pathlib import Path
from typing import Generator


class ReadFile:
    def __new__(cls, relative_path_from_main_to_data_file: str) -> Generator:
        path = Path.cwd().joinpath(relative_path_from_main_to_data_file)
        with open(path, 'r') as file:
            for line in file:
                yield tuple(map(int, line.split('x')))
