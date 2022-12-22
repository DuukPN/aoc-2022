from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    monkeys = {}
    for line in data:
        name, value = line.split(": ")
        try:
            value = int(value)
        except ValueError:
            pass
        monkeys[name] = value

    return yell("root", monkeys)


def yell(monkey, monkeys):
    value = monkeys[monkey]
    if isinstance(value, int):
        return value

    n1, op, n2 = value.split(" ")
    if op == "/":
        op += "/"

    return eval(f"{n1} {op} {n2}", {n1: yell(n1, monkeys), n2: yell(n2, monkeys)})


def part_two(data):
    monkeys = {}
    for line in data:
        name, value = line.split(": ")
        try:
            value = int(value)
        except ValueError:
            pass
        monkeys[name] = value

    n1, _, n2 = monkeys["root"].split(" ")
    n1, n2 = special_yell(n1, monkeys), special_yell(n2, monkeys)
    if isinstance(n1, list):
        ops, n = n1, n2
    else:
        ops, n = n2, n1

    while len(ops) > 0:
        op = ops.pop()
        n = eval(op, {"x": n})

    return n


def special_yell(monkey, monkeys):
    if monkey == "humn":
        return []
    value = monkeys[monkey]
    if isinstance(value, int):
        return value

    n1, op, n2 = value.split(" ")
    n1, n2 = special_yell(n1, monkeys), special_yell(n2, monkeys)
    if isinstance(n1, list):
        ops = n1
        if op == "-":
            ops.append(f"x + {n2}")
        if op == "/":
            ops.append(f"x * {n2}")
        n = n2
    elif isinstance(n2, list):
        ops = n2
        if op == "-":
            ops.append(f"-x + {n1}")
        if op == "/":
            ops.append(f"{n1} // x")
        n = n1
    else:
        return eval(f"{n1} {'//' if op == '/' else op} {n2}")

    if op == "+":
        ops.append(f"x - {n}")
    if op == "*":
        ops.append(f"x // {n}")

    return ops


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
