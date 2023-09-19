from sys import stdin

input = stdin.readline
size = int(input())

RGB_data = []
DP = [[0] * 3 for i in range(size)]
for i in range(size):
    RGB_data.append(list(map(int, input().split())))

DP[0] = RGB_data[0]
DP[1][0] = min(DP[0][1:]) + RGB_data[1][0]
DP[1][1] = min(DP[0][0], DP[0][2]) + RGB_data[1][1]
DP[1][2] = min(DP[0][:2]) + RGB_data[1][2]

for i in range(2, size):
    DP[i][0] = min(DP[i - 1][1:]) + RGB_data[i][0]
    DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + RGB_data[i][1]
    DP[i][2] = min(DP[i - 1][:2]) + RGB_data[i][2]

print(min(DP[-1]))