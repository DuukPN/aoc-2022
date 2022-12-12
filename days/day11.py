from lib import load_input


def solve(data, part=2):
    lines = parse_monkeys(data.split('\n\n'))
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


class Monkey:
    def __init__(self, items, operation, divisibility, monkeys):
        self.items = items
        self.operation = operation
        self.divisibility = divisibility
        self.monkeys = monkeys
        self.inspect = 0

    def __repr__(self):
        return str(self.items)

    def __str__(self):
        return str(self.items)


def parse_monkeys(data):
    monkeys = []
    for monkey in data:
        monkey = monkey.splitlines()
        items = [int(x) for x in monkey[1].split(": ")[1].split(", ")]
        operation = monkey[2].split(" new = ")[1]
        divisible = int(monkey[3].split(" ")[-1])
        throw_to = (int(monkey[4].split(" ")[-1]), int(monkey[5].split(" ")[-1]))
        monkeys.append(Monkey(items, operation, divisible, throw_to))

    return monkeys


def part_one(data):
    for _ in range(20):
        for monkey in data:
            items = monkey.items
            monkey.items = []
            for item in items:
                monkey.inspect += 1
                item = eval(monkey.operation, {"old": item}) // 3
                data[monkey.monkeys[item % monkey.divisibility > 0]].items.append(item)

    activity = sorted(monkey.inspect for monkey in data)
    return activity[-1] * activity[-2]


def part_two(data):
    div = 1
    for monkey in data:
        div *= monkey.divisibility
    for _ in range(10000):
        for monkey in data:
            items = monkey.items
            monkey.items = []
            for item in items:
                monkey.inspect += 1
                item = eval(monkey.operation, {"old": item}) % div
                data[monkey.monkeys[item % monkey.divisibility > 0]].items.append(item)

    activity = sorted(monkey.inspect for monkey in data)
    return activity[-1] * activity[-2]


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
