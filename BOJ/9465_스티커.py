from sys import stdin

input = stdin.readline

TC = int(input())
for _ in range(TC):
    width = int(input())
    data = [list(map(int, input().split())) for i in range(2)]
    DP = [[0] * width for i in range(2)]
    DP[0][0] = data[0][0]
    DP[1][0] = data[1][0]
    if width > 1:
        DP[0][1] = data[0][1] + DP[1][0]
        DP[1][1] = data[1][1] + DP[0][0]
    for i in range(2, width):
        two_minus = max(DP[0][i - 2], DP[1][i - 2])
        DP[0][i] = max(DP[1][i - 1], two_minus) + data[0][i]
        DP[1][i] = max(DP[0][i - 1], two_minus) + data[1][i]

    print(max(DP[0][width - 1], DP[1][width - 1]))