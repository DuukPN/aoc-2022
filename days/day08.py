from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def parse_grid(data):
    lines = []
    for line in data:
        curr = [int(x) for x in line]
        lines.append(curr)
    return lines


def part_one(data):
    grid = parse_grid(data)
    visible = 0
    for i, line in enumerate(grid):
        if i == 0 or i + 1 == len(grid):
            visible += len(line)
            continue

        for j, n in enumerate(line):
            if j == 0 or j + 1 == len(line):
                visible += 1
                continue

            for k in range(j + 1, len(line)):
                if grid[i][k] >= n:
                    break
            else:
                visible += 1
                continue

            for k in range(j - 1, -1, -1):
                if grid[i][k] >= n:
                    break
            else:
                visible += 1
                continue

            for k in range(i + 1, len(grid)):
                if grid[k][j] >= n:
                    break
            else:
                visible += 1
                continue

            for k in range(i - 1, -1, -1):
                if grid[k][j] >= n:
                    break
            else:
                visible += 1
                continue

    return visible


def part_two(data):
    grid = parse_grid(data)
    max_scenic = 0
    for i, line in enumerate(grid):
        for j, n in enumerate(line):
            scenic_score = 1
            visible = 0
            for k in range(j + 1, len(line)):
                visible += 1
                if grid[i][k] >= n:
                    break
            scenic_score *= visible

            visible = 0
            for k in range(j - 1, -1, -1):
                visible += 1
                if grid[i][k] >= n:
                    break
            scenic_score *= visible

            visible = 0
            for k in range(i + 1, len(grid)):
                visible += 1
                if grid[k][j] >= n:
                    break
            scenic_score *= visible

            visible = 0
            for k in range(i - 1, -1, -1):
                visible += 1
                if grid[k][j] >= n:
                    break
            scenic_score *= visible

            if scenic_score > max_scenic:
                max_scenic = scenic_score

    return max_scenic


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
