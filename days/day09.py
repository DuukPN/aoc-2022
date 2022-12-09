from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    head_x, head_y = (0, 0)
    tail_x, tail_y = (0, 0)
    visited = set()
    visited.add((tail_x, tail_y))
    directions = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1)
    }

    for move in data:
        direction, n = move.split(" ")
        for _ in range(int(n)):
            dx, dy = directions[direction]
            head_x += dx
            head_y += dy
            if not dy:
                if abs(head_x - tail_x) > 1:
                    tail_x += (head_x - tail_x) // 2
                    if head_y != tail_y:
                        tail_y = head_y
            if not dx:
                if abs(head_y - tail_y) > 1:
                    tail_y += (head_y - tail_y) // 2
                    if head_x != tail_x:
                        tail_x = head_x

            visited.add((tail_x, tail_y))

    return len(visited)


def part_two(data):
    coord = [(0, 0) for _ in range(10)]
    visited = set()
    visited.add(coord[-1])
    directions = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1)
    }

    for move in data:
        direction, n = move.split(" ")
        for _ in range(int(n)):
            dx, dy = directions[direction]
            coord[0] = (coord[0][0] + dx, coord[0][1] + dy)
            for i in range(9):
                head_x, head_y = coord[i]
                tail_x, tail_y = coord[i+1]

                if abs(head_x - tail_x) > 1:
                    tail_x += (head_x - tail_x) // 2
                    if head_y != tail_y:
                        tail_y = head_y

                if abs(head_y - tail_y) > 1:
                    tail_y += (head_y - tail_y) // 2
                    if head_x != tail_x:
                        tail_x = head_x

                coord[i+1] = (tail_x, tail_y)

            # draw_grid(coord)
            visited.add(coord[-1])

    return len(visited)


def draw_grid(coord):
    grid = [["." for i in range(10)] for i in range(10)]
    for i, c in reversed(list(enumerate(coord))):
        x, y = c
        grid[x][y] = str(i)

    for line in grid:
        s = ""
        for c in line:
            s += c
        print(s)
    print()


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
