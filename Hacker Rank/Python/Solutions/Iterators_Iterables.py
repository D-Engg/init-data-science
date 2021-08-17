import itertools

list_size = int(input())
let_list = input().split()
idx = int(input())
fact = 0

indices = [ i + 1 for i in range(len(let_list)) if let_list[i] == 'a']

combos = [*itertools.combinations([i for i in range(1, list_size + 1)], r = idx)]

for x in combos:
    temp = 0
    for i in indices:
        if i in x and temp == 0:
            fact += 1
            temp += 1

print(fact/len(combos))