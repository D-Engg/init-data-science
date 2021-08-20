try:
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))[ : n]
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    
    print(sum((i in A) - (i in B) for i in arr))
    
except Exception as e:
    print('Some error occured')
