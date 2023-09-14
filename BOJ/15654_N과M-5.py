from itertools import product

N, M = map(int, input().split())
data = sorted(map(int, input().split()))

for i in data:
    for j in product(filter(lambda x : x != i, data), repeat = M - 1):
        if len(set(j)) == M - 1:
            print(i, end = " ")
            print(*j)