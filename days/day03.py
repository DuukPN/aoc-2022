from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    s = 0
    for line in data:
        line = [char for char in line]
        half = len(line) // 2
        first = line[:half]
        second = line[half:]
        intersect = set(first).intersection(set(second))
        for k in intersect:
            if k.isupper():
                s += ord(k) - 38
            else:
                s += ord(k) - 96

    return s


def part_two(data):
    s = 0
    for i in range(0, len(data), 3):
        first = set([char for char in data[i]])
        second = set([char for char in data[i + 1]])
        third = set([char for char in data[i + 2]])
        intersect = set(first).intersection(set(second)).intersection(set(third))
        for k in intersect:
            if k.isupper():
                s += ord(k) - 38
            else:
                s += ord(k) - 96

    return s


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
