from sys import stdin
from collections import deque

def BFS(A, B):
    people = 0
    Queue = deque()
    Queue.append((A, B))
    Visited = [[False] * width for i in range(height)] # 외부에서 쓸 일이 없다면 지역변수로 넣어주자..
    Visited[A][B] = True

    while Queue:
        y, x = Queue.popleft()
        for next_y, next_x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if 0 <= next_y < height and 0 <= next_x < width and map_data[next_y][next_x] != "X":
                if not Visited[next_y][next_x]:
                    Visited[next_y][next_x] = True
                    Queue.append((next_y, next_x))
                    if map_data[next_y][next_x] == "P":
                        people += 1
    # 큐에 넣고 꺼낼 때 방문 확인 & 처리보다 넣을 때 확인 & 방문처리가 104ms(21%) 빠름..
    """ if not Visited[y][x]: 넣을때 방문처리를 해서 연산을 줄입시다...
            Visited[y][x] = True
            if map_data[y][x] == "P":
                people += 1
            for next_y, next_x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if 0 <= next_y < height and 0 <= next_x < width and map_data[next_y][next_x] != "X":
                    Queue.append((next_y, next_x)) """
    return people

input = stdin.readline

height, width = map(int, input().split())
map_data = [input().rstrip() for i in range(height)]
people = 0

for i in range(height):
    for j in range(width):
        if map_data[i][j] == "I":
            break
    else:
        continue
    break

# print(people if people else "TT")
print(BFS(i, j) or "TT") # 반환값이 0 False 등등인 경우를 이용, if 대신 쓸수도 있음!