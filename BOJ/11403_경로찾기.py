from sys import stdin

input = stdin.readline

N = int(input())
map_data = [list(map(int, input().rstrip().split())) for i in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if not map_data[i][j]:
                if map_data[i][k] and map_data[k][j]:
                    map_data[i][j] = 1

for i in map_data:
    print(*i)