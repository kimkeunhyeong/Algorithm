from sys import stdin

# 플로이드워셜 -> DFS로 교체
def DFS(i):
    for j in graph[i]:
        if not Visited[j]:
            Visited[j] = 1
            DFS(j)

input = stdin.readline

N = int(input())
map_data = [list(map(int, input().rstrip().split())) for i in range(N)]
graph = [[] for i in range(N)]

for i in range(N):
    for j in range(N):
        if map_data[i][j]:
            graph[i].append(j)

for i in range(N):
    # loop마다 i에서 0 ~ N까지 방문을 검사하는데, Visited가 N * N 사이즈의 하나의 리스트인 경우,
    # 이전 loop에서 방문했던 점을 방문할 수 없어 길이 있음에도 체크할 수 없음
    # -> 각 row마다 N 사이즈의 리스트 사용
    Visited = [0] * N
    DFS(i)
    print(*Visited)