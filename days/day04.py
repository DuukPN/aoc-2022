from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    total = 0
    for line in data:
        pairs = line.split(",")
        bounds = [pair.split("-") for pair in pairs]
        bounds = [int(nr) for bound in bounds for nr in bound]
        one1, one2, two1, two2 = bounds

        if (one1 >= two1 and one2 <= two2) or (one1 <= two1 and one2 >= two2):
            total += 1

    return total


def part_two(data):
    total = 0
    for line in data:
        pairs = line.split(",")
        bounds = [pair.split("-") for pair in pairs]
        bounds = [int(nr) for bound in bounds for nr in bound]
        one1, one2, two1, two2 = bounds

        if one1 <= two2 and two1 <= one2:
            total += 1

    return total


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
