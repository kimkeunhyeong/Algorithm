from sys import stdin

input = stdin.readline

N = int(input())
data = []
DP = [[] for i in range(N - 1, 0, -1)]

for i in range(N):
    data.append(list(map(int, input().split())))
DP.append(data[-1])

for i in range(N-2, -1, -1):
    for j in range(i + 1):
        data[i][j] += max(data[i + 1][j], data[i + 1][j + 1])

print(data[0][0])