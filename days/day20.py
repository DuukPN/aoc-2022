from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


class Node:
    def __init__(self, n, prev, next):
        self.n = n
        self.prev = prev
        self.next = next

    def move(self, length):
        if self.n > 0:
            next = self.next
            next.prev = self.prev
            self.prev.next = next
            for _ in range(self.n % (length - 1)):
                next = next.next

            self.prev = next.prev
            self.prev.next = self
            self.next = next
            next.prev = self
        if self.n < 0:
            prev = self.prev
            prev.next = self.next
            self.next.prev = prev
            for _ in range((-self.n) % (length - 1)):
                prev = prev.prev

            self.next = prev.next
            self.next.prev = self
            self.prev = prev
            prev.next = self

    def result(self):
        cur = self
        total = 0
        for _ in range(3):
            for _ in range(1000):
                cur = cur.next
            total += cur.n

        return total

    def print(self):
        cur = self.next
        string = f"{str(self.n)} "
        while cur != self:
            string += str(cur.n) + " "
            cur = cur.next
        print(string)


def part_one(data):
    first = cur = None
    for n in data:
        cur = Node(int(n), cur, None)
        if not first:
            first = cur
        else:
            cur.prev.next = cur
    cur.next = first
    first.prev = cur

    zero = None
    done = set()
    cur = first
    while len(done) != len(data):
        if cur in done:
            cur = cur.next
            continue
        if not cur.n:
            zero = cur
        next = cur.next
        cur.move(len(data))
        done.add(cur)
        cur = next

    return zero.result()


def part_two(data):
    first = cur = None
    for n in data:
        cur = Node(int(n) * 811589153, cur, None)
        if not first:
            first = cur
        else:
            cur.prev.next = cur
    cur.next = first
    first.prev = cur

    zero = None
    order = []
    done = set()
    cur = first
    while len(done) != len(data):
        if cur in done:
            cur = cur.next
            continue
        order.append(cur)
        if not cur.n:
            zero = cur
        next = cur.next
        cur.move(len(data))
        done.add(cur)
        cur = next
    for _ in range(9):
        print(_)
        for node in order:
            node.move(len(data))

    return zero.result()


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
