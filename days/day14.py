from lib import load_input


def solve(data, part=2):
    lines = parse_rocks(data.splitlines())
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def parse_rocks(data):
    rocks = set()
    for line in data:
        coords = [tuple(int(x) for x in line.split(",")) for line in line.split(" -> ")]
        prev = coords[0]
        for coord in coords[1:]:
            if coord[1] == prev[1]:
                for i in range(min(coord[0], prev[0]), max(coord[0], prev[0]) + 1):
                    rocks.add((i, coord[1]))
            if coord[0] == prev[0]:
                for i in range(min(coord[1], prev[1]), max(coord[1], prev[1]) + 1):
                    rocks.add((coord[0], i))
            prev = coord

    return rocks


def part_one(data):
    total = 0
    max_y = max(map(lambda x: x[1], data))
    while True:
        sand = (500, 0)
        while True:
            if sand[1] > max_y:
                return total
            if (sand[0], sand[1] + 1) not in data:
                sand = (sand[0], sand[1] + 1)
            elif (sand[0] - 1, sand[1] + 1) not in data:
                sand = (sand[0] - 1, sand[1] + 1)
            elif (sand[0] + 1, sand[1] + 1) not in data:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                total += 1
                data.add(sand)
                sand = (500, 0)


def part_two(data):
    total = 0
    floor = max(map(lambda x: x[1], data)) + 2
    while True:
        sand = (500, 0)
        while True:
            on_floor = sand[1] == floor - 1
            if (sand[0], sand[1] + 1) not in data and not on_floor:
                sand = (sand[0], sand[1] + 1)
            elif (sand[0] - 1, sand[1] + 1) not in data and not on_floor:
                sand = (sand[0] - 1, sand[1] + 1)
            elif (sand[0] + 1, sand[1] + 1) not in data and not on_floor:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                total += 1
                if sand == (500, 0):
                    return total
                data.add(sand)
                sand = (500, 0)


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
