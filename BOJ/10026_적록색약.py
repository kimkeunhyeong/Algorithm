from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

def DFS(y, x, color, weakness = False):
    if Visited[y][x]:
        return 0
    
    Visited[y][x] = True
    flag = 1

    for i in range(4):
        next_y = y + move_y[i]
        next_x = x + move_x[i]
        if 0 <= next_y < N and 0 <= next_x < N and not Visited[next_y][next_x]:
            next_color = map_data[next_y][next_x]
            if next_color != color:
                if not weakness:
                    continue
                else:
                    if not (next_color and color):
                        continue

            DFS(next_y, next_x, color, weakness)
    
    return flag

input = stdin.readline

N = int(input())

map_data = []
move_y = [1, -1, 0, 0]
move_x = [0, 0, 1, -1]
mapping = {"B" : 0, "R" : 1, "G" : 2}
for i in range(N):
    string = input().rstrip()
    map_data.append([mapping[i] for i in string])

normal = weak = 0

Visited = [[False] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        normal += DFS(i, j, map_data[i][j])

Visited = [[False] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        weak += DFS(i, j, map_data[i][j], weakness = True)

print(normal, weak)