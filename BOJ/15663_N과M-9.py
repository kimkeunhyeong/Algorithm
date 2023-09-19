from itertools import product
from collections import Counter

M, N = map(int, input().split())
data = list(map(int, input().split()))
count = Counter(data)

for i in sorted(set(product(data, repeat = N))):
    for key, value in Counter(i).items():
        if count[key] < value:
            break
    else:
        print(*i)