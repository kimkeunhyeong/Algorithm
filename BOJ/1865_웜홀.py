from sys import stdin
from math import inf

def Bell(g, start):
    Visited = [inf] * (point_cnt + 1)
    Visited[start] = 0
    
    for repeat in range(point_cnt - 1):
        for point in range(1, point_cnt + 1):
            for connected in g[point]:
                if Visited[connected[0]] > Visited[point] + connected[1]:
                    Visited[connected[0]] = Visited[point] + connected[1]
    
    for point in range(1, point_cnt + 1):
        for connected in g[point]:
            if Visited[connected[0]] > Visited[point] + connected[1]:
                return True
    
    return False

input = stdin.readline
TC = int(input())

for i in range(TC):
    point_cnt, road_cnt, hole_cnt = map(int, input().split())
    graph = [[] for i in range(point_cnt + 1)]

    for i in range(road_cnt):
        start, end, time = map(int, input().split())
        graph[start].append([end, time])
        graph[end].append([start, time])
    for i in range(hole_cnt):
        start, end, time = map(int, input().split())
        graph[start].append([end, -time])
    
    # 자기자신으로 돌아오고자 할 때, 음수가 되는 경우를 찾는다.
    # -> 벨만포드에서 음수 사이클이 발생하면 음수가 됨.
    # 근데 시작지점이 지정되어있지 않은데 모든 정점에 대해 검사하면 시간초과 안뜨나?
    backward = False
    for i in range(1, point_cnt + 1):
        backward = backward or Bell(graph, i)

    print("YES" if backward else "NO")