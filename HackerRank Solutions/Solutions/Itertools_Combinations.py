from itertools import combinations

A, n = input().split()

for i in range(1, int(n) + 1):
    for j in combinations(sorted(A), i):
        print(''.join(j))