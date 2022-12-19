from collections import deque

from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    xs = set()
    ys = set()
    zs = set()
    total = 0
    for line in data:
        x, y, z = (int(c) for c in line.split(","))
        for nx, ny, nz in ((x, y, z), (x + 1, y, z)):
            total += -1 if (nx, ny, nz) in xs else 1
            xs.add((nx, ny, nz))
        for nx, ny, nz in ((x, y, z), (x, y + 1, z)):
            total += -1 if (nx, ny, nz) in ys else 1
            ys.add((nx, ny, nz))
        for nx, ny, nz in ((x, y, z), (x, y, z + 1)):
            total += -1 if (nx, ny, nz) in zs else 1
            zs.add((nx, ny, nz))

    return total


def part_two(data):
    grid = set()
    for line in data:
        x, y, z = (int(c) for c in line.split(","))
        grid.add((x, y, z))

    queue = deque()
    visited = {0, 0, 0}
    total = 0
    directions = {
        (0, 0, 1),
        (0, 0, -1),
        (0, 1, 0),
        (0, -1, 0),
        (1, 0, 0),
        (-1, 0, 0)
    }
    queue.append((0, 0, 0))
    while len(queue):
        x, y, z = queue.popleft()
        for dx, dy, dz in directions:
            nx, ny, nz = (x + dx, y + dy, z + dz)
            if -1 <= nx < 23 and -1 <= ny < 23 and -1 <= nz < 23:
                if not (nx, ny, nz) in grid:
                    if (nx, ny, nz) not in visited:
                        queue.append((nx, ny, nz))
                        visited.add((nx, ny, nz))
                else:
                    total += 1

    return total


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
