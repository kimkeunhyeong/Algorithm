from sys import stdin
from heapq import *

input = stdin.readline
N = int(input())

heap = []
result = []
for _ in range(N):
    number = int(input())
    if number == 0:
        if len(heap):
            print(heappop(heap)[1])
        else:
            print(0)
    else:
        heappush(heap, (abs(number), number))