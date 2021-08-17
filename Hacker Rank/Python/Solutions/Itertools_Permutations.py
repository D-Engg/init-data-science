from itertools import permutations

A, n = input().split()

print(*[''.join(x) for x in permutations(sorted(A), r = int(n))], sep = '\n')