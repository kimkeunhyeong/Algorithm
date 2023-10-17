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
    route[start][end] = cost

floyd()

for i in route[1:]:
    print(*i[1:])