from sys import stdin
from collections import deque

def BFS():
    y_move = [0, 0, 1, -1]
    x_move = [1, -1, 0, 0]
    Visited = [[-1] * width for i in range(height)]
    Visited[0][0] = 1
    Queue = deque()
    Queue.append([0, 0, 0]) # y, x, break:

    while Queue:
        now = Queue.popleft()
        next_dist = Visited[now[0]][now[1]] + 1

        for dy, dx in zip(y_move, x_move):
            next_y, next_x = now[0] + dy, now[1] + dx
            if 0 <= next_y < height and 0 <= next_x < width and Visited[next_y][next_x] == -1:
                if map_data[next_y][next_x] == "0": # 안막혀있으면 그냥 추가
                    Queue.append([next_y, next_x, now[2]])
                    Visited[next_y][next_x] = next_dist
                else: # 막혀있으면 break 썼는지 확인
                    if now[2] == 0:
                        Queue.append([next_y, next_x, 1])
                        Visited[next_y][next_x] = next_dist

    print(Visited[height - 1][width - 1])
input = stdin.readline

height, width = map(int, input().split())
map_data = [input().rstrip() for i in range(height)]

BFS()