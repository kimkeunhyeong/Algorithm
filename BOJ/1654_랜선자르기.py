from sys import stdin
import time
input = stdin.readline

line_cnt, target_count = map(int, input().split())
data = []
for i in range(line_cnt):
    data.append(int(input()))

right = max(data) + 1
left = 0

while right > left and right != (left + 1):
    middle = (left + right) // 2
    count = 0
    for i in data:
        count += i // middle
    if count >= target_count:
        left = middle
    else:
        right = middle
        
print(left)