from collections import Counter

num_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))
customers = int(input())

earning = 0

for _ in range(customers):
    shoe_price = list(map(int, input().split()))
    if (shoe_sizes.get(shoe_price[0]) and shoe_sizes.get(shoe_price[0]) > 0):
        earning += shoe_price[1]
        shoe_sizes[shoe_price[0]] -= 1
print(earning)