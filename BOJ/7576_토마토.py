from sys import stdin
from collections import deque
# 수정 후, 98520KB, 1872ms
input = stdin.readline
width, height = map(int, input().split())

map_data = []
for i in range(height):
    map_data.append(list(map(int,input().split())))

Queue = deque()

for i in range(height):
    for j in range(width):
        if map_data[i][j] == 1:
            Queue.append((i, j, 0))

while Queue:
    y, x, days = Queue.popleft()
    for next_y, next_x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        if 0 <= next_y < height and 0 <= next_x < width and map_data[next_y][next_x] == 0:
            map_data[next_y][next_x] = 1
            Queue.append((next_y, next_x, days + 1))
    result = days

for i in range(height):
    for j in range(width):
        if map_data[i][j] == 0:
            result = -1
            break
    else:
        continue
    break # for else - break를 까먹지 말자!!!!

print(result)


"""
수정 전(107516KB, 2148ms)

from sys import stdin
from collections import deque

input = stdin.readline
width, height = map(int, input().split())

map_data = []
for i in range(height):
    map_data.append(list(map(int,input().split())))

Queue = deque()
Visited = [[None] * width for i in range(height)]

for i in range(height):
    for j in range(width):
        if map_data[i][j] == 1:
            Queue.append((i, j, 0))
        elif map_data[i][j] == -1:
            Visited[i][j] = -1

while Queue:
    y, x, days = Queue.popleft()
    if not Visited[y][x]:
        Visited[y][x] = days
        for next_y, next_x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if 0 <= next_y < height and 0 <= next_x < width and \
                not Visited[next_y][next_x] and map_data[next_y][next_x] == 0:
                map_data[next_y][next_x] = 1
                Queue.append((next_y, next_x, days + 1))
    result = days

for i in range(height):
    for j in range(width):
        if Visited[i][j] == None:
            result = -1
            break
    else:
        continue

print(result)
"""