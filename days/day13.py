from lib import load_input
from functools import cmp_to_key


def solve(data, part=2):
    lines = data
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    data = data.strip().split("\n\n")
    data = [tuple(eval(l) for l in line.split("\n")) for line in data]
    total = 0
    for i, ls in enumerate(data):
        if compare(ls[0], ls[1]) > 0:
            total += i + 1

    return total


def compare(left, right):
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    for i in range(min([len(left), len(right)])):
        if left[i] != right[i]:
            if isinstance(left[i], int) and isinstance(right[i], int):
                c = right[i] - left[i]
            else:
                c = compare(left[i], right[i])
            if c:
                return c
    return len(right) - len(left)


def part_two(data):
    data = [eval(l) for l in data.splitlines() if l]
    data.append([[2]])
    data.append([[6]])
    data = sorted(data, key=cmp_to_key(compare), reverse=True)
    return (data.index([[2]]) + 1) * (data.index([[6]]) + 1)


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
