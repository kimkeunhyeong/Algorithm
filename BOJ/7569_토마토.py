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
            # 기존코드가 더 보기 쉬운 반면, 검사가 필요하지 않은 z, y, x에도 범위 검사를 시행하므로 연산량이 많아 느림.
            # if문으로 필요한 범위만 검사하면 좌표수는 6개로 동일하나, 검사가 1/3으로 줄어듦 (z & y & x -> z | y | x)
            # -1(빈 공간) 검사 없이 0만 검사해도 결과에 영향을 끼치지 않으므로 제외.
            if z > 0 and not tomato[z - 1][y][x]:
                tomato[z - 1][y][x] = 1
                Queue.append((z - 1, y, x))
            if z + 1 < height and not tomato[z + 1][y][x]:
                tomato[z + 1][y][x] = 1
                Queue.append((z + 1, y, x))
            if y > 0 and not tomato[z][y - 1][x]:
                tomato[z][y - 1][x] = 1
                Queue.append((z, y - 1, x))
            if y + 1 < length and not tomato[z][y + 1][x]:
                tomato[z][y + 1][x] = 1
                Queue.append((z, y + 1, x))
            if x > 0 and not tomato[z][y][x - 1]:
                tomato[z][y][x - 1] = 1
                Queue.append((z, y, x - 1))
            if x + 1 < width and not tomato[z][y][x + 1]:
                tomato[z][y][x + 1] = 1
                Queue.append((z, y, x + 1))
    # 기존 코드.
    """         for next_z, next_y, next_x in [(z, y, x + 1), (z, y, x - 1),
                                           (z, y + 1, x), (z, y - 1, x),
                                           (z + 1, y, x), (z - 1, y, x)]:
                if 0 <= next_z < height and 0 <= next_y < length and 0 <= next_x < width and \
                    tomato[next_z][next_y][next_x] != -1:
                    if tomato[next_z][next_y][next_x] == 0:
                        tomato[next_z][next_y][next_x] = 1
                        Queue.append((next_z, next_y, next_x)) """
    
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