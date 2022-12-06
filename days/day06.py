from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()[0]
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    for i in range(len(data) - 4):
        if len(set(data[i:i + 4])) == 4:
            return i + 4


def part_two(data):
    for i in range(len(data) - 14):
        if len(set(data[i:i + 14])) == 14:
            return i + 14


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
