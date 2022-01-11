"""Jefferson Peralva Machiqueira"""

from pathlib import Path


class ReadFile:
    def __new__(cls, relative_path_from_main_to_data_file: str):
        path = Path.cwd().joinpath(relative_path_from_main_to_data_file)
        with open(path, 'r') as file:
            content = file.readline()
            for movement in content:
                yield movement
