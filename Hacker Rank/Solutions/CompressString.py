from itertools import groupby

S = input()

for k, g in groupby(S):
    print((len(list(g)), int(k)), end = ' ')