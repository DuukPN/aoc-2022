from lib import load_input


def solve(data, part=2):
    start, steps = [p.splitlines() for p in data.split("\n\n")]
    if part == 1:
        return part_one(start, steps)
    elif part == 2:
        return part_two(start, steps)


def part_one(start, steps):
    no_columns = int(start[-1].strip().split(" ")[-1])
    cols = [[] for i in range(no_columns)]
    for line in start[:-1]:
        for i in range(no_columns):
            if i * 4 + 1 < len(line):
                crate = line[i * 4 + 1]
                if crate != " ":
                    cols[i].append(crate)

    for col in cols:
        col.reverse()

    for step in steps:
        split = step.split(" ")
        no, src, dest = int(split[1]), int(split[3]), int(split[5])
        for _ in range(no):
            cols[dest - 1].append(cols[src - 1].pop())

    msg = ""
    for col in cols:
        msg += col.pop()

    return msg


def part_two(start, steps):
    no_columns = int(start[-1].strip().split(" ")[-1])
    cols = [[] for i in range(no_columns)]
    for line in start[:-1]:
        for i in range(no_columns):
            if i * 4 + 1 < len(line):
                crate = line[i * 4 + 1]
                if crate != " ":
                    cols[i].append(crate)

    for col in cols:
        col.reverse()

    for step in steps:
        split = step.split(" ")
        no, src, dest = int(split[1]), int(split[3]), int(split[5])
        temp = cols[src - 1][-no:]
        cols[src - 1] = cols[src - 1][:-no]
        for t in temp:
            cols[dest - 1].append(t)

    msg = ""
    for col in cols:
        msg += col.pop()

    return msg


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
