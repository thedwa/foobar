def solution(l):
    g = generate_graph(l)
    matches = reduce(g)
    return len(l) - matches

def loop(x,y):
    base = int((x+y)/gcd(x,y))
    return bool(base & (base - 1))

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def generate_graph(l):
    G = {i: [] for i in range(len(l))}
    for i in range(len(l)):
        for j in range(i, len(l)):
            if i != j and loop(l[i], l[j]):
                G[i].append(j)
                G[j].append(i)
    return G

def reduce(g):
    matched = 0
    checks = len(g[max(g, key=lambda key: len(g[key]))])
    while len(g) > 1 and checks >= 1:
        init_mw_node = min(g, key=lambda key: len(g[key]))
        if (len(g[init_mw_node])) < 1 :
            del g[init_mw_node]
        else:
            temp_sec_min = [len(g[g[init_mw_node][0]])+1,1]
            for node_i in g[init_mw_node]:
                if len(g[node_i]) < temp_sec_min[0]:
                    temp_sec_min = [len(g[node_i]), node_i]
                for check_i in range(len(g[node_i])):
                    if g[node_i][check_i] == init_mw_node:
                        del g[node_i][check_i]
                        break
            for node_i in g[temp_sec_min[1]]:
                for check_i in range(len(g[node_i])):
                    if g[node_i][check_i] == temp_sec_min[1]:
                        del g[node_i][check_i]
                        break
            del g[init_mw_node]
            del g[temp_sec_min[1]]
            matched += 2
        if len(g) > 1:
            checks = len(g[max(g, key=lambda key: len(g[key]))])
    return matched


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