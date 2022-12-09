from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    head_x, head_y, tail_x, tail_y = [0 for _ in range(4)]
    visited = set()
    directions = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1)
    }

    for m in data:
        direction, n = m.split(" ")
        for _ in range(int(n)):
            dx, dy = directions[direction]
            head_x += dx
            head_y += dy
            tail_x, tail_y = move(head_x, head_y, tail_x, tail_y)
            visited.add((tail_x, tail_y))

    return len(visited)


def part_two(data):
    knots = [(0, 0) for _ in range(10)]
    visited = set()
    directions = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1)
    }

    for m in data:
        direction, n = m.split(" ")
        for _ in range(int(n)):
            dx, dy = directions[direction]
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
            for i in range(9):
                knots[i + 1] = move(*knots[i], *knots[i + 1])

            visited.add(knots[-1])
        draw_grid(knots)

    return len(visited)


def move(head_x, head_y, tail_x, tail_y):
    if abs(head_x - tail_x) > 1:
        tail_x += (head_x - tail_x) // 2
        tail_y += sign(head_y - tail_y)

    if abs(head_y - tail_y) > 1:
        tail_y += (head_y - tail_y) // 2
        tail_x += sign(head_x - tail_x)

    return tail_x, tail_y


def sign(n):
    return (n > 0) - (n < 0)


def draw_grid(coord):
    low = -11
    high = 16
    grid = [["." for _ in range(low, high)] for _ in range(low, high)]
    for i, c in reversed(list(enumerate(coord))):
        x, y = c
        grid[y - low][x - low] = str(i)

    for line in reversed(grid):
        s = ""
        for c in line:
            s += c
        print(s)
    print()


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input("medium")))
