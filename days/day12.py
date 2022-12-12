from lib import load_input
from collections import deque
from queue import PriorityQueue


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def make_graph(data, all_starts=False):
    edges = {}
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    start = []
    end = 0
    for i, line in enumerate(data):
        edges[i] = {}
        for j, c in enumerate(line):
            edges[i][j] = []
            if c == "S":
                if not all_starts:
                    start = (i, j)
                c = "a"
            if c == "E":
                end = (i, j)
                c = "z"
            if all_starts and c == "a":
                start.append((i, j))
            c = ord(c)
            for dx, dy in dirs:
                if 0 <= i + dx < len(data) and 0 <= j + dy < len(line):
                    if ord(data[i + dx][j + dy].replace("S", "a").replace("E", "z")) - c <= 1:
                        edges[i][j].append((i + dx, j + dy))

    return edges, start, end


def part_one(data):
    graph, start, end = make_graph(data)
    queue = deque()
    queue.append((*start, 0))
    visited = {start}
    while len(queue) > 0:
        i, j, steps = queue.popleft()
        if (i, j) == end:
            return steps
        for neigh in graph[i][j]:
            if neigh not in visited:
                queue.append((*neigh, steps + 1))
                visited.add(neigh)


def part_two(data):
    graph, start, end = make_graph(data, True)
    queue = PriorityQueue()
    for s in start:
        queue.put((0, *s))
    visited = set()
    while not queue.empty():
        steps, i, j = queue.get()
        if (i, j) == end:
            return steps
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for neigh in graph[i][j]:
            queue.put((steps + 1, *neigh))


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
