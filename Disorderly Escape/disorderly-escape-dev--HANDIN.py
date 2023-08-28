from math import factorial
from fractions import gcd
from collections import Counter

# Function to generate integer partitions
def integer_partitions(n, i=1):
    yield [n]
    for i in range(i, n // 2 + 1):
        for p in integer_partitions(n - i, i):
            yield [i] + p

# Function to calculate conjugacy size
def conjugacy_size(nums):
    ans = Counter(nums)  # Count the occurrences of each number in nums
    s = sum(nums)
    res = factorial(s)
    for num, count in ans.items():
        res = res // (pow(num, count) * factorial(count))

    return res

# Main solution function
def solution(w, h, s):
    answer = 0
    for c in integer_partitions(w):
        for r in integer_partitions(h):
            m = conjugacy_size(r) * conjugacy_size(c)
            answer += m * pow(s, sum([sum([gcd(i, j) for i in r]) for j in c]))
    answer = answer // (factorial(w) * factorial(h))
    return str(answer)

# Test the function
print(solution(2, 2, 2))  # Output: "7"
print(solution(2, 3, 4))  # Output: "430"