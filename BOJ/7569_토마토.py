from sys import stdin
from collections import deque

def BFS(g):
    global days
    Queue = deque()
    for i in g:
        Queue.append(i)
    
    while Queue:
        days += 1
        for _ in range(len(Queue)):
            z, y, x = Queue.popleft()
            for next_z, next_y, next_x in [(z, y, x + 1), (z, y, x - 1),
                                           (z, y + 1, x), (z, y - 1, x),
                                           (z + 1, y, x), (z - 1, y, x)]:
                if 0 <= next_z < height and 0 <= next_y < length and 0 <= next_x < width and \
                    tomato[next_z][next_y][next_x] != -1:
                    if tomato[next_z][next_y][next_x] == 0:
                        tomato[next_z][next_y][next_x] = 1
                        Queue.append((next_z, next_y, next_x))
    return days

input = stdin.readline

width, length, height = map(int, input().split())
tomato = []
graph = []
not_ripen = False

for i in range(height):
    floor = []
    for j in range(length):
        data = list(map(int, input().split()))
        floor.append(data)
        for k, value in enumerate(data): # 하단의 토마토 체크용 for-loop를 통합
            match value:
                case 0:
                    not_ripen = True
                case 1:
                    graph.append((i, j, k))
    tomato.append(floor)

days = -1 # BFS 마지막 loop는 모두 Visited이므로 1을 뺴줘야 함

if not_ripen:
    BFS(graph)
    # BFS 실행 후 안익은 토마토 검색
    for i in range(height):
        for j in range(length):
            for k in range(width):
                if not tomato[i][j][k]:
                    print(-1)
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print(days)
# 이미 익은 토마토만 있는 경우, 0 출력
else:
    print(0)