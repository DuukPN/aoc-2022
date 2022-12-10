from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    cycle = 0
    x = 1
    signals = 0
    for op in data:
        cycle += 1
        if cycle % 40 == 20:
            signals += cycle * x
        if op != "noop":
            cycle += 1
            if cycle % 40 == 20:
                signals += cycle * x
            x += int(op.split(" ")[1])

    return signals


def part_two(data):
    crt = ""
    x = 1
    cycle = 0
    for op in data:
        crt += "#" if abs(cycle % 40 - x) <= 1 else "."
        cycle += 1
        if op != "noop":
            crt += "#" if abs(cycle % 40 - x) <= 1 else "."
            cycle += 1
            x += int(op.split(" ")[1])

    res = ""
    for off in range(6):
        res += crt[off * 40:off * 40 + 40] + "\n"

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
