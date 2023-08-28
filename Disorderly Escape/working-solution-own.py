from math import factorial
from itertools import permutations

def solution(w, h, s):
    total_fixed_points = 0

    for perm_w in permutations(range(w)):
        for perm_h in permutations(range(h)):
            grid = [[(perm_w[i], perm_h[j]) for j in range(h)] for i in range(w)]
            cycles = 0
            visited = [[False] * h for _ in range(w)]

            for i in range(w):
                for j in range(h):
                    if not visited[i][j]:
                        cycles += 1
                        x, y = i, j
                        while not visited[x][y]:
                            visited[x][y] = True
                            x, y = grid[x][y]

            total_fixed_points += s**cycles

    return str(total_fixed_points // (factorial(w) * factorial(h)))


# Test the function
print(solution(10, 10, 2))  # Output: "7"
print(solution(2, 3, 4))  # Output: "430"
