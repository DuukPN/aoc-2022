from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    theirs = []
    mine = []
    for line in data:
        them, me = line.split(" ")
        theirs.append(them)
        mine.append(me)

    points = {
        "A": {
            "X": 4,
            "Y": 8,
            "Z": 3,
        },
        "B": {
            "X": 1,
            "Y": 5,
            "Z": 9,
        },
        "C": {
            "X": 7,
            "Y": 2,
            "Z": 6,
        }
    }

    total = 0
    for i, me in enumerate(mine):
        total += points[theirs[i]][me]

    return total


def part_two(data):
    theirs = []
    mine = []
    for line in data:
        them, me = line.split(" ")
        theirs.append(them)
        mine.append(me)

    points = {
        "A": {
            "X": 3,
            "Y": 4,
            "Z": 8,
        },
        "B": {
            "X": 1,
            "Y": 5,
            "Z": 9,
        },
        "C": {
            "X": 2,
            "Y": 6,
            "Z": 7,
        }
    }

    total = 0
    for i, me in enumerate(mine):
        total += points[theirs[i]][me]

    return total


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
