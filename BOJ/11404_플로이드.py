from sys import stdin
from math import inf

def floyd():
    for k in range(1, city_cnt + 1):
        for i in range(1, city_cnt + 1):
            for j in range(1, city_cnt + 1):
                middle_dist = route[i][k] + route[k][j]
                route[i][j] = min(route[i][j], middle_dist)

input = stdin.readline

city_cnt = int(input())
bus_cnt = int(input())

# prep input
route = [[inf] * (city_cnt + 1) for i in range(city_cnt + 1)]
for i in range(1, city_cnt + 1):
    route[i][i] = 0

# get route info
for i in range(bus_cnt):
    start, end, cost = map(int, input().split())
    # 변경하면서 min부분이 삭제됨...
    route[start][end] = min(route[start][end], cost)

floyd()

for i in route[1:]:
    # i -> j 이동 불가인 경우 0 출력해줘야 함
    print(str(i[1:]).replace("inf", "0").replace(",", "")[1:-1])