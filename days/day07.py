from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


class Node:
    def __init__(self, name, parent, children, size, d):
        self.name = name
        self.parent = parent
        self.children = children
        self.size = size
        self.dir = d

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def add_child(self, name, size, d):
        if not self.get_child(name):
            self.children.append(Node(name, self, [], size, d))
        curr = self
        while curr is not None:
            curr.size += size
            curr = curr.parent


def build_tree(data):
    root = Node("/", None, [], 0, True)
    current = root
    for line in data:
        line = line.split(" ")
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    current = root
                elif line[2] == "..":
                    current = current.parent
                else:
                    current = current.get_child(line[2])
        else:
            size = 0
            if line[0] != "dir":
                size = int(line[0])
            current.add_child(line[1], size, not size)

    return root


def part_one(data):
    root = build_tree(data)

    return sum_1(root)


def sum_1(curr):
    s = 0
    if curr.dir and curr.size <= 100000:
        s += curr.size
    for child in curr.children:
        s += sum_1(child)
    return s


def part_two(data):
    root = build_tree(data)
    total_space = 70000000
    free = total_space - root.size
    to_free = 30000000 - free

    return find_smallest_larger_than(root, to_free)


def find_smallest_larger_than(curr, size):
    if not curr.dir:
        return 0
    sizes = [find_smallest_larger_than(child, size) for child in curr.children]
    sizes.append(curr.size)
    sizes = [s for s in sizes if s >= size]
    if not sizes:
        return 700000000
    return min(sizes)


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
