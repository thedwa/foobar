def solution(banana_list):
    n = len(banana_list)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if will_loop(banana_list[i], banana_list[j]):
                graph[i].append(j)
                graph[j].append(i)

    match = [-1] * n
    result = 0
    for node in range(n):
        if match[node] == -1:
            visited = [0] * n
            if not augment_path(node, visited, match, graph):
                result += 1

    return result


def will_loop(x, y):
    total = x + y
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return total / x % 2 != 0


def augment_path(node, visited, match, graph):
    for neighbor in graph[node]:
        if visited[neighbor]:
            continue
        visited[neighbor] = 1
        if match[neighbor] == -1 or augment_path(match[neighbor], visited, match, graph):
            match[node] = neighbor
            return 1
    return 0



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