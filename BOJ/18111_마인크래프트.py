import math
from sys import stdin
from collections import Counter

input = stdin.readline
height, width, blocks = map(int, input().split())
map_data = []

for i in range(height):
    # 굳이 2차원 데이터가 필요하지는 않을 것 같다.
    map_data.extend(map(int, input().split()))
map_data = dict(Counter(map_data))

min_height, max_height = min(map_data.keys()), max(map_data.keys())
time, result_height = math.inf, 0

for target_height in range(min_height, max_height+1):
    positive = negative = 0
    for i in map_data.keys():
        gap = i - target_height
        if gap < 0:
            negative += gap * map_data[i]
        else:
            positive += gap * map_data[i]
    if positive + negative + blocks < 0 :
        # 블록이 모자라서 통과
        continue
    else:
        calced_time = 2 * positive - negative
        if calced_time <= time:
            if calced_time == time:
                result_height = max(result_height, target_height)
            else:
                time, result_height = calced_time, target_height

print(time, result_height)