import heapq
def solution(banana_list):
    # Helper function to check if two trainers will enter an infinite loop
    def loop(x, y):
        base = int((x + y) / gcd(x, y))
        return bool(base & (base - 1))

    # Helper function to find the greatest common divisor of two numbers
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # Generate a graph where each node represents a trainer and an edge represents a pair of trainers that will enter an infinite loop
    def generate_graph(l):
        G = {i: [] for i in range(len(l))}
        for i in range(len(l)):
            for j in range(i, len(l)):
                if i != j and loop(l[i], l[j]):
                    G[i].append(j)
                    G[j].append(i)
        return G

    # Reduce the graph by iteratively removing pairs of nodes until there are no more matches possible
    def reduce(g):
        matched = 0
        while len(g) > 1:
            # Create a list of nodes and their degrees, and turn it into a heap
            node_degrees = [(len(g[node]), node) for node in g]
            heapq.heapify(node_degrees)
            
            # Pop the node with the smallest degree from the heap
            _, node = heapq.heappop(node_degrees)
            # If the node's degree is less than 1, remove it from the graph
            if len(g[node]) < 1:
                for node_i in list(g.keys()):
                    g[node_i] = [n for n in g[node_i] if n != node]
                del g[node]
                continue
            
            # Find the neighbor of the node with the smallest degree
            temp_sec_min = min(g[node], key=lambda node_i: len(g[node_i]))
            # If the neighbor's degree is less than 1, remove it from the graph
            if len(g[temp_sec_min]) < 1:
                for node_i in list(g.keys()):
                    g[node_i] = [n for n in g[node_i] if n != temp_sec_min]
                del g[temp_sec_min]
                continue
            
            # Remove the node and its neighbor from the graph
            for node_i in (node, temp_sec_min):
                for node_j in list(g.keys()):
                    g[node_j] = [n for n in g[node_j] if n != node_i]
            del g[node]
            del g[temp_sec_min]
            
            # Increase the count of matched pairs
            matched += 2
            
            # If there are still nodes left in the graph, update the heap
            if len(g) > 1:
                node_degrees = [(len(g[node]), node) for node in g if len(g[node]) > 0]
                heapq.heapify(node_degrees)
        return matched

    # Generate the graph and reduce it
    g = generate_graph(banana_list)
    matches = reduce(g)
    
    # The number of trainers left to watch the workers is the number of nodes left in the graph
    return len(banana_list) - matches


# Testing the solution function with the provided test cases
print(solution([1,1])) # Expected output: 2
print(solution([1, 7, 3, 21, 13, 19])) # Expected output: 0
print(solution([1, 7, 13, 3, 19, 21])) # Expected output: 0


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