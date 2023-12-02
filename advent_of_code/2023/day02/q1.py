from advent_of_code.utils.io import readstrings
from dataclasses import dataclass


d_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
d_num = [str(i) for i in range(1, 10)]


def solve2(file):
    score = 0
    for line in readstrings(file):
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for dn, ds in zip(d_num, d_str):
                if line[i:].startswith(ds):
                    digits.append(dn)
        print(digits)
        score += int(digits[0] + digits[-1])
    return score


if __name__ == "__main__":
    # res = solve("/workspaces/advent_of_code/advent_of_code/2023/day01/1.in")
    # assert res == 142

    res = solve2("/workspaces/advent_of_code/advent_of_code/2023/day01/2.in")
    print(res)
    assert res == 281

    res = solve2("/workspaces/advent_of_code/advent_of_code/2023/day01/input.in")
    print(res)

    # solve()
