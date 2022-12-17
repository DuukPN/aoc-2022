import itertools
import time
from functools import cache

from lib import load_input
import re


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


class Node:
    def __init__(self, name, flow, adjacent):
        self.name = name
        self.flow = flow
        self.adjacent = adjacent

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def parse_graph(data):
    graph = {}
    for line in data:
        pattern = re.compile(r"""Valve (?P<name>.*?) has flow rate=(?P<flow>.*?); tunnels? leads? to valves? (?P<adjacent>.*?)$""")
        match = re.match(pattern, line)
        cur = Node(match.group("name"), int(match.group("flow")), match.group("adjacent").split(", "))
        graph[match.group("name")] = cur

    for node in graph.values():
        adjacent = {}
        for adj in node.adjacent:
            adjacent[graph[adj]] = 1
        node.adjacent = adjacent

    deleted = set()
    for node in graph.values():
        if node.flow == 0 and node.name != "AA":
            for adj1, adj2 in itertools.combinations(node.adjacent.keys(), 2):
                dist = node.adjacent[adj1] + node.adjacent[adj2]
                if adj2 not in adj1.adjacent or adj1.adjacent[adj2] > dist:
                    adj1.adjacent[adj2] = dist
                if adj1 not in adj2.adjacent or adj2.adjacent[adj1] > dist:
                    adj2.adjacent[adj1] = dist
                del adj1.adjacent[node]
                del adj2.adjacent[node]
                deleted.add(node)

    for node in deleted:
        del graph[node.name]

    return graph


def part_one(data):
    graph = parse_graph(data)

    @cache
    def max_flow(cur, opened, time_left):
        if time_left <= 1 or len(opened) + 1 == len(graph):
            return 0
        options = []
        if cur not in opened:
            options.append((time_left - 1) * cur.flow + max_flow(cur, opened | {cur}, time_left - 1))
        for adj in cur.adjacent:
            options.append(max_flow(adj, opened, time_left - cur.adjacent[adj]))
        return max(options)

    return max_flow(graph.get("AA"), frozenset(), 30)


def part_two(data):
    graph = parse_graph(data)

    @cache
    def max_flow(cur, opened, time_left):
        if time_left <= 1 or len(opened) + 1 == len(graph):
            return 0
        options = []
        if cur not in opened:
            options.append((time_left - 1) * cur.flow + max_flow(cur, opened | {cur}, time_left - 1))
        for adj in cur.adjacent:
            options.append(max_flow(adj, opened, time_left - cur.adjacent[adj]))
        return max(options)

    @cache
    def max_flow_2(cur, opened, time_left):
        if time_left <= 1 or len(opened) + 1 == len(graph):
            return 0
        options = []
        if cur not in opened:
            options.append((time_left - 1) * cur.flow + max_flow_2(cur, opened | {cur}, time_left - 1))
        for adj in cur.adjacent:
            options.append(max_flow_2(adj, opened, time_left - cur.adjacent[adj]))
        options.append(max_flow(graph.get("AA"), opened, 26))
        return max(options)

    return max_flow_2(graph.get("AA"), frozenset(), 26)


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
