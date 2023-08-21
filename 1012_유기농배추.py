from sys import stdin
from collections import deque

input = stdin.readline
TC = int(input())

for _ in range(TC):
    width, height, count = map(int, input().split())
    map_data = [[False] * width for __ in range(height)]
    Visited = set()
    cabb_data = []

    for __ in range(count):
        x, y = map(int, input().split())
        cabb_data.append((y, x))
        map_data[y][x] = True
    
    Queue = deque()
    Queue.append(cabb_data.pop())
    bug_cnt = 1

    while cabb_data and Queue: # 체크할 배추가 있으면 검사
        check = Queue.popleft()

        if check not in Visited:
            Visited.add(check)
            y, x = check
            for next_y, next_x in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if 0 <= next_y < height and 0 <= next_x < width and map_data[next_y][next_x]:
                    Queue.append((next_y, next_x))

        while not Queue and cabb_data: # 큐가 빈 경우 체크하지 않은 배추 위치를 추가
            next = cabb_data.pop()
            if next not in Visited:
                Queue.append(next)
                bug_cnt += 1
    print(bug_cnt)