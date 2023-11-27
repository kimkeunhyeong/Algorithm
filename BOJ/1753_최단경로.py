from sys import stdin
from math import inf
from heapq import *

input = stdin.readline

Vertex, Edge = map(int, input().split())
graph = [[] for i in range(Vertex + 1)]

start = int(input())
Heap = [(start, 0)]

distance = [inf] * (Vertex + 1)
distance[start] = 0

for i in range(Edge):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    
# 다익스트라
while Heap:
    check_node, check_dist = heappop(Heap)
    if check_dist > distance[check_node]:
        continue
    for node, node_weight in graph[check_node]:
        new_weight = check_dist + node_weight
        if distance[node] > new_weight:
            distance[node] = new_weight
            heappush(Heap, (node, new_weight))

for i in distance[1:]:
    if i != inf:
        print(i)
    else:
        print("INF")