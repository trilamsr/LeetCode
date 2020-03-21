import json
import pprint
from collections import defaultdict

with open("Testcase.json") as test_file:
    data = json.load(test_file)
input = data['input']
printing = pprint.PrettyPrinter(indent=4).pprint


def get_destination(paths):
    ret = defaultdict(list)
    for origin, destination in paths:
        ret[origin].append(destination)
    return ret

def longest_path(origin, paths):
    memo = {}
    visited = set()
    destinations = get_destination(paths)
    dfs(memo, destinations, visited, origin)
    # printing(memo)
    return [origin] + max(memo[origin], key=len)

def dfs(memo, destinations, visited, start):
    visited.add(start)
    if start not in memo:
        memo[start] = []
        for dest in destinations[start]:
            if dest in visited: continue
            cur_path = dfs(memo, destinations, visited, dest)
            memo[start].append(cur_path)
    visited.remove(start)
    max_path = max(memo[start], key=len) if len(memo[start]) else []
    return [start] + max_path

output = longest_path('JFK', input)
printing(output)