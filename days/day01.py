from lib import load_input


def solve(data, part=2):
    lines = data.strip().split("\n\n")
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    totals = [sum([int(n) for n in line.split("\n")]) for line in data]
    return max(totals)


def part_two(data):
    totals = [sum([int(n) for n in line.split("\n")]) for line in data]
    return sum(sorted(totals, reverse=True)[:3])


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
