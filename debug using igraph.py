from collections import OrderedDict
import networkx as nx

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

def get_graph(banana_list):
    graph = nx.Graph()
    length = len(banana_list)
    for i in range(length):
        for j in range(i + 1, length):
            if infinite_loop(banana_list[i], banana_list[j]):
                graph.add_edge(i, j, weight = 1)
    return graph

def solution(banana_list):
    graph = get_graph(banana_list)
    matching = nx.max_weight_matching(graph, maxcardinality=True)
    return len(banana_list) - 2 * len(matching)


print(solution([1, 7, 3, 21, 13, 19]))  # Expected output: 0
print(solution([1, 7, 3, 21, 13, 19]))  # Expected output: 0
print('starting now')
print(solution([1, 7, 3, 21, 13, 19])) # Expected output: 0
print(solution([1, 7, 3, 13, 19, 21])) # Expected output: 0
print(solution([1, 7, 21, 3, 13, 19])) # Expected output: 0
print(solution([1, 7, 21, 13, 3, 19])) # Expected output: 0
print(solution([1, 7, 13, 3, 19, 21])) # Expected output: 0
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