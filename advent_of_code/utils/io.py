import pathlib


def readstrings(path: str):
    with open(path, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def get_example(example_number: int, file_in_folder: str):
    return pathlib.Path(file_in_folder).parent / f"{example_number}.in"
