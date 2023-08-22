from sys import stdin
from collections import deque
def BFS(start):
    global Visited
    global map_data
    global group

    Queue = deque()
    Queue.append(start)
    group.append(0)

    while Queue:
        y, x = Queue.popleft()
        if not Visited[y][x]:
            Visited[y][x] = True
            group[-1] += 1
            for next_y, next_x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if 0 <= next_y < N and 0 <= next_x < N and map_data[next_y][next_x] == "1":
                    Queue.append((next_y, next_x))
input = stdin.readline

N = int(input())
map_data = []
Visited = [[False] * N for i in range(N)]
group = []

for i in range(N):
    map_data.append(input().rstrip())

for i in range(N):
    for j in range(N):
        if map_data[i][j] == "1" and not Visited[i][j]:
            BFS((i, j))
            
group.sort()
print(len(group), *group, sep="\n")