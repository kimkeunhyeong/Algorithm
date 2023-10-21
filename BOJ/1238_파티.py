from sys import stdin
from heapq import *
from math import inf

def dijkstra(start, graph):
    distance = [inf] * (Village + 1)
    Visited = [False] * (Village + 1)

    distance[start] = 0
    Queue = [[0, start]]

    while Queue:
        dist, check_road = heappop(Queue)
        Visited[check_road] = True

        for road, time in graph[check_road]:
            if not Visited[road]:
                new_time = dist + time
                if distance[road] > new_time:
                    heappush(Queue, [new_time, road])
                    distance[road] = new_time

    return distance[1:]

input = stdin.readline

Village, Roads, Target_V = map(int, input().split())
graph = [[] for i in range(Village + 1)]
graph_reversed = [[] for i in range(Village + 1)]

for i in range(Roads):
    start, end, time = map(int, input().split())
    graph[start].append([end, time])
    graph_reversed[end].append([start, time])

result = 0

for start, end in zip(dijkstra(Target_V, graph), dijkstra(Target_V, graph_reversed)):
    result = max(result, start + end)

print(result)