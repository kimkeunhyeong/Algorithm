from itertools import combinations

N, M = map(int, input().split())
data = sorted(map(int, input().split()))

for i in combinations(data, M):
    print(*i)