from sys import stdin
from math import inf
from heapq import *

input = stdin.readline

Vertex, Edge = map(int, input().split())
graph = [[] for i in range(Vertex + 1)]

start = int(input())
Heap = [(0, start)]

distance = [inf] * (Vertex + 1)
distance[start] = 0

for i in range(Edge):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    
# 다익스트라
while Heap:
    check_dist, check_node = heappop(Heap)
    if check_dist > distance[check_node]:
        continue
    for node, node_weight in graph[check_node]:
        new_weight = check_dist + node_weight
        if distance[node] > new_weight:
            distance[node] = new_weight
            # graph의 원소 순서랑 tuple의 원소 순서를 맞춰줬더니 heapQ가 제대로 작동하지 않아 시간초과가 발생함.
            # tuple은 1순위로 전자를 비교하고, 그 값이 같은 경우 후순위를 비교함에 유의!!
            # -> tuple 비교가 제대로 되지 않아 쓸데없는 update가 많이 발생하는 결과 초래.
            heappush(Heap, (new_weight, node))

for i in distance[1:]:
    if i != inf:
        print(i)
    else:
        print("INF")