from lib import load_input
import re
import itertools


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def parse_sensors(data):
    sensors = []
    distances = []
    beacons = set()
    for line in data:
        line = re.split("x=|, y=|: ", line)
        sensor = (int(line[1]), int(line[2]))
        beacon = (int(line[4]), int(line[5]))
        sensors.append(sensor)
        beacons.add(beacon)
        distances.append(manhattan_distance(sensor, beacon))

    return sensors, distances, beacons


def part_one(data):
    sensors, distances, beacons = parse_sensors(data)

    y = 2000000
    row = set()
    for i, sensor in enumerate(sensors):
        places = distances[i] - abs(sensor[1] - y)
        for j in range(places + 1):
            row.add((sensor[0] - j, y))
            row.add((sensor[0] + j, y))

    return len(row - beacons)


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part_two(data):
    sensors, distances, beacons = parse_sensors(data)

    for cur in itertools.combinations(sensors, 4):
        pp1 = set(s[0] + s[1] + distances[sensors.index(s)] + 1 for s in cur)
        pp2 = set(s[0] + s[1] - distances[sensors.index(s)] - 1 for s in cur)
        pm1 = set(s[0] - s[1] + distances[sensors.index(s)] + 1 for s in cur)
        pm2 = set(s[0] - s[1] - distances[sensors.index(s)] - 1 for s in cur)

        pos = pp1.intersection(pp2)
        neg = pm1.intersection(pm2)
        if len(pos) == len(neg) == 1:
            (pos,) = pos
            (neg,) = neg
            y = (pos - neg) // 2
            x = pos - y
            for i, sensor in enumerate(sensors):
                if manhattan_distance(sensor, (x, y)) < distances[i]:
                    break
            else:
                return x * 4000000 + y


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
