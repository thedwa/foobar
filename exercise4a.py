from __future__ import division
from collections import OrderedDict


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def infinite_loop(x, y):
    total = x + y
    if total % 2 == 1:
        return True
    ratio = total / gcd(x, y)
    return bin(int(ratio)).count('1') != 1


def get_matches(banana_list):
    graph = OrderedDict()
    length = len(banana_list)
    for i in range(length):
        for j in range(i + 1, length):
            if infinite_loop(banana_list[i], banana_list[j]):
                if i not in graph:
                    graph[i] = []
                if j not in graph:
                    graph[j] = []
                graph[i].append(j)
                graph[j].append(i)
    return graph


def bfs(graph, match, dist):
    queue = [u for u in graph if match[u] == None]
    for u in queue:
        dist[u] = 0
    dist[None] = float('inf')
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            next_u = match[v]
            if dist[next_u] == float('inf'):
                dist[next_u] = dist[u] + 1
                if next_u is not None:
                    queue.append(next_u)
    return dist[None] != float('inf')


def dfs(graph, match, dist, u):
    if u == None:
        return True
    for v in graph[u]:
        next_u = match[v]
        if dist[next_u] == dist[u] + 1 and dfs(graph, match, dist, next_u):
            match[u] = v
            match[v] = u
            return True
    dist[u] = float('inf')
    return False


def hopcroft_karp(graph):
    match = OrderedDict((v, None) for v in graph)
    dist = OrderedDict((v, None) for v in graph)
    matching = 0
    while bfs(graph, match, dist):
        for u in graph:
            if match[u] == None and dfs(graph, match, dist, u):
                matching += 1
    return matching


def solution(banana_list):
    graph = get_matches(banana_list)
    matching = hopcroft_karp(graph)
    return len(banana_list) - 2 * matching


print(solution([1, 7, 3, 21, 13, 19]))  # Expected output: 0
print(solution([1, 7, 3, 21, 13, 19]))  # Expected output: 0
print('starting now')
print(solution([1, 7, 3, 21, 13, 19])) # Expected output: 0
print(solution([1, 7, 3, 13, 19, 21])) # Expected output: 0
print(solution([1, 7, 21, 3, 13, 19])) # Expected output: 0
print(solution([1, 7, 21, 13, 3, 19])) # Expected output: 0
print(solution([1, 7, 13, 3, 19, 21])) # Expected output: 0
print(solution([1, 7, 13, 19, 3, 21])) # Expected output: 0
print(solution([1, 7, 19, 3, 13, 21])) # Expected output: 0
print(solution([1, 7, 19, 13, 3, 21])) # Expected output: 0
print(solution([1, 7, 3, 21, 19, 13])) # Expected output: 0
print(solution([1, 7, 3, 13, 21, 19])) # Expected output: 0
print(solution([1, 7, 21, 3, 19, 13])) # Expected output: 0
print(solution([1, 7, 21, 13, 19, 3])) # Expected output: 0
print(solution([1, 7, 13, 3, 21, 19])) # Expected output: 0
print(solution([1, 7, 13, 19, 21, 3])) # Expected output: 0
print(solution([1, 7, 19, 3, 21, 13])) # Expected output: 0
print(solution([1, 7, 19, 13, 21, 3])) # Expected output: 0
print(solution([1, 3, 7, 21, 13, 19])) # Expected output: 0
print(solution([1, 3, 7, 13, 19, 21])) # Expected output: 0
print(solution([1, 3, 21, 7, 13, 19])) # Expected output: 0
print(solution([1, 3, 21, 13, 7, 19])) # Expected output: 0
print(solution([1, 3, 13, 7, 19, 21])) # Expected output: 0
print(solution([1, 3, 13, 19, 7, 21])) # Expected output: 0
print(solution([1, 3, 19, 7, 13, 21])) # Expected output: 0
print(solution([1, 3, 19, 13, 7, 21])) # Expected output: 0
print(solution([1, 3, 7, 21, 19, 13])) # Expected output: 0
print(solution([1, 3, 7, 13, 21, 19])) # Expected output: 0
print(solution([1, 3, 21, 7, 19, 13])) # Expected output: 0
print(solution([1, 3, 21, 13, 19, 7])) # Expected output: 0
print(solution([1, 3, 13, 7, 21, 19])) # Expected output: 0
print(solution([1, 3, 13, 19, 21, 7])) # Expected output: 0
print(solution([1, 3, 19, 7, 21, 13])) # Expected output: 0
print(solution([1, 3, 19, 13, 21, 7])) # Expected output: 0
print(solution([1, 21, 7, 3, 13, 19])) # Expected output: 0
print(solution([1, 21, 7, 13, 3, 19])) # Expected output: 0
print(solution([1, 21, 3, 7, 13, 19])) # Expected output: 0
print(solution([1, 21, 3, 13, 7, 19])) # Expected output: 0
print(solution([1, 21, 13, 3, 19, 7])) # Expected output: 0
print(solution([1, 21, 13, 19, 3, 7])) # Expected output: 0
print(solution([1, 21, 19, 3, 13, 7])) # Expected output: 0
print(solution([1, 21, 19, 13, 3, 7])) # Expected output: 0
print(solution([1, 21, 7, 3, 19, 13])) # Expected output: 0
print(solution([1, 21, 7, 13, 19, 3])) # Expected output: 0
print(solution([1, 21, 3, 7, 19, 13])) # Expected output: 0
print(solution([1, 21, 3, 13, 19, 7])) # Expected output: 0
print(solution([1, 21, 13, 3, 7, 19])) # Expected output: 0
print(solution([1, 21, 13, 19, 7, 3])) # Expected output: 0
print(solution([1, 21, 19, 3, 7, 13])) # Expected output: 0
print(solution([1, 21, 19, 13, 7, 3])) # Expected output: 0
print(solution([1, 13, 7, 3, 19, 21])) # Expected output: 0
print(solution([1, 13, 7, 21, 3, 19])) # Expected output: 0
print(solution([1, 13, 3, 7, 19, 21])) # Expected output: 0
print(solution([1, 13, 3, 21, 19, 7])) # Expected output: 0
print(solution([1, 13, 21, 3, 7, 19])) # Expected output: 0
print(solution([1, 13, 21, 19, 7, 3])) # Expected output: 0
print(solution([1, 13, 19, 3, 7, 21])) # Expected output: 0
print(solution([1, 13, 19, 21, 7, 3])) # Expected output: 0
print(solution([1, 19, 7, 3, 13, 21])) # Expected output: 0
print(solution([1, 19, 7, 21, 3, 13])) # Expected output: 0
print(solution([1, 19, 3, 7, 13, 21])) # Expected output: 0
print(solution([1, 19, 3, 21, 13, 7])) # Expected output: 0
print(solution([1, 19, 21, 3, 7, 13])) # Expected output: 0
print(solution([7, 1, 3, 21, 13, 19])) # Expected output: 0
print(solution([7, 1, 3, 13, 19, 21])) # Expected output: 0
print(solution([7, 1, 21, 3, 13, 19])) # Expected output: 0
print(solution([7, 1, 21, 13, 19, 3])) # Expected output: 0
print(solution([7, 1, 13, 3, 19, 21])) # Expected output: 0
print(solution([7, 1, 13, 19, 3, 21])) # Expected output: 0
print(solution([7, 1, 19, 3, 13, 21])) # Expected output: 0
print(solution([7, 1, 19, 13, 3, 21])) # Expected output: 0
print(solution([7, 3, 1, 21, 13, 19])) # Expected output: 0
print(solution([7, 3, 1, 13, 19, 21])) # Expected output: 0
print(solution([7, 3, 21, 1, 13, 19])) # Expected output: 0
print(solution([7, 3, 21, 13, 19, 1])) # Expected output: 0
print(solution([7, 3, 13, 1, 19, 21])) # Expected output: 0
print(solution([7, 3, 13, 19, 1, 21])) # Expected output: 0
print(solution([7, 3, 19, 1, 13, 21])) # Expected output: 0
print(solution([7, 3, 19, 13, 1, 21])) # Expected output: 0
print(solution([7, 21, 1, 3, 13, 19])) # Expected output: 0
print(solution([7, 21, 1, 13, 3, 19])) # Expected output: 0
print(solution([7, 21, 3, 1, 13, 19])) # Expected output: 0
print(solution([7, 21, 3, 13, 1, 19])) # Expected output: 0
print(solution([7, 21, 13, 1, 3, 19])) # Expected output: 0
print(solution([7, 21, 13, 19, 1, 3])) # Expected output: 0
print(solution([7, 21, 19, 1, 3, 13])) # Expected output: 0
print(solution([7, 21, 19, 13, 1, 3])) # Expected output: 0
print(solution([7, 13, 1, 3, 19, 21])) # Expected output: 0
print(solution([7, 13, 1, 21, 3, 19])) # Expected output: 0
print(solution([7, 13, 3, 1, 19, 21])) # Expected output: 0
print(solution([7, 13, 3, 21, 19, 1])) # Expected output: 0
print(solution([7, 13, 21, 1, 3, 19])) # Expected output: 0
print(solution([7, 13, 21, 19, 1, 3])) # Expected output: 0
print(solution([7, 13, 19, 1, 3, 21])) # Expected output: 0
print(solution([7, 13, 19, 3, 1, 21])) # Expected output: 0
print(solution([7, 19, 1, 3, 13, 21])) # Expected output: 0
print(solution([7, 19, 1, 21, 3, 13])) # Expected output: 0
print(solution([7, 19, 3, 1, 13, 21])) # Expected output: 0
print(solution([7, 19, 3, 21, 13, 1])) # Expected output: 0
print(solution([7, 19, 21, 1, 3, 13])) # Expected output: 0
print(solution([7, 19, 21, 13, 1, 3])) # Expected output: 0
print(solution([7, 19, 13, 1, 3, 21])) # Expected output: 0
print(solution([7, 19, 13, 3, 1, 21])) # Expected output: 0
print('over now')
print(solution([1, 1]))  # Expected output: 2
print(solution([2,10]))
print(solution([1,4])) # Expected output: 0
print(solution([3,5])) # Expected output: 2
print(solution([1])) # Expected output: 1
print(solution([1073741823, 1073741823, 1073741823, 1073741823])) # Expected output: 4
print(solution([5, 5, 5, 5, 5])) # Expected output: 5
print(solution([1]*100)) # Expected output: 100
print(solution([1073741823, 1]))
print(solution([1]))

print(solution([46,987]))