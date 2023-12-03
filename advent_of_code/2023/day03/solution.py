from __future__ import annotations
from advent_of_code.utils.io import readstrings, get_example
from dataclasses import dataclass
from typing import List
import numpy as np


@dataclass
class Cubeset:
    red: int = 0
    green: int = 0
    blue: int = 0

    @staticmethod
    def from_line(line: str) -> List[Cubeset]:
        game_sets = line[line.find(":") + 1 :].split(";")
        return [Cubeset.from_set(s) for s in game_sets]

    @staticmethod
    def from_set(cube_set: str) -> Cubeset:
        cubes = [s.strip() for s in cube_set.split(",")]
        d = {}
        for c in cubes:
            print(c)
            num, col = c.split(" ")
            d[col] = int(num)
        return Cubeset(**d)

    def possible(self, bag: Cubeset) -> bool:
        return self.red <= bag.red and self.green <= bag.green and self.blue <= bag.blue

    def as_vec(self):
        return np.array([self.red, self.green, self.blue])


elf_bag = Cubeset(12, 13, 14)


def solve1(file):
    result = 0
    for i, line in enumerate(readstrings(file)):
        games = Cubeset.from_line(line)
        possible = True
        for g in games:
            if not g.possible(elf_bag):
                possible = False
                break
        if possible:
            result += i + 1
    return result


def solve2(file):
    result = 0
    for line in readstrings(file):
        games = Cubeset.from_line(line)
        games_mat = np.vstack([g.as_vec() for g in games])
        min_vals = np.max(games_mat, 0)
        powers = min_vals[0] * min_vals[1] * min_vals[2]
        result += powers
        print(games_mat)
        print(min_vals)
        print(powers)
    return result


if __name__ == "__main__":
    res = solve1(get_example(1, __file__))
    print(res)
    assert res == 4361

    # res = solve1(get_example("input", __file__))
    # print(res)
    # assert res == 2727

    # res = solve2(get_example(2, __file__))
    # print(res)
    # assert res == 2286

    # res = solve2(get_example("input", __file__))
    # print(res)
    # assert res == 56580
